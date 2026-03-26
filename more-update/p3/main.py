import flet as ft
from dataclasses import dataclass


@dataclass
class Food:
    name: str
    img_path: str = None
    stamina: int = 0
    skill: int = 0
    luck: int = 0


FOOD_LIST = [
    Food("apple_pie", "apple_pie.png", 3, 5, 2),
    Food("bacon", "bacon.png", 8, 7, 5),
    Food("bread", "bread.png", 5, 4, 2),
    Food("burger", "burger.png", 4, 3, 9),
]

@ft.component
def App():

    foods: dict[str, Food] = {food.name: food for food in FOOD_LIST}

    food: Food
    food, set_food = ft.use_state(foods["apple_pie"])
    snackbar_key, set_snackbar_key = ft.use_key = ft.use_state(0)

    def handle_selected(e):
        set_food(foods[e.control.value])
        set_snackbar_key(snackbar_key + 1)

    def handle_snackbar_message(food_name: str):

        match food_name:
            case "apple_pie":
                message = "This is apple pie!"
            case "bacon":
                message = "This is bacon!"
            case "bread":
                message = "This is bread!"
            case "burger":
                message = "This is burger!"

        return message

    return ft.Column(
        controls=[
            ft.Text("Dropdown demo", size=30),
            ft.Dropdown(
                label="Choose food",
                options=[ft.DropdownOption(text=food.name) for food in foods.values()],
                value=food.name,
                on_select=handle_selected,
            ),
            ft.Row(
                controls=[
                    ft.Image(src=food.img_path, width=100, height=100),
                    ft.Column(
                        controls=[
                            ft.Text(f"Skill: {food.skill}", size=22),
                            ft.Text(f"Luck: {food.luck}", size=22),
                            ft.Text(f"Stamina: {food.stamina}", size=22),
                        ],
                    ),
                ]
            ),
            ft.SnackBar(
                content=ft.Text(value=handle_snackbar_message(food.name)),
                key=f"snackbar_{snackbar_key}",
                open=snackbar_key > 0,
                on_dismiss=lambda e: set_snackbar_key(0),
            ),
        ]
    )


def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 800

    page.render(App)


ft.run(main, assets_dir="assets")
