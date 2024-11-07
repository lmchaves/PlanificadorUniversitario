# [ [M0] Milestone 0: Modelado del problema](https://github.com/lmchaves/OrganizarTaller/milestone/4)
- Realizar un análisis de la [HU1](https://github.com/lmchaves/OrganizarTaller/issues/5) para identificar y definir los elementos clave del dominio relacionados con la supervisión y gestión del inventario de piezas en el taller. 
- __Entregable__:
    - Código que encapsule los elementos fundamentales del dominio, permitiendo la interacción entre entidades como pueden ser Piezas, Inventario, Sedes y los procesos de control de disponibilidad.
- __Viabilidad__:
El código debe seguir buenas prácticas de diseño y programación, asegurando que se puedan realizar ajustes futuros para incorporar cambios en los requisitos del negocio.
Se considera validado mediante pruebas con conjuntos de datos de prueba, asegurando una gestión correcta de las piezas.


# [ [M1] Milestone 1: Optimización de pedidos](https://github.com/lmchaves/OrganizarTaller/milestone/3)
- Este hito tiene como objetivo optimizar el proceso de solicitud de piezas entre sedes, asegurando una distribución eficiente y oportuna.El sistema debe ser capaz de evaluar de manera automática la mejor sede desde la cual obtener las piezas necesarias, tomando en cuenta criterios clave explicados en [HU2](https://github.com/lmchaves/OrganizarTaller/issues/5) (costos de transporte, los tiempos de entrega y la disponibilidad en inventarios).

- __Entregable__:
    - Algoritmo de optimización que seleccione la mejor sede para pedir la pieza necesaria, teniendo en cuenta los criterios de costos de transportes entre sedes, tiempos de entrega en  función de la disponibilidad de inventario.

- __Viabilidad__:
Este hito se considerará completado cuando se demuestre que el algoritmo reduce de manera efectiva los tiempos y el costo promedio de entrega de piezas. Para ello, se compararán estos indicadores antes y después de la implementación del algoritmo, verificando que haya mejoras en ambos aspectos.


