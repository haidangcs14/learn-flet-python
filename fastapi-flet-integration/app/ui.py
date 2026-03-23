import flet as ft
import requests

def build_ui(page: ft.Page):

    def get_health():
        res = requests.get("http://localhost:8550/api/health")
        data = res.json()

        main_message.value = f"Health status: {data['status']}"
        page.update()
        
    main_message = ft.Text("Hello world from flet-fastapi-app")
    
    health_button = ft.Button("Get Health", on_click=lambda e: page.run_thread(get_health))

    page.add(main_message, health_button)