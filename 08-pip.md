# Setup a project 

## Prepare virtual env for python
```bash
pip3 install virtualenv
pip3 list
mkdir ~/.venvs
virtualenv ~/.venvs/{folder}
. ~/.venvs/{folder}/bin/activate
which python # or python --version
```
_Notes:_
- `folder` is the name of the folder holding your python version config


## Prepare project structure
```bash
mkdir {project} # name of your project
cd {project}
mkdir bin {MAIN} tests docs
touch {MAIN}/__init__.py
touch tests/__init__.py
```
_Notes:_
- `bin` is for scripts to run on CLI
- `tests` hold your test files
- `docs` hold your documentation
- `{MAIN}` is the name of your main module

## Create setup.py
```python
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'My project',
  'author': 'My name',
  'url': 'http://url.com',
  'download_url': 'http://url.com',
  'author_email': 'me@email.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['MAIN'],
  'scripts': [],
  'name': 'projectName'
}
setup(**config)
```

## Final structure
The final structure should look like
```
project/
     MAIN/
         __init__.py
     bin/
     docs/
     setup.py
     tests/
         MAIN_tests.py
         __init__.py
```

## Run test with `nose`
```bash
pip install nose
nosetests
```
Also check:
- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://docs.pytest.org/en/stable/getting-started.html)

