## Criterios de evaluación

Se han considerado los siguientes criterios, para las diferentes herramientas que llevan a cabo las diferentes funcionalidades para los tests:

1. **Herramientas activas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas. Para ello se consulta en los repositorios oficiales de las herramientas, como [Pytest](https://github.com/pytest-dev/pytest), [Nose2](https://github.com/nose-devs/nose2), donde se puede verificar la frecuencia de commits y actualizaciones recientes.

2. **Funcionalidades integradas**: Se valoran las herramientas que minimizan la necesidad de instalar dependencias adicionales cuando las funcionalidades nativas cumplen con los requisitos del proyecto. Esto simplifica la configuración y reduce la complejidad del entorno. (Es preferible que las herramientas permitan personalizar los mensajes de error en las aserciones o que proporcionen mnsajes predeterminados claros y útiles para la identificación de errores)

---

## Test Runners

### [Pytest](https://github.com/pytest-dev/pytest)

Permite ejecutar tests de forma automatizada mediante el comando **pytest**, es activamente mantenido y cuenta con una comunidad extensa, lo que asegura la resolución rápida de problemas (permitiendo tener muchos recursos, aquí está la [documentación](https://docs.pytest.org/en/stable/)).

### Unittest

Unittest es el framework de pruebas estándar incluido en Python. Ejecuta los tests de forma automatizada directamente desde el estándar de Python **python -m unittest**, organiza los tests en clases, métodos y módulos. Tiene una curva de aprendizaje más pronunciada que Pytest, adecuado para proyectos que priorizan el uso de herramientas estándar (aquí está la [documentación](https://docs.python.org/3/library/unittest.html)).

### [Nose2](https://github.com/nose-devs/nose2)

Nose2 es la evolución de Nose, una herramienta de testing para Python, diseñada para ser más moderna y compatible con los estándares actuales. Nose2 permite ejecutar pruebas de forma automatizada mediante el comando **nose2**. Compatible con las bibliotecas de aserciones estándar, como las de Unittest, y permite extender funcionalidades mediante plugins. Sin embargo, su comunidad y soporte son más limitados en comparación con Pytest.




## Conclusión

Según los criterios establecidos, **Pytest** es la opción más adecuada debido a su mantenimiento activo, y sus funcionalidades integradas que simplifican la configuración y ejecución de pruebas sin requerir muchas dependencias externas. Unittest sigue siendo una herramienta estándar confiable así que tambien se puede usar en algunas ocasiones (se puede combinar con pytest). Nose2  introducen un nivel de complejidad innecesario debido a su menor comunidad de soporte (y actualizaciones) y su dependencia de configuraciones adicionales.

---

## Bibliotecas de Aserciones

### Unittest

Unittest incluye una biblioteca integrada que proporciona métodos como `self.assertEqual(actual, expected)` o `self.assertTrue(condition)` para comparaciones detalladas y expresivas. Esto lo hace útil para pruebas más estructuradas y específicas.

### [PyHamcrest](https://github.com/hamcrest/PyHamcrest)

Una biblioteca de aserciones más expresiva que permite escribir condiciones como `assert_that(actual, equal_to(expected))`. Se encuentra activamente mantenida, con actualizaciones periódicas en su repositorio oficial.

### [Ensure](https://pypi.org/project/ensure/)

Es una biblioreca de aserciones que proporciona verificaciones claras y específicas para validar condiciones esperadas, con un enfoque en la legibilidad y simplicidad. Soporta expresiones como `ensure.equal(actual, expected)` y se centra en una sintaxis intuitiva. Su mantenimiento activo y desarrollo reciente la hacen una opción confiable para integrarse en proyectos actuales.

## Conclusión

Unittest sigue siendo una opción sólida gracias a su biblioteca integrada y confiable. Ensure tiene una sintaxis explícita, PyHamcrest es útil para expresiones avanzadas, pero menos intuitivos (pueden añadir complejidad innecesaria, ya que su sintaxis más elaborada). 
Por lo tanto, combinar **Unittest** con herramientas como Pytest puede ser la mejor estrategia para aprovechar lo mejor de ambas: la estructura estándar de Unittest y los mensajes automáticos mejorados de Pytest.

---

## Herramientas CLI

### [Pytest](https://github.com/pytest-dev/pytest)

- Pytest se ejecuta con el comando `pytest` para correr todos los tests o `pytest ruta/test_función.py::test_nombre` para tests específicos.


### [Nose2](https://github.com/nose-devs/nose2)

- Los tests se corren con el comando `nose2` para todos los casos o especificando rutas concretas como `nose2 ruta.TestClase.test_nombre`.


## Conclusión

Pytest sobresale al generar mensajes claros y fáciles de interpretar que ayudan a solucionar problemas rápidamente. Nose2 también ofrecen mensajes útiles, aunque requieren comandos más específicos. 

---


