## Criterios de evaluación

Se han considerado los siguientes criterios, para las diferentes herramientas que llevan a cabo las diferentes funcionalidades para los tests:

1. **Herramientas activas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas. Para ello se consulta en los repositorios oficiales de las herramientas, como [Pytest](https://github.com/pytest-dev/pytest), [Nose2](https://github.com/nose-devs/nose2), y [Testify](https://github.com/Yelp/Testify), donde se puede verificar la frecuencia de commits y actualizaciones recientes.

2. **Biblioteca de aserciones**: La herramienta debe incluir una biblioteca que permita verificar condiciones esperadas de los tests mediante métodos simples y legibles, proporcionando mensajes detallados en caso de fallo para facilitar la depuración.
3. 
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


## Conclusión

Según los criterios establecidos, Pytest es la opción más adecuada debido a su mantenimiento activo, facilidad de uso y una biblioteca de aserciones integrada que simplifica la escritura y comprensión de los tests. Unittest sigue siendo una herramienta estándar confiable, aunque con una curva de aprendizaje más pronunciada. Nose2 y Testify ofrecen flexibilidad y extensibilidad, pero su menor nivel de actualización y soporte los hacen menos recomendables.

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

### [PyHamcrest](https://github.com/hamcrest/PyHamcrest)

Una biblioteca de aserciones más expresiva que permite escribir condiciones como `assert_that(actual, equal_to(expected))`. Se encuentra activamente mantenida, con actualizaciones periódicas en su repositorio oficial.

### [Ensure](https://pypi.org/project/ensure/)

Es una biblioreca de aserciones que proporciona verificaciones claras y específicas para validar condiciones esperadas, con un enfoque en la legibilidad y simplicidad. Soporta expresiones como `ensure.equal(actual, expected)` y se centra en una sintaxis intuitiva. Su mantenimiento activo y desarrollo reciente la hacen una opción confiable para integrarse en proyectos actuales.

## Conclusión

Pytest destaca por su simplicidad, mensajes automáticos detallados y mantenimiento activo. Ensure tiene una sintaxis explícita, mientras que Unittest permanece sólido para pruebas formales. PyHamcrest y Testify son útiles para expresiones avanzadas, pero menos intuitivos. Nose2 resulta menos práctico por su dependencia de bibliotecas externas.

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


