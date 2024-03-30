import flet as ft


def main(page: ft.Page):
    page.title = "flet counter app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_textbox = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        if int(number_textbox.value) > 0:
            number_textbox.value = str(int(number_textbox.value) - 1)
            page.update()

    def plus_click(e):
        number_textbox.value = str(int(number_textbox.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                number_textbox,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)
