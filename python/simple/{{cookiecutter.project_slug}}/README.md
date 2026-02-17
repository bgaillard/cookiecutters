# Simple project

## Development

{% if cookiecutter.package_manager == "poetry" %}
```bash
# Update the 'poetry.lock' file / update the dependencies
make update

# Build the development Docker image
make build-dev
```
{% endif %}

{% if cookiecutter.package_manager == "uv" %}
```bash
# Use Nvim with uv venv
uv run nvim

# Update the 'uv.lock' file / update the dependencies
make update

# Run the application using the production Docker image
make run-dev

# Run the application using the production Docker image
make run
```
{% endif %}
