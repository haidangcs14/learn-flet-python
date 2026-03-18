import flet as ft
from flet import *

def badge_item(text, active=False):
        return Container(
            margin=Margin.only(top=10),
            border_radius=30,
            padding=10,
            ink=True,
            on_click=lambda e: print(text),
            bgcolor="#41AE62" if active else None,
            border=Border.all(2, "#E1E1E1"),
            content=Text(
                text,
                size=13,
                color="white" if active else Colors.BLACK
            )
        )

def card_item():
        return Card(
            elevation=30,
            content=Container(
                bgcolor="white",
                padding=10,
                content=Column([
                    Image(
                        src="https://lelogama.go-jek.com/post_featured_image/header-paylater-voucher-gofood-plus.jpg",
                        fit="contain",
                        width=300,
                        height=220
                    ),
                    Text("Get Up 50 K Cashback", size=20, weight=FontWeight.BOLD),
                    Text(
                        '''
						Upgrade to Gopay Plus now,
                    	enjoy cashback up to 50K 
                        when using PayLater!''',
                        size=15,
                        color=Colors.GREY
                    )
                ])
            )
        )

@ft.component
def Badge():

    badges = ["All", "Covid-19", "Donation", "Entertainment"]

    return Container(
        margin=Margin.only(top=40, left=10),
        content=Column([
            Text("Top Picks For You", size=30, weight="bold"),

            # BADGE LIST
            Row(
                controls=[
                    badge_item(b, active=(b == "All")) for b in badges
                ],
                alignment=MainAxisAlignment.SPACE_AROUND
            ),

            # CARD LIST
            Container(
                content=Row(
                    controls=[card_item() for _ in range(5)],
                    scroll="always"
                )
            )
        ])
    )