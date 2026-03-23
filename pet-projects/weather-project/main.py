import flet as ft
import requests
import datetime
from pathlib import Path
import os

API_KEY = "018d70889154ca3c7a46855b153c73b9"
LOCATION = "quảng trị"


_current = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric&lang=vi"
)

# lits of days of the week
days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
]

def get_assets_dir() -> Path:
        default_assets_dir = Path(__file__).parent / "assets"   # fallback for local runs
        return Path(os.environ.get("FLET_ASSETS_DIR", str(default_assets_dir))).resolve()


def main(page: ft.Page):
    page.title = "WEATHER APP"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 800

    # animation
    def _expand(e):
        if e.data == True:
            _c.content.controls[1].height = 560
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.4
            _c.content.controls[1].update()

    # current temp
    def _current_temp():
        _current_temp = int(_current.json()['main']['temp'])
        _current_weather = _current.json()['weather'][0]['main']
        _current_description = _current.json()['weather'][0]['description']
        _current_wind = int(_current.json()['wind']['speed'])
        _current_humidity = _current.json()['main']['humidity']
        _current_feels = _current.json()['main']['feels_like']
        return [
            _current_temp, 
            _current_weather, 
            _current_description, 
            _current_wind, 
            _current_humidity, 
            _current_feels
        ]
    
    # current extra
    def _current_extra():
        
        _extra_info = []

        _extra = [
            [
                int(_current.json()["visibility"] / 1000),
                "Km",
                "Visibility",
                f"{get_assets_dir()}\\visibility.png"
            ],
            [
                round(_current.json()["main"]["pressure"] * 0.03, 2),
                "inHg",
                "Pressure",
                f"{get_assets_dir()}\\barometer.png"
            ],
            [
                datetime.datetime.fromtimestamp(
                    _current.json()["sys"]["sunset"]
                ).strftime("%I:%M %p"),
                "",
                "Sunset",
                f"{get_assets_dir()}\\sunset.png"
            ],
            [
                datetime.datetime.fromtimestamp(
                    _current.json()["sys"]["sunrise"]
                ).strftime("%I:%M %p"),
                "",
                "Sunrise",
                f"{get_assets_dir()}\\sunrise.png"
            ],
        ]

        for data in _extra:
            _extra_info.append(
                ft.Container(
                    bgcolor=ft.Colors.WHITE_10,
                    alignment=ft.Alignment.CENTER,
                    border_radius=12,
                    content=ft.Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            ft.Image(
                                src=data[3],
                                color=ft.Colors.WHITE,
                                width=32,
                                height=32,
                            ),

                            ft.Container(
                                content=ft.Column(
                                    alignment="center",
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        ft.Text(
                                            value=str(data[0]) + " " + data[1], 
                                            size=14,
                                        ),
                                        ft.Text(
                                            value=data[2], 
                                            size=11,
                                            color=ft.Colors.WHITE_54,
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
        
        return _extra_info

    # bottom data
    def _bot_data():
        _bot_data = []

        for idx in range(1, 8):
            _bot_data.append(
                ft.Row(
                    spacing=5, 
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            expand=1,
                            alignment=ft.MainAxisAlignment.START,
                            controls=[
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Text(
                                        days
                                        [
                                            datetime.datetime.weekday(
                                                datetime.datetime.fromtimestamp(
                                                    _current.json()["dt"]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        ft.Row(
                            expand=1,
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.START,
                                        controls=[
                                            ft.Container(
                                                width=20,
                                                height=20,
                                                alignment=ft.Alignment.CENTER_LEFT,
                                                content=ft.Image(
                                                    src=f"{get_assets_dir()}\\cloudy.png", # replace to img in weather
                                                )
                                            ),
                                            ft.Text(
                                                value=_current.json()['weather'][0]['main'], # replace to idx
                                                size=11,
                                                color=ft.Colors.WHITE_54,
                                                text_align="center",
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),

                        ft.Row(
                            expand=1,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.Container(
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Row(
                                        alignment=ft.Alignment.CENTER,
                                        spacing=5,
                                        controls=[
                                            ft.Container(
                                                width=30,
                                                content=ft.Text(
                                                    value=str(int(_current.json()['main']['temp_min'])) + "°", # replace to min daily temp
                                                    text_align=ft.MainAxisAlignment.START,
                                                )
                                            ),
                                            ft.Container(
                                                width=30,
                                                content=ft.Text(
                                                    value=str(int(_current.json()['main']['temp_max'])) + "°", # replace to min daily temp
                                                    text_align=ft.MainAxisAlignment.END,
                                                )
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        
        return _bot_data

    # top container
    def _top():

        _today = _current_temp()
        
        _today_extra = ft.GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in _current_extra():
            _today_extra.controls.append(info)

        return ft.Container(
            width=310,
            height=660 * 0.4,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.BOTTOM_LEFT,
                end=ft.Alignment.TOP_RIGHT,
                colors=[ft.Colors.LIGHT_BLUE_600, ft.Colors.LIGHT_BLUE_900],
            ),
            border_radius=35,
            animate=ft.Animation(duration=450, curve="decelerate"),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=ft.Column(
                alignment="start",
                spacing=10,
                controls=[
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Text(
                                "Toronto, CA",
                                size=16,
                                weight=ft.FontWeight.W_500,
                            ),
                        ]
                    ),
                    ft.Container(
                        padding=ft.Padding.only(bottom=5)
                    ),
                    ft.Row(
                        alignment="center",
                        spacing=30,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Image(
                                        width=90,
                                        height=90,
                                        src=f"{get_assets_dir()}\\cloudy.png"
                                    )
                                ],
                            ),
                            ft.Column(
                                spacing=5,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Today",
                                        size=12,
                                        text_align="center",
                                    ),
                                    ft.Row(
                                        vertical_alignment=ft.CrossAxisAlignment.START,
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                content=ft.Text(
                                                    _today[0],
                                                    size=52,
                                                )
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "°",
                                                    size=28,
                                                    text_align="center",
                                                )
                                            ),                                               
                                        ],
                                    ),
                                    ft.Text(
                                        _today[1] + " - Overcast",
                                        size=10,
                                        color=ft.Colors.WHITE_54,
                                        text_align="center",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    ft.Divider(height=8, thickness=1, color=ft.Colors.WHITE_10),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        ft.Image(
                                            width=20,
                                            height=20,
                                            src=f"{get_assets_dir()}\\wind.png",
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            value=str(_today[3]) + " km/h", 
                                            size=11,
                                        ),
                                        ft.Text(
                                            value="Wind", 
                                            size=9,
                                            color=ft.Colors.WHITE_54,
                                        ),
                                    ],
                                ),
                            ),     
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        ft.Image(
                                            width=20,
                                            height=20,
                                            src=f"{get_assets_dir()}\\humidity.png",
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            value=str(_today[4]) + "%", 
                                            size=11,
                                        ),
                                        ft.Text(
                                            value="Humidity", 
                                            size=9,
                                            color=ft.Colors.WHITE_54,
                                        ),
                                    ],
                                ),
                            ),     
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        ft.Image(
                                            width=20,
                                            height=20,
                                            src=f"{get_assets_dir()}\\thermometer.png",
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            value=str(_today[5]) + "°", 
                                            size=11,
                                        ),
                                        ft.Text(
                                            value="Feels like", 
                                            size=9,
                                            color=ft.Colors.WHITE_54,
                                        ),
                                    ],
                                ),
                            ),     
                        ],
                    ),

                    # on hover
                    _today_extra,
                ],
            ),
        )

    # bottom container
    def _bottom():
        _bottom_column = ft.Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=25,
        )
        
        for data in _bot_data():
            _bottom_column.controls.append(data)

        return ft.Container(
            padding=ft.Padding.only(top=280, left=20, right=20, bottom=20),
            content=_bottom_column,
        )


    _c = ft.Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor=ft.Colors.BLACK,
        padding=10,
        content=ft.Stack(
            width=300, height=550,
            controls=[
                _bottom(), 
                _top(),
            ],
        )
    )

    page.add(_c)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")