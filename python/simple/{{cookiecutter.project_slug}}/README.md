# Simple project

## Setup instructions

Pick the right Makefile and Dockerfile, then delete this file and the other setup files (Makefile and Dockerfile files).

### Available setups 

| Tool                   | Makefile                | Dockerfile                   |
|------------------------|-------------------------|------------------------------|
| `uv`                   | `Makefile.uv`           | `Dockerfile.uv`              |
| `uv` inside Docker     | `Makefile.docker.uv`    | `Dockerfile.docker.uv`       |
| `poetry`               | `Makefile.poetry`       | `Dockerfile.poetry`          |
| `poetry` inside Docker | `Makefile.docker.poetry`| `Dockerfile.docker.poetry`   |

### Sample startup commands

Suppose you picked `uv` inside Docker setup:

```bash
# Pick the right files
mv Makefile.docker.uv Makefile
mv Dockerfile.docker.uv Dockerfile
mv README.docker.uv.md README.md

# Remove other setup files
rm {Makefile,Dockerfile,README,SETUP}.*
```

## Development

```bash
# Use Nvim with uv venv
uv run nvim

# Generate the 'poetry.lock' file / update the Poetry dependencies
make poetry-update

# Build the development Docker image
make build-dev

# Run the main program using the development Docker image
make run-dev
```
