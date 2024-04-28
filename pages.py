import flet as ft
from datetime import date

def go(page: ft.Page):
    today = date.today()
    page.clean()

    def button_clicked(e):
        for control in lv.controls:
            control.disabled = True
        e.control.disabled = False
        page.update()

    lv = ft.ListView(expand=True, spacing=10)

    for i in range(10):
        b = ft.OutlinedButton(f"с {8+i}:00 до {9+i}:00", on_click=button_clicked, data=0)
        lv.controls.append(b)

    page.add(lv)

def home1(page: ft.Page):
    page.clean()
    time=["9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00",]
    def button_clicked(e):
        for control in lv.controls:
            control.disabled = True
        e.control.disabled = False
        page.update()


    lv = ft.ListView(expand=True, spacing=10)

    for i in range(10):
        b = ft.OutlinedButton(f"Забрать сегодня в {time[i]}", on_click=button_clicked, data=0)
        lv.controls.append(b)

    page.add(lv)


def test(page: ft.Page):
    page.clean()
    today = date.today()

    def button_clicked(e):
        for control in lv.controls:
            control.disabled = True
        e.control.disabled = False
        page.update()


    lv = ft.ListView(expand=True, spacing=10)

    for i in range(12):
        b = ft.OutlinedButton(f"Взять на тестдрайв с {today.strftime('%d.%m.%Y')} и вернуть через {i+1} месяц", on_click=button_clicked, data=0)
        lv.controls.append(b)

    page.add(lv)