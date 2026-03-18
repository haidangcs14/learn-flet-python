import flet as ft
from flet import *

def Badge():
    return Container(
		margin = Margin.only(top=40,left=10),
		content=Column([
			Text("Top Picks For You",size=30,weight="bold"),
			Row(
                [
					Container(
						margin = Margin.only(top=10),
						border_radius=30,
						padding=10,
						bgcolor="#41AE62",
						ink=True,
						on_click=lambda e: print("badge test"),
						border = Border.all(2,"#E1E1E1"),
						content = Text("All",size=13,color="white")
					),
					Container(
						margin = Margin.only(top=10),
						border_radius=30,
						padding=10,
						ink=True,
						on_click=lambda e: print("badge test"),
						border = Border.all(2,"#E1E1E1"),
						content = Text("Covid-19",size=13,color=Colors.BLACK)
					),
					Container(
						margin = Margin.only(top=10),
						border_radius=30,
						padding=10,
						ink=True,
						on_click=lambda e: print("badge test"),
						border = Border.all(2,"#E1E1E1"),
						content = Text("Donation",size=13,color=Colors.BLACK)
					),
					Container(
						margin = Margin.only(top=10),
						border_radius=30,
						padding=10,
						ink=True,
						on_click=lambda e: print("badge test"),
						border = Border.all(2,"#E1E1E1"),
						content = Text("Entertainment",size=13,color=Colors.BLACK)
					),
				],
				alignment=MainAxisAlignment.SPACE_AROUND
            ),

			# FOR CARD SECTION
			Container(
			# margin = margin.only(bottom=40),
			content=Row([
				Card(
					elevation=30,
					content=Container(
					bgcolor="white",
					padding=10,
					content=Column([
						Image(
						src="https://lelogama.go-jek.com/post_featured_image/header-paylater-voucher-gofood-plus.jpg",
						fit="contain",
						width=300, height=220),
						Text("Get Up 50 K Cashback", size=20, weight=FontWeight.BOLD),
						Text('''upgrade to Gopay plus now 
							,enjoy cashback up to 50 K 
							if you transact with PayLater !
           					''',
                            size=15,
                            color=Colors.GREY)
					])
				)),
				Card(
					elevation=30,
					content=Container(
					bgcolor="white",
					padding=10,
					content=Column([
						Image(
						src="https://lelogama.go-jek.com/post_featured_image/header-paylater-voucher-gofood-plus.jpg",
						fit="contain",
						width=300, height=220),
						Text("Get Up 50 K Cashback", size=20, weight=FontWeight.BOLD),
						Text('''upgrade to Gopay plus now 
							,enjoy cashback up to 50 K 
							if you transact with PayLater !
							''',
                            size=15,
                            color=Colors.GREY)
						])
					)),
				],scroll="always")
			)
		])
	)