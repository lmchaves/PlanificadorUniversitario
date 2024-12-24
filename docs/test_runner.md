# Herramienta para tests

## Criterios de evaluación

Para seleccionar la herramietna para tests, se han considerado los siguientes criterios:


1. **Herramientas activas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas.

2. **Biblioteca de aserciones**: la herramienta debe incluir una biblioteca adecuada para verificar condiciones esperadas en los tests de manera clara y legible.


## Pytest

Permite ejecutar tests de forma automatizada mediante el comando **pytest**, es activamente mantenido y cuenta con una comunidad extensa, lo que asegura la resolución rápida de problemas (permitiendo tener muchos recursos).

Pytest utiliza una biblioteca de aserciones nativa que permite escribir afirmaciones simples como `assert actual == expected`. Esta biblioteca genera automáticamente mensajes detallados en caso de fallos, lo que facilita la depuración y comprensión de errores.

**Ejecución desde CLI:**  
Pytest se ejecuta con el comando `pytest` para correr todos los tests o `pytest ruta/test_función.py::test_nombre` para tests específicos.


## Unittest

Unittest es el framework de pruebas estándar incluido en Python, ejecuta los tests automatizada, directamente desde el estándar de Python **python -m unittest**, organiza los tests en clases, métodos y módulos. Tiene una curva de aprendizaje más pronunciada que Pytest, adecuado para proyectos que priorizan el uso de herramientas estándar.

Unittest incluye una biblioteca integrada que proporciona métodos como `self.assertEqual(actual, expected)` o `self.assertTrue(condition)` para comparaciones detalladas y expresivas. Esto lo hace útil para pruebas más estructuradas y específicas.

**Ejecución desde CLI:**  
Se utiliza el comando `python -m unittest` para ejecutar todos los tests, o `python -m unittest ruta.TestClase.test_nombre` para casos concretos.



## Nose2

Nose2 es la evolución de Nose, una herramienta de testing para Python, diseñada para ser más moderna y compatible con los estándares actuales. 
Nose2 permite ejecutar pruebas de forma automatizada mediante el comando **nose2**. Compatible con las bibliotecas de aserciones estándar, como las de Unittest, y permite extender funcionalidades mediante plugins.
Sin embargo, su comunidad y soporte son más limitados en comparación con Pytest.

Nose2 no tiene su propia biblioteca de aserciones, pero es compatible con las bibliotecas estándar de Python como las de Unittest. Esto permite escribir pruebas utilizando métodos como `self.assertEqual` o incluso el operador `assert`.

**Ejecución desde CLI:**  
Los tests se corren con el comando `nose2` para todos los casos o especificando rutas concretas como `nose2 ruta.TestClase.test_nombre`.




Según los criterios establecidos, Pytest es la opción más adecuada, aunque Unittest es una herramienta estándar y ampliamente usada, Pytest es preferido debido a su mantenimiento activo, 
amplia comunidad,permitiendo simplificar la escritura y comprensión de los tests. Nose2, aunque versátil, cuenta con menor soporte y comunidad en comparación.
