# Cookiecutters

Carefully designed collection of [Cookiecutter](https://cookiecutter.readthedocs.io/) templates for various project types.

## Philosophy

Each template tries to implement best practices, here are few of them:

- `README.md` file with indications to quickly start
- `CHANGELOG.md` file based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) principles
- Use of [Semantic Versioning](https://semver.org/)
- Makefiles with commands for common tasks (e.g. building, testing, running, linting, formatting)
- Source code linted with best linters and reporting no issue
- Usage of [pre-commit](https://pre-commit.com/) to run linters and formatters before each commit
- Dependencies and transitive dependencies continuously updated using [Dependabot](https://dependabot.com/) or [Renovate](https://docs.renovatebot.com/)
- Dockerfiles optimized for image size and performance to quickly deploy them to any environment
- Structured logging frameworks configured with sensible defaults
- Sample dotenv files to manage environment variables
- Configuration file for application parameters
- Unit and integration tests ready to use, high code coverage and coverage reports already configured
- Use of [semantic-release](https://python-semantic-release.readthedocs.io/) or [Release Please](https://github.com/googleapis/release-please) to automatically manage releases and changelogs
- Preconfigured CI/CD pipelines using [GitHub Actions](https://github.com/features/actions), [Gitlab CI/CD](https://docs.gitlab.com/ci/) or others
- Badges taken from [shields.io](https://shields.io/) or [Markdown Badges](https://github.com/Ileriayo/markdown-badges) to show build status, code coverage, technologies, etc.

## Usage

Just install [cookiecutter](https://cookiecutter.readthedocs.io/) and run it pointing to the desired template.

```bash
# Install cookiecutter with 'pip' or 'pipx'
python -m pip install --user cookiecutter
# or
pipx install cookiecutter

# Run cookiecutter pointing to the desired template (here 'python/fast-api-simple' as an example)
cd ~/workspace
cookiecutter https://github.com/bgaillard/cookiecutters.git --directory python/fast-api-simple
```

## Available templates

Each template has a much more detailed `README.md` file explaining how to use it and its features.

| Technology | Template name                                                | Description                 |
|------------|--------------------------------------------------------------|-----------------------------|
| Python     | [`python/fast-api-simple`](python/fast-api-simple/README.md) | Simple FastAPI application. |
| Python     | [`python/simple`](python/simple/README.md)                   | Simple Python application.  |
