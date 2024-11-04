# [ [M0] Milestone 0: Modelado del problema](https://github.com/lmchaves/OrganizarTaller/milestone/4)
- Hay que realizar un análisis de las historias de usuario, en concreto de las historias de usuario [HU1](https://github.com/lmchaves/OrganizarTaller/issues/4) y [HU2](https://github.com/lmchaves/OrganizarTaller/issues/5), para identificar y definir los problemas clave. Este análisis establecerá las bases para la creación de un modelo que represente los procesos y desafíos implicados en la gestión del inventario, la distribución de piezas y la atención al cliente. El objetivo es generar un marco que sirva de base sólida para el desarrollo futuro.
- __Entregable__:
    - Código que encapsule los elementos fundamentales del dominio, permitiendo la interacción entre entidades como pueden ser Piezas, Inventario, Sedes y Clientes, además de las relaciones necesarias para la gestión de la disponibilidad de piezas.
- __Viabilidad__:
El código debe seguir buenas prácticas de diseño y programación, asegurando que se puedan realizar ajustes futuros para incorporar cambios en los requisitos del negocio.
Se considera validado cuando el modelo de código refleje correctamente los elementos del dominio y las interacciones necesarias, permitiendo así un desarrollo efectivo en los siguientes hitos.

# [ [M1] Milestone 1: Optimización de pedidos y priorización de reparaciones](https://github.com/lmchaves/OrganizarTaller/milestone/3)
- Este hito se basa en la historia de usuario  [HU2](https://github.com/lmchaves/OrganizarTaller/issues/5) y  [HU3](https://github.com/lmchaves/OrganizarTaller/issues/6) busca implementar la lógica que permita gestionar las solicitudes de piezas entre las diferentes sedes, priorizando los factores de costos de transporte, tiempos estimados de entrega y la urgencia de las reparaciones.

- __Entregable__:
    - Algoritmo de optimización que seleccione la mejor sede para pedir la pieza necesaria, teniendo en cuenta los criterios de costos, tiempos de entrega.
    - Código de priorización que permita identificar las reparaciones más urgentes y asignar recursos de manera eficiente.

- __Viabilidad__:
Se considerará completado cuando el algoritmo de optimización asigne correctamente las piezas entre sedes, respetando los criterios de costos, tiempos y prioridades. 


# [ [M2] Milestone 2: Implementación de la consulta de disponibilidad de piezas](https://github.com/lmchaves/OrganizarTaller/milestone/2)
- Este hito se alinea con la historia de usuario [HU1](https://github.com/lmchaves/OrganizarTaller/issues/4) , busca desarrollar una funcionalidad que permita a Javier, el mecánico, consultar la disponibilidad de piezas en el sistema. Esta consulta debe incluir información sobre si las piezas están disponibles en el taller local y, en caso de no estarlo, proporcionar tiempos estimados de entrega desde otras sedes. Se busca que esta funcionalidad sea intuitiva y útil para la atención al cliente, ayudando a Javier a informar de manera precisa y rápida sobre las reparaciones necesarias.

- __Entregable__:
    - Código que facilite la consulta de disponibilidad de piezas, asegurando que se muestren los datos relevantes sobre el inventario y tiempos de entrega estimados.
La funcionalidad será validada mediante pruebas que aseguren que Javier puede realizar consultas de piezas y recibir información precisa sobre disponibilidad y tiempos de entrega, contribuyendo a una mejor atención al cliente.


