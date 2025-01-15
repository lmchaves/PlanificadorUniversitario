FROM python:3.13-alpine

RUN apk add --no-cache make \
    && pip install pdm

RUN adduser -D -h /home/userTest userTest

USER userTest

WORKDIR /app/test

RUN mkdir -p /home/userTest/.cache/pdm && \
    chmod -R a+w /home/userTest/.cache/pdm

ENV PDM_CACHE_DIR=/home/userTest/.cache/pdm

ENTRYPOINT ["pdm", "run", "make", "test"]
