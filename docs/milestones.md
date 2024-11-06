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
El hito se considerará completado cuando el algoritmo de optimización asigne correctamente las piezas solicitadas a la sede adecuada, reduciendo los costos y tiempos de manera efectiva.

# [ [M2] Milestone 2: Priorización de reparaciones según urgencia](https://github.com/lmchaves/OrganizarTaller/milestone/3)
- Basándose en el sistema ya creado para gestionar y optimizar los pedidos de piezas entre las sedes, se implementarán características adicionales para priorizar las reparaciones en función de la urgencia del cliente de forma que se resuelva el problema mencionado en la HU3 [HU3](https://github.com/lmchaves/OrganizarTaller/issues/6).

- __Entregable__:
    - Código de priorización que permita identificar las reparaciones más urgentes y asignar recursos de manera eficiente. 

- __Viabilidad__:
El código se considerará validado cuando se compruebe que prioriza las reparaciones según la urgencia del cliente, optimizando la asignación de recursos en función de la disponibilidad de piezas y tiempos de entrega estimados.

