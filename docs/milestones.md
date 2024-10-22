# [ [M0] Milestone 0: Modelado del problema](https://github.com/lmchaves/OrganizarTaller/milestone/4)
- Definir el dominio del problema centrado en las Historias de Usuario HU1 y HU2. Se desarrollará un modelo inicial que represente las entidades clave involucradas y las interacciones entre ellas, como la gestión del inventario, disponibilidad de piezas y transporte entre sedes.
- __Entregable__:
    - Código que implemente las entidades principales relacionadas con las HU1 y HU2, incluyendo: Piezas, Inventario, Sedes y Transporte.
    - El código debe mostrar las relaciones entre estas entidades, como la interacción entre inventario y sedes, el flujo de piezas entre sedes, y cómo los tiempos de transporte afectan la disponibilidad.

- __Viabilidad__:
Se considerará completado cuando el código refleje correctamente las interacciones del dominio descrito en las HU1 y HU2.

# [ [M1] Milestone 1: Implementación de la consulta de disponibilidad de piezas](https://github.com/lmchaves/OrganizarTaller/milestone/2)
- Implementar la funcionalidad que permita a Javier, el mecánico, consultar la disponibilidad de las piezas en el sistema. La información incluirá si la pieza está disponible en el taller local o si debe solicitarse desde otra sede, junto con tiempos estimados de entrega.

- __Entregable__:
    - Código con la funcionalidad de consulta de inventario para el mecánico.
- __Viabilidad__:
Se considerará completado cuando Javier pueda realizar consultas de piezas, recibir tiempos estimados de entrega, y los tests automáticos validen la funcionalidad implementada.

# [ [M2] Milestone 2:  Implementación de pedidos de piezas](https://github.com/lmchaves/OrganizarTaller/milestone/3)
- Implementar la lógica que permita gestionar las solicitudes de piezas entre las diferentes sedes, priorizando los factores de costos de transporte, tiempos estimados de entrega y la urgencia de las reparaciones.

- __Entregable__:
    - Algoritmo de optimización que seleccione la mejor sede para enviar la pieza, teniendo en cuenta los criterios de costos, tiempos de entrega y la prioridad de la reparación.
    - Código de priorización que permita identificar las reparaciones más urgentes y asignar recursos de manera eficiente.

- __Viabilidad__:
Se considerará completado cuando el algoritmo de optimización asigne correctamente las piezas entre sedes, respetando los criterios de costos, tiempos y prioridades. 

