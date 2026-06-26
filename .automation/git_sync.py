"""Sincronização com Git via subprocess (add, commit, push).

Trata erros silenciosamente: se não houver nada novo para commitar,
não levanta exceção nem quebra o pipeline.
"""
from __future__ import annotations

import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Fuso de Brasília (UTC-3, fixo — Brasil não usa horário de verão desde 2019),
# consistente com formatter.py/scraper.py: mantém a mensagem de commit no mesmo
# fuso dos nomes de arquivo, em vez do UTC do runner do GitHub Actions.
_BRT = timezone(timedelta(hours=-3))


def _run(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    """Roda um comando git capturando stdout/stderr, sem levantar exceção."""
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )


def _has_changes(repo_path: Path) -> bool:
    """True se houver algo staged/unstaged para commitar."""
    result = _run(["status", "--porcelain"], repo_path)
    return bool(result.stdout.strip())


def sync(repo_path: Path, branch: str = "main", note_count: int = 0) -> bool:
    """Executa add → commit → push. Retorna True se algo foi enviado.

    Nunca levanta exceção: em caso de falha, loga e retorna False.
    """
    repo_path = Path(repo_path)

    if not (repo_path / ".git").exists():
        print(f"❌ {repo_path} não é um repositório git (pulei o sync)")
        return False

    if not _has_changes(repo_path):
        print("📭 Nada novo para commitar.")
        return False

    timestamp = datetime.now(tz=_BRT).strftime("%Y-%m-%d %H:%M")
    message = f"auto: {timestamp} — {note_count} notas adicionadas"

    add = _run(["add", "."], repo_path)
    if add.returncode != 0:
        print(f"❌ git add falhou: {add.stderr.strip()}")
        return False

    commit = _run(["commit", "-m", message], repo_path)
    if commit.returncode != 0:
        # Provavelmente "nothing to commit" — não é erro fatal
        print(f"⚠️  git commit não gerou commit: {commit.stdout.strip() or commit.stderr.strip()}")
        return False
    print(f"📝 Commit: {message}")

    push = _run(["push", "origin", branch], repo_path)
    if push.returncode != 0:
        print(f"❌ git push falhou: {push.stderr.strip()}")
        return False

    print(f"🚀 Push concluído para origin/{branch}")
    return True
