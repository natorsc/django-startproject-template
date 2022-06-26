# -*- coding: utf-8 -*-
"""Copie para a raiz do projeto antes de usar."""

from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    migrations_dir = BASE_DIR.rglob('migrations')
    for dirs in migrations_dir:
        for file in dirs.rglob('*.py*'):
            if file.stem != '__init__':
                file.unlink()
                print(f'file {file} removed.')
    print('[!] clean [!]')
