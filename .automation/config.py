"""Configuração central: lê o .env e define paths derivados."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Carrega .env do diretório do projeto (não falha se não existir)
load_dotenv(Path(__file__).resolve().parent / ".env")


@dataclass(frozen=True)
class Config:
    groq_api_key: str
    vault_path: Path
    notes_dir: Path
    github_repo: str
    default_tag: str
    git_branch: str


def load_config() -> Config:
    """Lê as variáveis de ambiente e monta o objeto Config.

    Levanta RuntimeError se algo essencial estiver faltando.
    """
    groq_api_key = os.getenv("GROQ_API_KEY", "").strip()
    vault_path = Path(os.getenv("VAULT_PATH", "").strip()).expanduser()
    notes_subdir = os.getenv("NOTES_SUBDIR", "Research").strip()
    github_repo = os.getenv("GITHUB_REPO", "").strip()
    default_tag = os.getenv("DEFAULT_TAG", "research").strip()
    git_branch = os.getenv("GIT_BRANCH", "main").strip()

    if not str(vault_path):
        raise RuntimeError("VAULT_PATH não definido no .env")

    return Config(
        groq_api_key=groq_api_key,
        vault_path=vault_path,
        notes_dir=vault_path / notes_subdir,
        github_repo=github_repo,
        default_tag=default_tag,
        git_branch=git_branch,
    )
