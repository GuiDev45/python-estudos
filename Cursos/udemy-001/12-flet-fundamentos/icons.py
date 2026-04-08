import flet as ft

def main(page: ft.Page):
    icons_row = ft.Row(
        controls=[
            ft.Icon(icon="favorite", color=ft.Colors.PINK, size=30),
            ft.Icon(icon="audiotrack", color=ft.Colors.GREEN_400, size=30),
            ft.Icon(icon="beach_access", color=ft.Colors.BLUE, size=30),
            ft.Icon(icon="settings", color="#c1c1c1", size=30),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(
        ft.Column(
            controls=[icons_row]
        )
    )

ft.run(main)