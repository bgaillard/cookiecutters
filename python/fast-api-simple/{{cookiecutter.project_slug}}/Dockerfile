# @see https://github.com/orgs/python-poetry/discussions/1879#discussioncomment-216865

ARG POETRY_VERSION=2.1.2
ARG PYTHON_VERSION=3.13

ARG USER=jdoe
ARG GROUP=jdoe


# `python-base` sets up all our shared environment variables
FROM python:${PYTHON_VERSION}-slim as python-base

ARG GROUP
ARG GROUP_ID

ARG USER
ARG USER_ID

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    #
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    XDG_DATA_HOME=/home/$USER/.local/share


ENV VIRTUAL_ENV=/app/.venv \
    PATH="/home/$USER/.local/bin:/app/.venv/bin:$PATH"

# https://vsupalov.com/docker-shared-permissions/
RUN addgroup --gid $GROUP_ID $GROUP
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER


########################################################################################################################
# POETRY BUILDER
########################################################################################################################
FROM python-base as builder-base

ARG USER

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

USER $USER
RUN curl -sSL https://install.python-poetry.org | python


########################################################################################################################
# DEV
########################################################################################################################
FROM python-base as dev

ARG GROUP
ARG USER

COPY --chown=$USER:$GROUP --from=builder-base /home/$USER/.local/bin/poetry /home/$USER/.local/bin/poetry
COPY --chown=$USER:$GROUP --from=builder-base /home/$USER/.local/share /home/$USER/.local/share

RUN mkdir -p /app
RUN chown -R $USER:$GROUP /app

COPY --chown=$USER:$GROUP poetry.lock pyproject.toml /app/

USER $USER
WORKDIR /app

RUN /home/$USER/.local/bin/poetry install --no-root --with dev --with test

# Install Pyright using pyright-python, it will automatically install Node.js and pyright
RUN echo "print('ok')" > /tmp/a.py && poetry run pyright /tmp/a.py && rm /tmp/a.py

CMD ["python", "-m", "app.main"]


########################################################################################################################
# PROD
########################################################################################################################
FROM builder-base as builder-prod

ARG GROUP
ARG USER

USER $USER
WORKDIR /app
COPY --chown=$USER:$GROUP poetry.lock pyproject.toml ./
RUN /home/$USER/.local/bin/poetry install --no-root


FROM python-base as prod

ARG GROUP
ARG USER

COPY --chown=$USER:$GROUP --from=builder-prod /home/$USER/.bash_logout /home/$USER/.bash_logout
COPY --chown=$USER:$GROUP --from=builder-prod /home/$USER/.bashrc /home/$USER/.bashrc
COPY --chown=$USER:$GROUP --from=builder-prod /home/$USER/.profile /home/$USER/.profile
COPY --chown=$USER:$GROUP --from=builder-prod /app /app
COPY --chown=$USER:$GROUP ./app /app/app

USER $USER
WORKDIR /app

CMD ["gunicorn", "--bind=0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
