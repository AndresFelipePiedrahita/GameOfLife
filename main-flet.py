import flet as ft


def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Juego de la Vida de Conway"
    page.window.width = 1000
    page.window.height = 700
    page.window.min_width = 800
    page.window.min_height = 600
    page.window.center()
    page.theme_mode = ft.ThemeMode.DARK

    # Contenido temporal
    page.add(
        ft.Text(
            "Juego de la Vida de Conway",
            size=28,
            weight=ft.FontWeight.BOLD
        )
    )


ft.app(target=main)