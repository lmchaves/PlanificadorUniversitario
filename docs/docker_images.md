# Imagenes para el contenedor

## Criterios de evaluación

Para seleccionar el gestor de dependencias más adecuado para este proyecto, se han considerado los siguientes criterios:


1. **Imágenes mantenidas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas.

2. Tambien se va a tener en cuenta el peso de las imágenes.


## [Ubuntu](https://hub.docker.com/_/ubuntu)
Está activamente mantenida con actualizaciones y versiones recientes, tiene un peso de 29MB (con alguans versiones mas ligeras pero debes configurar más cosas manualmente), es una buena eleción para tener el sistema como base y ya ir añdiendo las herramientas necesarias.

## [Debian](https://hub.docker.com/_/debian)
La última actualización fue de hace un par de semanas, por lo que esta activamente mantenido. En cuanto al peso varia dependiendo de la version que escojas, tenemos la base con un peso muy parecido a ubuntu, pero luego tenemos varias opciones slim: debian:bullseye-slim, debian:bookworm-slim, stable-slim con un peso aproximado de 22MB.

## [Alpine](https://hub.docker.com/_/alpine)
La última actualización fue de hace unos días, siendo una herramieta activa y mantenida, con un peso mucho menor al de las anteriores, de tan slo 5MB, sin funcionalides extra siendo mínima y eficiente.

## [Python](https://hub.docker.com/_/python)
Ya que estoy utilizando python, tenemos que ver esta opción en la que ya nos viene instalado python, pero hay diversas opciones, de las ya comentadas anteriormente como Alpine(muy ligera), debian:bookworm-slim (aproxiamdamente 150MB demasiado pesada), python:bullseye-slim (aproximadamente 52 MB mejor apoción que la anterior). Con la última acutalzición de días, por lo que esta mantenida.

## [frostming/pdm](https://hub.docker.com/r/frostming/pdm)

Esta es la imagen de frostming creador de pdm, la cual utiliza Debian slim como base, la cual tiene instalado tanto Python como PDM y pesa 80MB. Pero el principal problema es que su última actualización fue hace 3 años.

## Conlusión

Hay varias opciones para elegir una imagen base para el proyecto. Las imágenes como Ubuntu, Debian o Alpine solo incluyen el sistema operativo, y todas están activamente mantenidas. Alpine destaca por ser la más ligera, pero presenta el inconveniente de que debemos instalar Python y sus dependencias adicionales, lo que puede aumentar el tiempo de construcción y el tamaño final.

Dentro de las imágenes que ya incluyen Python, tenemos opciones como la imagen frostming/pdm, que viene con PDM preinstalado. Sin embargo, esta imagen no está activamente mantenida, ya que no ha recibido actualizaciones en los últimos tres años. Debido a esto, me decantaré por la imagen oficial de Python sobre Alpine, ya que proporciona un mantenimiento activo y la inclusión de Python sin necesidad de instalaciones adicionales.
