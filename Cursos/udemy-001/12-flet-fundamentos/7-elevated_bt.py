import flet as ft

def main(page: ft.Page):
    page.title = "Botão com conteúdo customizado"

    # Tema e alinhamento
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f5f5f5"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.ElevatedButton(
                    width=180,
                    bgcolor="white",
                    elevation=3,
                    content=ft.Row(
                        [
                            ft.Icon(icon="favorite", color="pink"),
                            ft.Icon(icon="audiotrack", color="green"),
                            ft.Icon(icon="beach_access", color="blue"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
                ft.ElevatedButton(
                    bgcolor="white",
                    elevation=3,
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(value="Botão Composto", size=18, weight="bold"),
                                ft.Text(value="Texto Secundário", size=12, color="gray"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5
                        ),
                        padding=ft.padding.all(10)
                    )
                )
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)