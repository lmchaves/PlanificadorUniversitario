# Gestor de tareas

## Criterios de evaluación
Para elegir el gestor de tareas más adecuado, se han considerado los siguientes criterios:

1. **Facilidad de uso y configuración:** Herramientas sencillas de instalar y configurar, con una curva de aprendizaje accesible.
2. **Compatibilidad con el lenguaje del proyecto:** Preferencia por herramientas integradas nativamente con Python o independientes del lenguaje.
3. **Capacidades específicas:** Funcionalidades como ejecución remota, definición de tareas complejas o soporte para múltiples entornos.
4. **Comunidad y documentación:** Recursos disponibles para resolver problemas y aprender a utilizar la herramienta.
5. **Escalabilidad y aplicabilidad a largo plazo:** Adecuación para proyectos de diferentes tamaños y lenguajes, con posibilidad de expansión futura.
6. **Complejidad añadida:** Se penalizan herramientas que introducen más complejidad de la necesaria para el proyecto.



## Invoke

Es basada en Python (inspirado en ruby Rake), por lo que se pueden escribir las tareas utilizando Python, proporcionando una mayor integración en el código del proyecto.
Permite ejecutar comandos de shell y definir/organizar funciones de tareas desde un archivo tasks.py. 

## Paramiko

Paramiko es una librería Python que proporciona una implementación del protocolo SSH. Permite la ejecución remota de comandos en sistemas a través de SSH y la transferencia se gura de archivos. Su uso esta orientado en aplicaciones que requieren interacciones seguras entre máquinas. Pero, al estar diseñado principalmente para la ejecución de tareas en entornos remotos, agrega una complejidad adicional innecesaria

## Fabric

Fabric (basada en Paramiko) es una herramienta basada en Python para ejecutar comandos de shell de manera remota a través de SSH. Permite automatizar tareas en servidores y despliegues, extendiendo las funcionalidades de Invoke y Paramiko. Es una muy buena opción para gestionar tareas distribuidas en entornos remotos.Sin embargo, al igual que Paramiko, tiene una complejidad adicional innecesaria.


## Make

Make es una herramienta de automatización de tareas que no está limitada a un solo lenguaje de programación, por lo que puede ser utilizada en proyectos escritos en cualquier lenguaje, con una comunidad activa y una documentación extensa (muchos recursos). Solo es necesario crear un archivo específico (Makefile) para definir las tareas a ejecutar.

## Rake

Rake está orientado principalmente a proyectos escritos en Ruby, lo que limita su utilidad para proyectos en Python y otros lenguajes. Aunque tiene una buena integración con Ruby, su comunidad y documentación son más pequeñas en comparación con Make, que tiene un soporte más amplio y recursos más accesibles.   

 
## Just 

Just es una herramienta de automatización de tareas que permite definir comandos de manera sencilla a través de un archivo justfile, similar a Make, Just es más fácil de escribir y entender (lenguaje más "cotidiano" ).  Es independiente del lenguaje de programación, lo que permite integrarlo en proyectos de Python y otros lenguajes sin problema. Make  tiene una comunidad más grande, lo que se traduce en más recursos, tutoriales y una mejor documentación, lo que facilita su adopción y resolución de problemas.

Invoke es ideal para proyectos centrados exclusivamente en Python, pero Make te permite gestionar tareas en cualquier lenguaje, lo que lo hace más adecuado a largo plazo.

