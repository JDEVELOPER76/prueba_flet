import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Básica"
    page.window_width = 350
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.LIGHT

    # Pantalla de resultado
    display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        expand=True,
        height=100,
        bgcolor=ft.colors.GREY_200
    )

    # Almacenar la expresión actual
    expression = ""

    def button_click(e):
        nonlocal expression
        btn = e.control

        if btn.text == "=":
            try:
                # Evaluar la expresión
                result = eval(expression)
                display.value = str(result)
                expression = str(result)
            except:
                display.value = "Error"
                expression = ""
        elif btn.text == "C":
            display.value = "0"
            expression = ""
        elif btn.text == "←":
            expression = expression[:-1]
            display.value = expression if expression else "0"
        else:
            if display.value == "0" and btn.text not in ["+", "-", "*", "/"]:
                display.value = btn.text
                expression = btn.text
            else:
                display.value += btn.text
                expression += btn.text

        page.update()

    # Botones de la calculadora
    buttons = [
        [ft.ElevatedButton("C", on_click=button_click, width=70, height=70, bgcolor=ft.colors.RED_300),
         ft.ElevatedButton("←", on_click=button_click, width=70, height=70, bgcolor=ft.colors.ORANGE_300),
         ft.ElevatedButton("/", on_click=button_click, width=70, height=70, bgcolor=ft.colors.BLUE_300),
         ft.ElevatedButton("*", on_click=button_click, width=70, height=70, bgcolor=ft.colors.BLUE_300)],
        [ft.ElevatedButton("7", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("8", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("9", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("-", on_click=button_click, width=70, height=70, bgcolor=ft.colors.BLUE_300)],
        [ft.ElevatedButton("4", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("5", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("6", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("+", on_click=button_click, width=70, height=70, bgcolor=ft.colors.BLUE_300)],
        [ft.ElevatedButton("1", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("2", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("3", on_click=button_click, width=70, height=70),
         ft.ElevatedButton("=", on_click=button_click, width=70, height=70, bgcolor=ft.colors.GREEN_300)],
        [ft.ElevatedButton("0", on_click=button_click, width=145, height=70),
         ft.ElevatedButton(".", on_click=button_click, width=70, height=70)]
    ]

    # Layout
    row_buttons = []
    for row in buttons:
        row_buttons.append(ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY, controls=row))

    page.add(
        ft.Column(
            controls=[
                ft.Container(content=display, padding=10),
                ft.Column(controls=row_buttons, spacing=5, alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )

# Ejecutar la aplicación
ft.app(target=main)
  
