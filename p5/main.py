import flet as ft
 
@ft.component
def ClickExample():
    count, set_count = ft.use_state(0)
    
    return ft.Column([
        ft.Text(f"Clicked: {count} times"),
        ft.Button("Click me!", on_click=lambda _: set_count(count + 1)),
    ])

@ft.component
def ItemList():
    selected, set_selected = ft.use_state("")
    
    def handle_click(e):
        set_selected(e.control.data)
    
    return ft.Column([
        ft.Text(f"Selected: {selected}"),
        ft.Button("Item 1", data="item-1", on_click=handle_click),
        ft.Button("Item 2", data="item-2", on_click=handle_click),
        ft.Button("Item 3", data="item-3", on_click=handle_click),
    ])

@ft.component
def LiveSearch():
    query, set_query = ft.use_state("")
    
    return ft.Column([
        ft.TextField(
            label="Tìm kiếm",
            value=query,
            on_change=lambda e: set_query(e.control.value),
        ),
        ft.Text(f"Bạn đang tìm: {query}") if query else ft.Container(),
    ])

@ft.component
def SubmitExample():
    items, set_items = ft.use_state([])
    input_val, set_input = ft.use_state("")
    
    def handle_submit(_):
        if input_val:
            set_items([*items, input_val])
            set_input("")
    
    return ft.Column([
        ft.TextField(
            label="Nhập và nhấn Enter",
            value=input_val,
            on_change=lambda e: set_input(e.control.value),
            on_submit=handle_submit,
        ),
        ft.Column([ft.Text(f"• {item}") for item in items]),
    ])

@ft.component
def FocusExample():
    focused, set_focused = ft.use_state(False)
    
    return ft.Container(
        content=ft.TextField(
            label="Focus me",
            on_focus=lambda _: set_focused(True),
            on_blur=lambda _: set_focused(False),
        ),
        border=ft.Border.all(2, ft.Colors.GREEN if focused else ft.Colors.GREY),
        padding=10,
        border_radius=10,
    )

@ft.component
def HoverCard():
    hovered, set_hovered = ft.use_state(False)
    
    return ft.Container(
        content=ft.Text("Hover me!"),
        bgcolor=ft.Colors.GREEN_200 if hovered else ft.Colors.BLUE_100,
        padding=20,
        border_radius=10,
        on_hover=lambda e: set_hovered(e.data),
    )

def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 600 
    # page.render(ClickExample)
    # page.render(ItemList)
    # page.render(LiveSearch)
    # page.render(SubmitExample)
    # page.render(FocusExample)
    page.render(HoverCard)
 
ft.run(main)