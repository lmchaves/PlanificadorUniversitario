# Herramientas para Testing

## Criterios de evaluación

Para seleccionar la herramienta para tests, se han considerado los siguientes criterios:

1. **Herramientas activas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas.

2. **Biblioteca de aserciones**: La herramienta debe incluir una biblioteca que permita verificar condiciones esperadas de los tests mediante métodos simples y legibles, proporcionando mensajes detallados en caso de fallo para facilitar la depuración.

3. **Facilidad de ejecución desde CLI:** Capacidad para ejecutar pruebas fácilmente desde la línea de comandos, permitiendo ejecutar todos los tests o casos específicos.

---

## Test Runners

### [Pytest](https://github.com/pytest-dev/pytest)

Permite ejecutar tests de forma automatizada mediante el comando **pytest**, es activamente mantenido y cuenta con una comunidad extensa, lo que asegura la resolución rápida de problemas (permitiendo tener muchos recursos, aquí está la [documentación](https://docs.pytest.org/en/stable/)).

### Unittest

Unittest es el framework de pruebas estándar incluido en Python. Ejecuta los tests de forma automatizada directamente desde el estándar de Python **python -m unittest**, organiza los tests en clases, métodos y módulos. Tiene una curva de aprendizaje más pronunciada que Pytest, adecuado para proyectos que priorizan el uso de herramientas estándar (aquí está la [documentación](https://docs.python.org/3/library/unittest.html)).

### [Nose2](https://github.com/nose-devs/nose2)

Nose2 es la evolución de Nose, una herramienta de testing para Python, diseñada para ser más moderna y compatible con los estándares actuales. Nose2 permite ejecutar pruebas de forma automatizada mediante el comando **nose2**. Compatible con las bibliotecas de aserciones estándar, como las de Unittest, y permite extender funcionalidades mediante plugins. Sin embargo, su comunidad y soporte son más limitados en comparación con Pytest.

### [Testify](https://github.com/Yelp/Testify)

Testify es un test runner robusto, diseñado como una alternativa a Unittest. Proporciona una estructura clara para organizar tests y ofrece funcionalidades avanzadas como hooks para configurar y limpiar entornos. Aunque es menos popular que Pytest, es utilizado en proyectos que requieren flexibilidad adicional en sus pruebas.

---

## Bibliotecas de Aserciones

### [Pytest](https://github.com/pytest-dev/pytest)

Pytest utiliza una biblioteca de aserciones nativa que permite escribir afirmaciones simples como `assert actual == expected`. Esta biblioteca genera automáticamente mensajes detallados en caso de fallos, lo que facilita la depuración y comprensión de errores.

### Unittest

Unittest incluye una biblioteca integrada que proporciona métodos como `self.assertEqual(actual, expected)` o `self.assertTrue(condition)` para comparaciones detalladas y expresivas. Esto lo hace útil para pruebas más estructuradas y específicas.

### [Nose2](https://github.com/nose-devs/nose2)

Nose2 no tiene su propia biblioteca de aserciones, pero es compatible con las bibliotecas estándar de Python como las de Unittest. Esto permite escribir pruebas utilizando métodos como `self.assertEqual` o incluso el operador `assert`.

### [Testify](https://github.com/Yelp/Testify)

Testify incluye su propia biblioteca de aserciones, que ofrece métodos como `assert_equal(actual, expected)` y `assert_raises(exception, func)`. Estas aserciones son expresivas y útiles para depurar, con mensajes claros en caso de fallos.

### [Hamcrest](https://github.com/hamcrest/PyHamcrest)

Una biblioteca de aserciones más expresiva que permite escribir condiciones como `assert_that(actual, equal_to(expected))`.

---

## Herramientas CLI

### [Pytest](https://github.com/pytest-dev/pytest)

- Pytest se ejecuta con el comando `pytest` para correr todos los tests o `pytest ruta/test_función.py::test_nombre` para tests específicos.

### Unittest

- Se utiliza el comando `python -m unittest` para ejecutar todos los tests, o `python -m unittest ruta.TestClase.test_nombre` para casos concretos.

### [Nose2](https://github.com/nose-devs/nose2)

- Los tests se corren con el comando `nose2` para todos los casos o especificando rutas concretas como `nose2 ruta.TestClase.test_nombre`.

### [Testify](https://github.com/Yelp/Testify)

- Los tests se ejecutan con el comando `testify` para todos los casos o especificando tests específicos mediante `testify ruta.TestClase.test_nombre`.

---

## Conclusión

Según los criterios establecidos, Pytest es la opción más adecuada. Aunque Unittest es una herramienta estándar y ampliamente usada, Pytest es preferido debido a su mantenimiento activo, amplia comunidad y capacidad para simplificar la escritura y comprensión de los tests. Nose2 y Testify, aunque versátiles, cuentan con menor soporte y comunidad en comparación.
