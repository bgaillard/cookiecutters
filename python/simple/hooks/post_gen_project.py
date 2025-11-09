import os

def strtobool(value: str) -> bool:
  value = value.lower()
  if value in ("y", "yes", "on", "1", "true", "t"):
    return True
  return False

package_manager: str = "{{ cookiecutter.package_manager }}"
execute_package_manager_in_docker: bool = strtobool("{{ cookiecutter.execute_package_manager_in_docker }}")

if package_manager == "uv":
    os.remove(".github/dependabot.poetry.yml")
    os.remove("Dockerfile.docker.poetry")
    os.remove("Dockerfile.poetry")
    os.remove("Makefile.docker.poetry")
    os.remove("Makefile.poetry")
    os.remove("poetry.lock")

    os.rename(".github/dependabot.uv.yml", ".github/dependabot.yml")

    if execute_package_manager_in_docker:
        os.remove("Dockerfile.uv")
        os.remove("Makefile.uv")
        os.rename("Dockerfile.docker.uv", "Dockerfile")
        os.rename("Makefile.docker.uv", "Makefile")
    else:
        os.remove("Dockerfile.docker.uv")
        os.remove("Makefile.docker.uv")
        os.rename("Dockerfile.uv", "Dockerfile")
        os.rename("Makefile.uv", "Makefile")

elif package_manager == "poetry":
    os.remove(".github/dependabot.uv.yml")
    os.remove("Dockerfile.docker.uv")
    os.remove("Dockerfile.uv")
    os.remove("Makefile.docker.uv")
    os.remove("Makefile.uv")
    os.remove("uv.lock")

    os.rename(".github/dependabot.poetry.yml", ".github/dependabot.yml")

    if execute_package_manager_in_docker:
        os.remove("Dockerfile.poetry")
        os.remove("Makefile.poetry")
        os.rename("Dockerfile.docker.poetry", "Dockerfile")
        os.rename("Makefile.docker.poetry", "Makefile")
    else:
        os.remove("Dockerfile.docker.poetry")
        os.remove("Makefile.docker.poetry")
        os.rename("Dockerfile.poetry", "Dockerfile")
        os.rename("Makefile.poetry", "Makefile")
