'''
Thử thách mở rộng
- Percentage (%) - Thêm phép tính phần trăm
- Parentheses - Thêm dấu ngoặc ()
- History - Lưu lịch sử tính toán
- Keyboard support - Nhập từ bàn phím
- Scientific mode - Thêm sin, cos, sqrt…

'''
import flet as ft
import math
import re

@ft.observable
class CalcState:
    def __init__(self):
        self.expression: str = ""
        self.result: str = "0"
        self.angle_mode: str = "RAD"   # RAD hoặc DEG
        self.history: list = []

    def input(self, value: str):
        if (self.expression.endswith("%") and value.isdigit()):
            self.expression += "×"
        self.expression += value
    
    def clear(self):
        self.expression = ""
        self.result = "0"
    
    def delete(self):
        self.expression = self.expression[:-1]
    
    def calculate(self):
        try:
            # replate chars to eval
            expr = self.expression.replace("×", "*").replace("÷", "/").replace("^", "**").replace("%", "/100").replace("√", "sqrt")
        
            # scientific
            if self.angle_mode == "DEG":
                def sin(x): return math.sin(math.radians(x))
                def cos(x): return math.cos(math.radians(x))
                def tan(x): return math.tan(math.radians(x))
            else:
                sin = math.sin
                cos = math.cos
                tan = math.tan

            sqrt = math.sqrt
            log = math.log10

            self.result = str(round(eval(expr, {
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "sqrt": sqrt,
                "log": log
            }), 5))
            self.history.append((self.expression, self.result))
        except:
            self.result = "Error"

    # change angle mode
    def toggle_mode(self):
        self.angle_mode = "DEG" if self.angle_mode == "RAD" else "RAD"
    
    # toggle sign of last number
    def toggle_sign(self):
        # search last num in epxression
        '''
        \d+	1 hoặc nhiều chữ số
        \.?	dấu . (thập phân) có thể có hoặc không
        \d*	phần thập phân
        $	ở cuối chuỗi
        '''
        match = re.search(r'(\d+\.?\d*)$', self.expression) 

        if match:
            num = match.group(1)
            start = match.start(1)

            self.expression = (self.expression[:start] + f"({num})")
            
state = CalcState()

# component to display result
@ft.component
def DisplayResult():

    ft.use_state(state)

    return ft.Container(
        content=ft.Column([
            ft.Text(
                "Ans = " + state.expression if state.expression else "",
                size=24,
                color=ft.Colors.GREY_500,
                text_align=ft.TextAlign.RIGHT,
            ),
            ft.Text(
                state.result,
                size=48,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.RIGHT,
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.END, spacing=5),
        padding=20,
        bgcolor=ft.Colors.GREY_100,
        border_radius=ft.BorderRadius.only(top_left=20, top_right=20),
        alignment=ft.Alignment.CENTER_RIGHT,
    )

# component for buttons
@ft.component
def CalcButton(text: str, expand: int = 1, bg_color=None, text_color=None):
    def on_click(_):
        if text == "C":
            state.clear()
        elif text == "⌫":
            state.delete()
        elif text == "=":
            state.calculate()
        elif text == "+/-":
            state.toggle_sign()
        else:
            state.input(text)
    
    return ft.Container(
        content=ft.Text(text, size=16, weight=ft.FontWeight.W_500, color=text_color),
        bgcolor=bg_color or ft.Colors.WHITE,
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        expand=expand,
        height=70,
        on_click=on_click,
    )

@ft.component
def ButtonGrid():
    
    ft.use_state(state)
    
    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Switch(
                    label=f"{state.angle_mode}",
                    value=state.angle_mode == "DEG",
                    on_change=lambda e: state.toggle_mode()
                ),
                CalcButton("(", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton(")", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("%", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("⌫", bg_color=ft.Colors.GREY_700, text_color=ft.Colors.WHITE),
            ], spacing=10),
            ft.Row([
                CalcButton("sin", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("cos", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("7"),
                CalcButton("8"),
                CalcButton("9"),
                CalcButton("÷", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
            ], spacing=10),
            ft.Row([
                CalcButton("√", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("tan", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("4"),
                CalcButton("5"),
                CalcButton("6"),
                CalcButton("×", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
            ], spacing=10),
            ft.Row([
                CalcButton("log", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("^", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("1"),
                CalcButton("2"),
                CalcButton("3"),
                CalcButton("-", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
            ], spacing=10),
            ft.Row([
                CalcButton("+/-", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("C", bg_color=ft.Colors.RED_100, text_color=ft.Colors.RED),
                CalcButton("0"),
                CalcButton("."),
                CalcButton("=", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
                CalcButton("+", bg_color=ft.Colors.ORANGE, text_color=ft.Colors.WHITE),
            ], spacing=10),
        ], spacing=10),
        padding=15,
        width=400,
    )

# handle keyboard input
def keyboard(e: ft.KeyboardEvent):
    key = e.key
    # SHIFT mappings
    if e.shift:
        shift_map = {"8": "*","9": "(","0": ")","=": "+","5": "%",}
        if key in shift_map:
            state.input(shift_map[key])
            return
    # numbers
    if key.isdigit():
        state.input(key)
    # operators
    elif key in ["+", "-", "*", "/"]:
        state.input(key)
    # dot
    elif key == ".":
        state.input(".")
    # percent
    elif key == "%":
        state.input("%")
    # enter
    elif key == "Enter":
        state.calculate()
    # delete
    elif key == "Backspace":
        state.delete()
    # clear
    elif key == "Escape":
        state.clear()

@ft.component
def HistoryButton(page: ft.Page):
    def open_history(_):
        history_items = []
        for expr, res in reversed(state.history):
            history_items.append(
                ft.Row(
                    [
                        ft.Container(
                            ft.Text(expr, color=ft.Colors.BLUE),
                            padding=10,
                            border=ft.Border.all(1, ft.Colors.GREY_400),
                            border_radius=10,
                            align=ft.Alignment.CENTER,
                            expand=True
                        ),

                        ft.Text("=", size=20),

                        ft.Container(
                            ft.Text(res, color=ft.Colors.BLUE),
                            padding=10,
                            border=ft.Border.all(1, ft.Colors.GREY_400),
                            border_radius=10,
                            align=ft.Alignment.CENTER,
                            expand=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                )
            )

        dialog = ft.AlertDialog(
            title=ft.Text("Calculation History", align=ft.Alignment.CENTER),
            content=ft.Container(
                width=350,
                height=300,
                content=ft.Column(
                    history_items if history_items else [ft.Text("No history", align=ft.Alignment.CENTER)],
                    scroll=ft.ScrollMode.AUTO,
                    spacing=10
                )
            )
        )
        page.show_dialog(dialog) 

    return ft.IconButton(
        icon=ft.Icons.HISTORY,
        icon_color=ft.Colors.BLUE,
        on_click=open_history
    )

@ft.component
def CalcApp(page: ft.Page):
    return ft.Container(
        content=ft.Column([
            HistoryButton(page),
            DisplayResult(),
            ButtonGrid(),
        ], spacing=0),
        bgcolor=ft.Colors.GREY_200,
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.BLACK_26),
    )


def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.width = 400
    page.window.height = 800 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.CYAN_100

    page.on_keyboard_event = keyboard
    
    page.render(lambda: CalcApp(page))

 
ft.run(main)