# import flet as ft
# from flet import *
# import cv2
# import os


# def register_click(name, job):
#     # name_job = f"{name} - {job}"
#     # capture = cv2.VideoCapture(0)

#     # while True:
#     #     _, frame = capture.read()
#     #     cv2.imshow("Cap face", frame)

#     #     if cv2.waitKey(1) & 0xFF == ord("s"):
#     #         img_path = os.path.join("face", f"{name_job}.ipg")
#     #         cv2.imwrite(img_path, frame)
#     #         break
#     #     elif cv2.waitKey(1) & 0xFF == ord("q"):
#     #         break
    
#     # capture.release()
#     # cv2.destroyAllWindows()
    
#     pass


# def login_click():
#     print("login")

# def main(page: ft.Page):

#     page.title = "Login Project"
#     page.window.width = 500
#     page.window.height = 800

#     name_field = TextField(label="Username")
#     job_field = TextField(label="Job")


#     page.add(
#         Column(
#             margin=Margin.only(top=100),
#             controls=[
#                 Text("Login App", weight=FontWeight.BOLD, size=50),
#                 name_field, 
#                 job_field,
#                 Row(
#                     controls=[
#                         Button(
#                             "Register",
#                             bgcolor=Colors.ORANGE, 
#                             color=Colors.WHITE,
#                             on_click=register_click(name_field, job_field),
#                         ),
#                         Button(
#                             "Login",
#                             bgcolor=Colors.BLUE, 
#                             color=Colors.WHITE,
#                             on_click=login_click,
#                         ),
#                     ], alignment=MainAxisAlignment.CENTER, 
#                 ), 
#             ], horizontal_alignment=CrossAxisAlignment.CENTER,
#         )
#     )

# if __name__ == "__main__":
#     ft.run(main)