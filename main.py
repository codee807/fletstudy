import flet as ft

def main(page: ft.Page):
    page.title = "我的刷题App"
    page.add(ft.Text("Hello, 世界！打包成功！", size=30))

ft.app(target=main)
