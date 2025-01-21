FROM python:alpine

RUN apk add --no-cache \
    make \
    curl\   
    bash 


RUN adduser -D -h /home/userTest userTest

RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache && \
    mkdir -p /home/userTest/.venv && \
    chmod -R a+w /home/userTest/.venv 


ENV PATH="/home/userTest/.local/bin:$PATH"

USER userTest

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/userTest/.cache/uv
ENV UV_PROJECT_ENVIRONMENT=/home/userTest/.venv

WORKDIR /app/test

CMD ["make", "test"]
