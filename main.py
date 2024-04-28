import flet as ft
import json
import shelters
import functions

class Save:
    def __init__(self):
        self.userdata = self.load_data()

    def load_data(self):
        try:
            with open('userbase.json', 'r') as file:
                dataclass = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            dataclass = {}
        return dataclass

    def save_data(self):
        with open('userbase.json', 'w') as file:
            json.dump(self.userdata, file)

def main(page: ft.Page):
    save = Save()
    sign_status = False
    page.scroll = "adaptive"


    name = ft.TextField(label="Ваше имя", autofocus=True)
    password = ft.TextField(label="Пароль", password=True, can_reveal_password=True)
    greetings = ft.Column()
    name_info = ft.TextField(label="Ваше имя", read_only=True, visible=True, width=500)
    password_info = ft.TextField(label="Ваш пароль", read_only=True, password=True, can_reveal_password=True, visible=True, width=500)

    def info(e):
        page.controls.clear()
        text_info = ('Мы команда из трёх человек, учащихся 7-го класса, а также ЦДНИТТ при КузГТУ "УникУм".\n Этот проект направлен на поддержку наших четвероногих друзей.\n'
                     'Помощь может быть самая разная: от пожертвования денежных средств до "тест-драйва жизни с питомцем" и обязательства взять всё обеспечение будущего члена семьи под свой контроль.\n')
        about_us = ft.TextField(label="О нас", value=str(text_info), read_only=True, multiline=True)
        page.add(
            about_us,
            ft.IconButton(ft.icons.ARROW_LEFT, on_click=profile)
        )
        page.update()

    def shelters(e):
        Progect.shelters(page)

    def admin(e):
        page.controls.clear()
        Progect.shelters(page)
        Progect.admin(page)
        page.update()

    def reg(e):
        if name.value == "" or password.value == "":
            greetings.controls.append(ft.Text("Имя или пароль не могут быть пустыми!"))
        save.userdata[name.value] = password.value
        save.save_data()
        greetings.controls.append(ft.Text(f"Вы зарегистрировались как {name.value}!"))
        name.value = ""
        password.value = ""
        page.update()
        name.focus()

    def sign_in(e):
        if name.value in save.userdata and save.userdata[name.value] == password.value:
            global sign_status
            sign_status = True
            profile(e)
            name_info.value = str(name.value)
            password_info.value = str(password.value)
        elif name.value == "admin" and password.value == "admin_panel_run":
            admin(page)
        elif name.value == "" or password.value == "":
            greetings.controls.append(ft.Text("Имя или пароль не могут быть пустыми!"))
        else:
            greetings.controls.append(ft.Text("Неверное имя или пароль!"))
            name.value = ""
            password.value = ""
            name.focus()
        page.update()

    def reg_menu(e):
        global sign_status
        sign_status = False
        page.controls.clear()
        page.add(
            name,
            password,
            ft.ElevatedButton("Зарегистрироваться?", on_click=reg),
            ft.ElevatedButton("Войти?", on_click=sign_in),
            greetings,
        )
        name.value = ""
        password.value = ""
        name.focus()
        page.update()

    def on_destination_click(e):
        index = page.navigation_bar.selected_index
        if index == 0:
            profile(e)
            page.update()
        elif index == 1:
            page.controls.clear()
            shelters(e)
            page.update()

        greetings.controls.clear()
        page.update()

    def profile(e):
        page.controls.clear()
        page.add(
            name_info,
            password_info,
            ft.ElevatedButton("Выйти?", on_click=sign_out),
            ft.ElevatedButton("О нас", on_click=info),
            greetings,
        )
        page.navigation_bar = ft.NavigationBar(
            on_change=on_destination_click,
            destinations=[
                ft.NavigationDestination(icon=ft.icons.ACCOUNT_CIRCLE, label="Аккаунт"),
                ft.NavigationDestination(icon=ft.icons.PETS, label="Приюты"),
            ]
        )
        greetings.controls.append(ft.Text(f"Вы вошли как {str(name.value)}!"))
        page.update()

    def sign_out(e):
        reg_menu(e)
        page._clean(page.navigation_bar)

    page.add(
        name,
        password,
        ft.ElevatedButton("Зарегистрироваться?", on_click=reg),
        ft.ElevatedButton("Войти?", on_click=sign_in),
        greetings,
    )
ft.app(target=main)
