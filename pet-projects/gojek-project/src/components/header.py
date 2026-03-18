import flet as ft
from flet import *

# @ft.component

def Header():
    return ResponsiveRow([
		
		Column(
			col={"sm":12,"md":12,"lg":12},
			controls=[
				Container(
					border_radius = BorderRadius.all(30),
					padding=10,
					bgcolor="#DEDEDE",
					content=Row([
							# INSERT LOGO GOJEK HERE
							Image(
								src="https://flet.dev/img/logo.svg",
								fit="contain",
								width=120,
								height=50
								),
							CircleAvatar(foreground_image_src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnvVX91SdXFqCZ9Xn4QHoRl1kStmfxSSkF0sfFsV9v&s")
						], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
					)
				)
			])
		])
