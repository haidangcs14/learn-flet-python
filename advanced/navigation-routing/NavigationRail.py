import flet as ft

@ft.observable
class RailState:
    selected_index: int = 0

state = RailState()

@ft.component
def ContentPanel():
    ft.use_state(state)

    labels = ["Home", "Settings", "About"]
    return ft.Container(
        content=ft.Text(labels[state.selected_index], size=24),
        expand=True,
        alignment=ft.Alignment.CENTER,
    )

@ft.component
def SideNavApp():
    ft.use_state(state)

    return ft.Row([
        ft.NavigationRail(
            selected_index=state.selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Settings"),
                ft.NavigationRailDestination(icon=ft.Icons.INFO, label="About"),
            ],
            on_change=lambda e: setattr(state, 'selected_index', e.control.selected_index),
        ),
        ft.VerticalDivider(width=1),
        ContentPanel(),    
    ], expand=True)

def main(page: ft.Page):
    page.title = "Navigation Rail"
    page.window.width = 500
    page.window.height = 800 

    page.render(SideNavApp)

ft.run(main)