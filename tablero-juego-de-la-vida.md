# Tablero — Juego de la Vida de Conway (Python + Flet)

> Marca cada casilla con `[x]` a medida que la completen. Las tareas de "Integración" las hacen juntos.

---

## 🟦 SPRINT 1 — Fundamentos

### Persona A — Núcleo del juego (lógica pura, sin UI)
- [ ] Definir estructura de datos de la grilla (matriz 2D o set de celdas vivas)
- [ ] Método `get_cell(x, y)` → devuelve estado (vivo/muerto)
- [ ] Método `set_cell(x, y, valor)` → cambia estado de una celda
- [ ] Función para contar vecinos vivos de una celda
- [ ] Método `step()` → aplica las 4 reglas de Conway y genera la siguiente generación
- [ ] Método para inicializar grilla vacía o aleatoria
- [ ] Escribir 2-3 pruebas manuales (ej: un *blinker* debe oscilar entre dos estados)

### Persona B — Interfaz básica (Flet)
- [x] Crear ventana principal en Flet
- [ ] Dibujar una grilla de celdas (Canvas o GridView) con tamaño fijo, sin lógica aún
- [ ] Hacer que clic en una celda cambie su color (visual, sin conectar al núcleo todavía)
- [ ] Layout base: espacio para la grilla + espacio para futuros botones/controles

### Juntos — Integración
- [ ] Acordar el "contrato": nombres exactos de métodos de la clase `Grid` (¡antes de programar cada uno por su lado!)
- [ ] Conectar clic en la UI → llama a `set_cell()` del núcleo
- [ ] Probar juntos: ¿se ve reflejado el clic correctamente en pantalla?

**✅ Meta del sprint:** poder hacer clic y encender/apagar celdas en pantalla (sin animación todavía).

---

## 🟩 SPRINT 2 — Simulación completa

### Persona A — Núcleo
- [ ] Agregar patrones predefinidos (glider, blinker, toad, etc.) como diccionario o funciones
- [ ] Método para cargar un patrón en la grilla desde una posición dada
- [ ] (Opcional) Detectar si la simulación llegó a un estado estable o vacío

### Persona B — Interfaz
- [ ] Botón **Play**
- [ ] Botón **Pause**
- [ ] Botón **Step** (avanzar una sola generación)
- [ ] Botón **Reset** (limpiar grilla)
- [ ] Slider de velocidad de simulación
- [ ] Contador visible de "Generación N"

### Juntos — Integración
- [ ] Loop de animación: cada N milisegundos llama a `step()` y redibuja
- [ ] Conectar slider de velocidad al loop
- [ ] Menú o botones para cargar patrones predefinidos en la grilla
- [ ] Probar el flujo completo: cargar patrón → play → pause → step → reset

**✅ Meta del sprint:** el juego funciona de punta a punta.

---

## 🟨 SPRINT 3 — Pulido (opcional)

- [ ] Guardar patrón actual en archivo (JSON o texto)
- [ ] Cargar patrón desde archivo
- [ ] Grilla toroidal (los bordes se conectan) o grilla infinita
- [ ] Mejoras visuales: tema oscuro, colores, zoom/pan
- [ ] Empaquetar la app (ej: `flet pack`) para compartirla como ejecutable

---

## Checklist de proceso (cada semana)

- [ ] Lunes: elegir tareas de la semana entre los dos
- [ ] Cada día: mensaje corto de avance ("hice X, hoy hago Y, bloqueo: Z")
- [ ] Viernes: probar juntos lo construido (Review)
- [ ] Viernes: qué siguió bien / qué cambiar (Retro rápida)

**Definición de "hecho":** el código corre sin errores, el otro compañero lo probó manualmente, y está subido a `main` en GitHub.
