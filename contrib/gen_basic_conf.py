# -*- coding: utf-8 -*-
"""Arquivo é utilizado para automatizar algumas tarefas."""

import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_SAMPLE = BASE_DIR.joinpath('contrib', 'env-sample.env')
REQUIREMENTS_FILE = BASE_DIR.joinpath('requirements.txt')
REQUIREMENTS_DEV_FILE = BASE_DIR.joinpath('requirements-dev.txt')

# Creating .env.
shutil.copy2(ENV_SAMPLE, BASE_DIR.joinpath('.env'))

# Creating requirements.txt.
# subprocess.call(
#     ['poetry', 'export', '--without-hashes', '-f', 'requirements.txt',
#      '--output', f'{REQUIREMENTS_FILE}'],
#     cwd=BASE_DIR,
# )

# Creating requirements.txt (dev).
# subprocess.call(
#     ['poetry', 'export', '--dev', '--without-hashes', '-f',
#      'requirements.txt', '--output', f'{REQUIREMENTS_DEV_FILE}'],
#     cwd=BASE_DIR,
# )

# Get migrations.
subprocess.call(
    ['poetry', 'run', 'python', 'manage.py', 'makemigrations'],
    cwd=BASE_DIR,
)

# Run migrate.
subprocess.call(
    ['poetry', 'run', 'python', 'manage.py', 'migrate'],
    cwd=BASE_DIR,
)

# Run collectstatic.
subprocess.call(
    ['poetry', 'run', 'python', 'manage.py', 'collectstatic', '--noinput'],
    cwd=BASE_DIR,
)

# Create superuser.
subprocess.call(
    ['poetry', 'run', 'python', 'manage.py', 'createsuperuser'],
    cwd=BASE_DIR,
)
