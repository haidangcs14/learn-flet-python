import flet as ft
from fastapi import FastAPI
from app.api import register_routes
from app.ui import build_ui
import flet.fastapi as ff

# main ui
def main(page: ft.Page):
    build_ui(page)

app = FastAPI() # backend server   
register_routes(app) # dang ki cac api endpoints

flet_app = ff.app(main, before_main=None) # chuyển app Flet thành ASGI app (để chạy cùng FastAPI)
app.mount("/", flet_app) # gan app vao endpoint "/"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8550, reload=True) # for dev to auto reload page