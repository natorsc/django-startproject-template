# Django startproject template

Template para iniciar um novo projeto com a linguagem de programação Python e o framework web Django. 

## Como usar

```bash
mkdir nome-do-projeto && cd nome-do-projeto
```

```bash
python3 -m venv venv && source venv/bin/activate
```

```bash
pip install django
```

```bash
django-admin startproject \
_config \
. \
--extension md,txt \
--name=Procfile \
--template https://github.com/natorsc/django-startproject-template/archive/main.zip
```

```bash
pip install -r requirements-dev.txt
```

---

## 💡 Extra

### Poetry

#### requirements.txt

Para gerar o arquivo de dependências `requirements.txt` através do [Poetry](https://python-poetry.org/) utilizar o comando:

```bash
poetry export \
--without-hashes \
-f requirements.txt \
-o requirements.txt
```

Para gerar o arquivo com as dependências de desenvolvimento (`requirements-dev.txt`):

```bash
poetry export \
--dev \
--without-hashes \
-f requirements.txt \
-o requirements-dev.txt
```

---
