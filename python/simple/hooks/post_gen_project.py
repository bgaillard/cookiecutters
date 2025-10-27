import logging
import os

logging.basicConfig(level=logging.DEBUG)

current_working_directory: str = os.getcwd()

logging.debug(f"Current working directory: {current_working_directory}")

for f in os.listdir(current_working_directory):
    logging.debug(f"Found file/directory: {f}")

project_name: str = "{{ cookiecutter.project_name }}"

docker_build_tool: str = "{{ cookiecutter.docker_build_tool }}"
package_manager: str = "{{ cookiecutter.package_manager }}"
execute_package_manager_in_docker: str = "{{ cookiecutter.execute_package_manager_in_docker }}"

if package_manager == "uv":
    os.remove("Dockerfile.docker.poetry")
    os.remove("Dockerfile.poetry")
    os.remove("Makefile.docker.poetry")
    os.remove("Makefile.poetry")
    os.remove("poetry.lock")
