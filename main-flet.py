import flet as ft
import flet.canvas as cv

# Configuración de la grilla
ROWS = 30
COLS = 30
CELL_SIZE = 20


def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Juego de la Vida de Conway"
    page.window.width = 900
    page.window.height = 750
    page.window.center()
    page.theme_mode = ft.ThemeMode.DARK

    # Dibujar las celdas
    shapes = []

    for row in range(ROWS):
        for col in range(COLS):
            shapes.append(
                cv.Rect(
                    x=col * CELL_SIZE,
                    y=row * CELL_SIZE,
                    width=CELL_SIZE,
                    height=CELL_SIZE,
                    paint=ft.Paint(
                        style=ft.PaintingStyle.STROKE,
                        stroke_width=1,
                        color=ft.Colors.GREY_600,
                    ),
                )
            )

    # Crear el tablero
    board = cv.Canvas(
        shapes=shapes,
        width=COLS * CELL_SIZE,
        height=ROWS * CELL_SIZE,
    )

    # Agregar todo a la página
    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Juego de la Vida de Conway",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.Alignment.CENTER,
                        padding=ft.Padding.only(top=20, bottom=20),
                    ),
                    ft.Container(
                        content=board,
                        alignment=ft.Alignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
    )


ft.app(target=main)