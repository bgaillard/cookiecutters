# Cookiecutters

[Cookiecutter: Better Project Templates](https://cookiecutter.readthedocs.io/)

## Setup

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Install cookiecutter
python -m pip install --user cookiecutter
```

## Usage

```bash
# Cd to the directory where you want to create the project
cd /path/to/your/projects

# Run cookiecutter
cookiecutter ~/workspace/cookiecutters/python/fast-api-simple
```

## Testing

```bash
# Testing the 'python/simple' cookiecutter
python -m pip install --user cookiecutter
cd python simple
make test
```
