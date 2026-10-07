# Sistema de Biblioteca Universitaria

## Datos del equipo

**Número de equipo:** 7

**Integrantes:**

1. Pedro Alexander Henriquez Guzman
2. Brayan Adonay Peñate Alas
3. Jared Emanuel Marin Rodriguez
4. Eduard Francisco Peraza Guardado
5. Wendy Zelena Peraza Guevara
6. Cesar Oliver Salazar Mejia

**Escenario seleccionado:** Biblioteca (nivel básico)

## Descripción de la solución

El proyecto representa los materiales que una biblioteca universitaria presta a sus usuarios: **libros** y **revistas**. En Python se modelan con clases (herencia, sobrescritura y polimorfismo). En el frontend, una página web muestra el catálogo en tarjetas y permite seleccionar un material para préstamo.

## Estructura del proyecto

```
biblioteca/
├── backend/
│   └── biblioteca.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```

**Ejecutar el backend:** `python backend/biblioteca.py`
**Ver el frontend:** abrir `frontend/index.html` en el navegador.

## Parte Python (POO)

### Clase padre: `MaterialBiblioteca`

Contiene lo que comparten todos los materiales: los atributos `titulo`, `codigo` y `disponibilidad`, y el método `mostrar_informacion()`. También declara `calcular_dias_prestamo()`, que obliga a cada clase hija a definir sus propios días de préstamo.

### Clases hijas

- **`Libro`**: hereda de `MaterialBiblioteca` y agrega el atributo `autor`. Su préstamo dura **7 días**.
- **`Revista`**: hereda de `MaterialBiblioteca` y agrega el atributo `numero_edicion`. Su préstamo dura **3 días**.

### Método sobrescrito

`mostrar_informacion()` está definido en la clase padre y sobrescrito en `Libro` y `Revista`. Cada hija reutiliza el texto base con `super()` y le añade su dato propio (autor o número de edición). `calcular_dias_prestamo()` también se redefine en cada hija con su propio valor.

### Polimorfismo

En `main()` se crea una sola lista con 2 libros y 2 revistas. Un único ciclo `for` recorre la lista y llama a `mostrar_informacion()` y `calcular_dias_prestamo()` sobre cada objeto, sin preguntar de qué tipo es. Python ejecuta automáticamente la versión que corresponde: un libro muestra su autor y devuelve 7 días; una revista muestra su edición y devuelve 3 días.

## Parte Frontend

- **HTML:** define la estructura de la página con etiquetas semánticas (`header`, `main`, `section`, `article`, `footer`). Muestra el nombre del sistema, el catálogo y, en cada material, su título, tipo, disponibilidad, datos relevantes y el botón de préstamo.
- **CSS:** da el diseño visual. Presenta los materiales en tarjetas dentro de una cuadrícula, usa azul para los libros y magenta para las revistas, distingue disponible (verde) y prestado (rojo), y deshabilita visualmente el botón cuando no hay disponibilidad.
- **JavaScript:** escucha el evento `click` de los botones de préstamo y muestra un mensaje indicando qué material seleccionó el usuario.

## Frontend y backend: responsabilidades

**Frontend (lo que ve y usa el usuario):**
- Mostrar el catálogo y la información de cada material.
- Recibir las acciones del usuario, como presionar "Solicitar préstamo".
- Mostrar mensajes y respuestas en pantalla.

**Backend (la lógica del sistema, aquí representada con Python):**
- Definir los tipos de material y sus reglas (por ejemplo, 7 días para libros y 3 para revistas).
- Verificar si un material está disponible antes de prestarlo.
- Guardar y actualizar el estado de los materiales.

## Flujo conceptual

**Usuario → Frontend → Backend → Respuesta → Frontend**

1. El **usuario** presiona "Solicitar préstamo" en una tarjeta.
2. El **frontend** captura la acción y enviaría la solicitud al sistema.
3. El **backend** revisaría si el material está disponible, aplicaría los días de préstamo y prepararía el resultado.
4. El backend enviaría una **respuesta** (préstamo aprobado o rechazado).
5. El **frontend** mostraría esa respuesta al usuario.

> **Aclaración:** en este proyecto **no existe una conexión real** entre Python y el frontend, porque la actividad no la requiere. El flujo anterior es solo una explicación conceptual. El frontend muestra datos escritos directamente en el HTML y el mensaje del botón lo genera únicamente JavaScript.
