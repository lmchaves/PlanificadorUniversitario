# [M0] Milestone 0: Modelado del problema
- __Objetivo__ : Crear un modelo que represente los elementos del dominio del problema, reflejando la estructura del taller automotriz y los procesos de gestión logística.
Este modelo debe definir claramente las clases que intervienen en el sistema, como Piezas, Inventario, Reparaciones, Sedes, Transporte, y Clientes. Cada clase deberá incluir sus características relevantes y los comportamientos necesarios.
- __Entregable__:
    - Código que refleje los elementos del dominio, incluyendo clases para Piezas, Inventario, Reparaciones, Sedes, Transporte, Clientes y cualquier otra clase necesaria.
    - El código también debe reflejar las relaciones entre estos elementos, como la interacción entre inventario y sedes, el flujo de piezas entre diferentes localidades, y cómo los tiempos de entrega y costos afectan la distribución de piezas.

- __Viabilidad__:
Se considerará completado cuando el modelado en código esté validado y represente correctamente las interacciones del dominio, y cuando los elementos estén listos para
ser utilizados en la implementación de la lógica de negocio.

# [M1] Milestone 1: Implementación de la consulta de disponibilidad de piezas
- __Objetivo__:
Implementar la funcionalidad que permita a Javier, el mecánico, consultar la disponibilidad de las piezas en el sistema en tiempo real. La información incluirá si la pieza está disponible en el taller local o si debe solicitarse desde otra sede, junto con tiempos estimados de entrega.

- __Entregable__:

Código con la funcionalidad de consulta de inventario para el mecánico.
Sistema que ofrezca información sobre la disponibilidad de las piezas y tiempos de entrega.
- __Viabilidad__:
Se considerará completado cuando Javier pueda realizar consultas de piezas, recibir tiempos estimados de entrega, y los tests automáticos validen la funcionalidad implementada.

