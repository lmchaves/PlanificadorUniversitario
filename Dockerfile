FROM python:alpine

RUN apk add --no-cache \
    make \
    curl \
    && pip install pdm

WORKDIR /app/test  

RUN adduser -D -h /home/userTest userTest


RUN mkdir -p /home/userTest/.cache/pdm && \
    chmod -R a+w /home/userTest/.cache/pdm && \
    mkdir -p /home/userTest/.pdm-venvs && \
    chmod -R a+w /home/userTest/.pdm-venvs

USER userTest

ENV PDM_CACHE_DIR=/home/userTest/.cache/pdm
ENV PDM_VENV_LOCATION=/home/userTest/.pdm-venvs


ENTRYPOINT ["make", "test"]
