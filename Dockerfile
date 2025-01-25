FROM python:alpine

RUN apk add --no-cache \
    make

RUN adduser -D -h /home/userTest userTest

RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache && \
    mkdir -p /home/userTest/.venv && \
    chmod -R a+w /home/userTest/.venv 

# Configurar PATH para pipx y Python
ENV PATH="/home/userTest/.local/bin:$PATH"
ENV PIPX_BIN_DIR="/home/userTest/.local/bin"
ENV PIPX_HOME="/home/userTest/.local/pipx"

USER userTest

RUN python3 -m pip install --user pipx && \
    pipx install uv

ENV UV_CACHE_DIR=/home/userTest/.cache/uv
ENV UV_PROJECT_ENVIRONMENT=/home/userTest/.venv

WORKDIR /app/test

CMD ["make", "test"]
