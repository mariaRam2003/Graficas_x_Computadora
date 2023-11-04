# Instrucciones de uso - Código de Renderización 3D con Pygame

Este código utiliza Pygame para renderizar un modelo 3D en tiempo real. Puedes interactuar con el modelo y los shaders utilizando las siguientes teclas y comandos:

## Teclas de Control:

- `K_RIGHT`: Mueve el color de fondo hacia la derecha.
- `K_LEFT`: Mueve el color de fondo hacia la izquierda.
- `K_UP`: Mueve el color de fondo hacia arriba.
- `K_DOWN`: Mueve el color de fondo hacia abajo.
- `K_SPACE`: Cambia el componente azul del color de fondo hacia arriba.
- `K_LSHIFT`: Cambia el componente azul del color de fondo hacia abajo.

## Teclas de Modelo 3D:

- `K_d`: Rota el modelo hacia la derecha.
- `K_a`: Rota el modelo hacia la izquierda.
- `K_w`: Rota el modelo hacia arriba.
- `K_s`: Rota el modelo hacia abajo.
- `K_p` o `K_KP_PLUS`: Aumenta el zoom en un 1%.
- `K_MINUS` o `K_KP_MINUS`: Reduce el zoom en un 1%.

## Teclas de Control de Shaders:

- `K_c`: Muestra la lista de comandos disponibles.
- `K_r`: Restablece los shaders a los originales.
- `K_1`: Aplica el shader "Gourad Fragment".
- `K_2`: Aplica el shader "Multicolor Fragment".
- `K_3`: Aplica el shader "Noise Fragment".
- `K_4`: Aplica el shader "Metal Fragment".

## Otros Comandos:

- `ESC`: Sale de la aplicación.
- `Cualquier otra tecla`: No tiene ninguna acción asignada.

## Notas adicionales:

- El modelo 3D se carga desde un archivo "Estatua.obj" y se le aplica una textura y una textura de ruido.
- El código renderiza el modelo 3D en tiempo real y muestra el resultado en una ventana de Pygame.

## Como se ve:
![pygame-window-2023-11-03-23-03-22](https://github.com/mariaRam2003/Graficas_x_Computadora/assets/83832445/5dd4db23-9f25-41b7-9f38-c1d66403593d)


