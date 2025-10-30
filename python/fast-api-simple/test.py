from cookiecutter.main import cookiecutter  # pyright: ignore[reportMissingTypeStubs, reportUnknownVariableType]
from pathlib import Path

PROJECT_NAME: str = "sample_fastapi_project"

COMMON_FILE_NAMES: list[str] = [
    ".dockerignore",
    ".env.local",
    ".env.test",
    ".gitattributes",
    ".gitignore",
    ".python-version",
    "CHANGELOG.md",
    "Dockerfile",
    "Makefile",
    "README.md",
    "app",
    "pyproject.toml",
    "setup.cfg",
]
POETRY_FILE_NAMES: list[str] = COMMON_FILE_NAMES + [
    "poetry.lock",
]
UV_FILE_NAMES: list[str] = COMMON_FILE_NAMES + [
    "uv.lock",
]

def assert_file_contains(file_path: Path, expected_content: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        content: str = f.read()
        assert expected_content in content


def assert_file_exists(project_dir: Path, expected_file_names: list[str]) -> None:
    for f in Path(project_dir).iterdir():
        assert f.name in expected_file_names


def test_default(tmp_path: Path) -> None:
    project_dir: Path = Path(
        cookiecutter(
            template=".",
            no_input=True,
            output_dir=str(tmp_path),
        )
    )

    # Ensure the project directory was created
    assert project_dir.exists()
    assert project_dir.name == PROJECT_NAME
    assert project_dir == Path(tmp_path).joinpath(PROJECT_NAME)

    # Ensure expected files exist
    assert_file_exists(project_dir, UV_FILE_NAMES)

    # Ensure the 'Dockerfile' is the right one
    dockerfile: Path = project_dir.joinpath("Dockerfile")
    assert_file_contains(dockerfile, "UV_COMPILE_BYTECODE=1")
    assert_file_contains(dockerfile, "--uid 1000")

    # Ensure the 'Makefile' is the right one
    makefile: Path = project_dir.joinpath("Makefile")
    assert_file_contains(makefile, "UV ?= uv")


def test_with_poetry(tmp_path: Path) -> None:
    project_dir: Path = Path(
        cookiecutter(  # pyright: ignore[reportUnknownArgumentType]
            template=".",  
            no_input=True,
            extra_context={"package_manager": "poetry"},
            output_dir=str(tmp_path),
        )
    )

    # Ensure the project directory was created
    assert project_dir.exists()
    assert project_dir.name == PROJECT_NAME
    assert project_dir == Path(tmp_path).joinpath(PROJECT_NAME)

    # Ensure expected files exist
    assert_file_exists(project_dir, POETRY_FILE_NAMES)

    # Ensure the 'Dockerfile' is the right one
    dockerfile: Path = project_dir.joinpath("Dockerfile")
    assert_file_contains(dockerfile, "POETRY_CACHE_DIR=")
    assert_file_contains(dockerfile, "--uid 1000")

    # Ensure the 'Makefile' is the right one
    makefile: Path = project_dir.joinpath("Makefile")
    assert_file_contains(makefile, "POETRY ?= poetry")


def test_with_poetry_in_docker(tmp_path: Path) -> None:
    project_dir: Path = Path(
        cookiecutter(  # pyright: ignore[reportUnknownArgumentType]
            template=".",
            no_input=True,
            extra_context={
                "package_manager": "poetry",
                "execute_package_manager_in_docker": True,
            },
            output_dir=str(tmp_path),
        )
    )

    # Ensure the project directory was created
    assert project_dir.exists()
    assert project_dir.name == PROJECT_NAME
    assert project_dir == Path(tmp_path).joinpath(PROJECT_NAME)

    # Ensure expected files exist
    assert_file_exists(project_dir, POETRY_FILE_NAMES)

    # Ensure the 'Dockerfile' is the right one
    dockerfile: Path = project_dir.joinpath("Dockerfile")
    assert_file_contains(dockerfile, "POETRY_NO_INTERACTION=1")
    assert_file_contains(dockerfile, "--uid $USER_ID")

    # Ensure the 'Makefile' is the right one
    makefile: Path = project_dir.joinpath("Makefile")
    assert_file_contains(makefile, "POETRY_BUILDER_BASE")


def test_with_uv(tmp_path: Path) -> None:
    project_dir: Path = Path(
        cookiecutter(  # pyright: ignore[reportUnknownArgumentType]
            template=".",
            no_input=True,
            extra_context={"package_manager": "uv"},
            output_dir=str(tmp_path),
        )
    )

    # Ensure the project directory was created
    assert project_dir.exists()
    assert project_dir.name == PROJECT_NAME
    assert project_dir == Path(tmp_path).joinpath(PROJECT_NAME)

    # Ensure expected files exist
    assert_file_exists(project_dir, UV_FILE_NAMES)

    # Ensure the 'Dockerfile' is the right one
    dockerfile: Path = project_dir.joinpath("Dockerfile")
    assert_file_contains(dockerfile, "UV_COMPILE_BYTECODE=1")
    assert_file_contains(dockerfile, "--uid 1000")

    # Ensure the 'Makefile' is the right one
    makefile: Path = project_dir.joinpath("Makefile")
    assert_file_contains(makefile, "UV ?= uv")


def test_with_uv_in_docker(tmp_path: Path) -> None:
    project_dir: Path = Path(
        cookiecutter(  # pyright: ignore[reportUnknownArgumentType]
            template=".",
            no_input=True,
            extra_context={
                "package_manager": "uv",
                "execute_package_manager_in_docker": True,
            },
            output_dir=str(tmp_path),
        )
    )

    # Ensure the project directory was created
    assert project_dir.exists()
    assert project_dir.name == PROJECT_NAME
    assert project_dir == Path(tmp_path).joinpath(PROJECT_NAME)

    # Ensure expected files exist
    assert_file_exists(project_dir, UV_FILE_NAMES)

    # Ensure the 'Dockerfile' is the right one
    dockerfile: Path = project_dir.joinpath("Dockerfile")
    assert_file_contains(dockerfile, "UV_COMPILE_BYTECODE=1")
    assert_file_contains(dockerfile, "--uid $USER_ID")

    # Ensure the 'Makefile' is the right one
    makefile: Path = project_dir.joinpath("Makefile")
    assert_file_contains(makefile, "UV ?= $(DOCKER_DEV) uv")

