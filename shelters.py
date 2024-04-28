import flet as ft
import random
import calendar
from datetime import date, timedelta
import pages
import json

class Save:
    def __init__(self):
        self.shelterdata = self.load_data()

    def load_data(self):
        try:
            with open('imagebase.json', 'r') as file:
                dataclass = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            dataclass = {}
        return dataclass

    def save_data(self):
        for data in self.shelterdata:
            if isinstance(data, ft.Image):
                self.shelterdata[data] = data.src
        with open('imagebase.json', 'w') as file:
            json.dump(self.shelterdata, file)

class SaveText:
    def __init__(self):
        self.textdata = self.load_data()

    def load_data(self):
        try:
            with open('shelterbase.json', 'r') as file:
                textclass = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            textclass = {}
        return textclass

    def save_data(self):
        with open('shelterbase.json', 'w+') as file:
            json.dump(self.textdata, file)

save = Save()
save_text = SaveText()
def shelters(page: ft.Page):

    img = ft.Image(
        src=f"https://i.otzovik.com/objects/b/1200000/1192539.png",
        width=220,
        height=220,
        fit=ft.ImageFit.CONTAIN,
    )

    img2 = ft.Image(
        src=f"https://avatars.mds.yandex.net/get-altay/3933982/2a00000175d47c9330f32c7061582117dbb6/XXL_height",

        width=270,
        height=280,
        fit=ft.ImageFit.CONTAIN,
    )

    def dogs_lists(e):
        page.clean()
        page.add(
            ft.Row([ft.CircleAvatar(ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Image("https://avatars.mds.yandex.net/get-entity_search/937587/877439466/S122x122Smart_2x"),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="Прогуляться",
                        is_default_action=True,
                        trailing_icon=ft.icons.FMD_GOOD,
                        on_click=lambda e: F.go(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Тест-драйв",
                        trailing_icon=ft.icons.AUTO_MODE,
                        on_click=lambda e: F.test(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Забрать",
                        is_destructive_action=True,
                        trailing_icon=ft.icons.HOME,
                        on_click=lambda e: F.home1(page),
                    ),
                ],
            ), radius=70),
                ft.Column([
                    ft.Text('Питомец 0.', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Лабрадоры используются на охоте, в качестве собак-поводырей, собак-спасателей, но главным образом в роли компаньонов.'),

                ])]), ft.Column([ft.Text(' ')]),
            ft.Row([ft.CircleAvatar(ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Image("https://avatars.mds.yandex.net/get-entity_search/1540656/806578245/S122x122Smart_2x"),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="Прогуляться",
                        is_default_action=True,
                        trailing_icon=ft.icons.FMD_GOOD,
                        on_click=lambda e: F.go(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Тест-драйв",
                        trailing_icon=ft.icons.AUTO_MODE,
                        on_click=lambda e: F.test(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Забрать",
                        is_destructive_action=True,
                        trailing_icon=ft.icons.HOME,
                        on_click=lambda e: F.home1(page),
                    ),
                ],
            ), radius=70),
                ft.Column([
                    ft.Text('Питомец 1.', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Это аборигенная порода, не являющаяся результатом планомерного отбора. \nИсторически используется среднеазиатскими народами и чабанами для охраны скота.'),
                ])]), ft.Column([ft.Text(' ')]),
            ft.Row([
                ft.CircleAvatar(ft.CupertinoContextMenu(
                    enable_haptic_feedback=True,
                    content=ft.Image(
                        "https://avatars.mds.yandex.net/get-entity_search/5503081/777345428/S122x122Smart_2x"),
                    actions=[
                        ft.CupertinoContextMenuAction(
                            text="Прогуляться",
                            is_default_action=True,
                            trailing_icon=ft.icons.FMD_GOOD,
                            on_click=lambda e: F.go(page),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Тест-драйв",
                            trailing_icon=ft.icons.AUTO_MODE,
                            on_click=lambda e: F.test(page),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Забрать",
                            is_destructive_action=True,
                            trailing_icon=ft.icons.HOME,
                            on_click=lambda e: F.home1(page),
                        ),
                    ],
                ), radius=70),
                ft.Column([
                    ft.Text('Питомец 2.', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Бультерьеры весьма доброжелательны и преданны, если их правильно воспитать. \nЭти собаки чрезмерно активны и нуждаются в регулярных физических нагрузках, где они смогут выплеснуть свою энергию.'),
                ])]))

    def dogs_list(e):
        page.clean()
        page.add(

            ft.Row([ft.CircleAvatar(ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Image("https://avatars.mds.yandex.net/get-entity_search/2102351/886036195/S122x122Smart_2x"),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="Прогуляться",
                        is_default_action=True,
                        trailing_icon=ft.icons.FMD_GOOD,
                        on_click=lambda e: F.go(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Тест-драйв",
                        trailing_icon=ft.icons.AUTO_MODE,
                        on_click=lambda e: F.test(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Забрать",
                        is_destructive_action=True,
                        trailing_icon=ft.icons.HOME,
                        on_click=lambda e: F.home1(page),
                    ),
                ],
            ), radius=70),
                ft.Column([
                    ft.Text('Питомец 0.', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Это собака среднего размера с типичным обликом гончей. \nБигли обладают хорошим обонянием и используются прежде всего для охоты на кроликов и зайцев.'),

                ])]), ft.Column([ft.Text(' ')]),
            ft.Row([ft.CircleAvatar(ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Image("https://avatars.mds.yandex.net/get-entity_search/1554108/877776638/S122x122Smart_2x"),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="Прогуляться",
                        is_default_action=True,
                        trailing_icon=ft.icons.FMD_GOOD,
                        on_click=lambda e: F.go(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Тест-драйв",
                        trailing_icon=ft.icons.AUTO_MODE,
                        on_click=lambda e: F.test(page),
                    ),
                    ft.CupertinoContextMenuAction(
                        text="Забрать",
                        is_destructive_action=True,
                        trailing_icon=ft.icons.HOME,
                        on_click=lambda e: F.home1(page),
                    ),
                ],
            ), radius=70),
                ft.Column([
                    ft.Text('Питомец 1.', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Это самая мелкая из шести пород исконно японского происхождения. \nВ 1936 году сиба-ину была объявлена национальным достоянием Японии, где основное поголовье этих собак находится в деревнях.'),
                ])]), ft.Column([ft.Text(' ')]),
            ft.Row([
                ft.CircleAvatar(ft.CupertinoContextMenu(
                    enable_haptic_feedback=True,
                    content=ft.Image(
                        "https://avatars.mds.yandex.net/get-entity_search/96437/779608743/S122x122Smart_2x"),
                    actions=[
                        ft.CupertinoContextMenuAction(
                            text="Прогуляться",
                            is_default_action=True,
                            trailing_icon=ft.icons.FMD_GOOD,
                            on_click=lambda e: F.go(page),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Тест-драйв",
                            trailing_icon=ft.icons.AUTO_MODE,
                            on_click=lambda e: F.test(page),
                        ),
                        ft.CupertinoContextMenuAction(
                            text="Забрать",
                            is_destructive_action=True,
                            trailing_icon=ft.icons.HOME,
                            on_click=lambda e: F.home1(page),
                        ),
                    ],
                ), radius=70),
                ft.Column([
                    ft.Text('Питомец 2', theme_style=ft.TextThemeStyle.LABEL_LARGE),

                    ft.Text(
                        'Доберманы отличаются активным, энергичным характером, склонны к проявлению агрессии. \nОбладают выраженным охранным инстинктом, как территориальным, так и направленным на охрану человека.'),
                ])]))

    page.add(ft.Row([ft.Row(
        [
            img, ]
    ),
        ft.Row(
            [ft.Column([
                ft.Row(
                    [ft.Text('     '), ft.Text(f'Приют "Верный"', size=15, weight=ft.FontWeight.W_600), ]),
                ft.Row([
                    ft.Container(ft.Text("Описание приюта")), ]),
                ft.Row([
                    ft.Text(f'Адрес:', theme_style=ft.TextThemeStyle.TITLE_SMALL), ft.Text('ул. 40 лет Октября'),
                ]),
                ft.Row([
                    ft.Text('Ссылка на ВК:', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                    ft.TextButton('Тут', url='https://vk.com/priyut42?ysclid=lvg8phd67i799200002')
                ]),
                ft.TextButton(text='Подробнее', on_click=dogs_lists),
                ft.TextButton(text='Пожертвование')
            ])], alignment=ft.MainAxisAlignment.START),

        ft.Row(
            [
                img2, ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.Column([
                ft.Row(
                    [ft.Text('     '), ft.Text(f'Приют "Верный"', size=15, weight=ft.FontWeight.W_600), ]),
                ft.Row([
                    ft.Container(ft.Text("Описание приюта")), ]),
                ft.Row([
                    ft.Text(f'Адрес:', theme_style=ft.TextThemeStyle.TITLE_SMALL), ft.Text('ул. 40 лет Октября'),
                ]),
                ft.Row([
                    ft.Text('Ссылка на ВК:', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                    ft.TextButton('Тут', url='https://vk.com/priyut42?ysclid=lvg8phd67i799200002')
                ]),
                ft.TextButton(text='Подробнее', on_click=dogs_list),
                ft.TextButton(text='Пожертвование')
            ])], alignment=ft.MainAxisAlignment.CENTER)]))

    try:
        page.add(ft.Image(save.shelterdata["img_shelter"]))
    except KeyError:
        page.add(ft.Text("Изображение пока недоступно"))

    for data in save_text.textdata:
        page.add(ft.Text(f"{data}: {save_text.textdata[data]}"))

def admin(page:ft.Page):
    name_shelter = ft.TextField(label="Введите название нового приюта")
    adress_shelter = ft.TextField(label="Введите адрес нового приюта")
    adress_img = ft.TextField(label="Вставьте путь до фотографии для нового приюта")

    def add_shelter(e):
        img_shelter = ft.Image(src=adress_img.value, width=220, height=220, fit=ft.ImageFit.CONTAIN)
        page.add(ft.Row([ft.Row(
            [
                img_shelter,
            ],
        ),
            ft.Row(
                [ft.Column([
                    ft.Row(
                        [ft.Text('     '), ft.Text(name_shelter.value), ]),
                    ft.Row([
                        ft.Container(ft.Text("")),
                    ]),
                    ft.Row([
                        ft.Text(f'Адрес:', theme_style=ft.TextThemeStyle.TITLE_SMALL),
                        ft.Text(adress_shelter.value),
                    ]),
                    # ft.TextButton(text='Подробнее', on_click=dogs_lists),
                    # ft.TextButton(text='Пожертвование', on_click=don)
                ], alignment=ft.MainAxisAlignment.START),  # Закрываем список в ft.Column
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),  # Закрываем список в ft.Row
        ]))  # Закрываем список в ft.Row и функцию add_shelter

        # Save the necessary data to shelterdata
        save.shelterdata = {
            "img_shelter": adress_img.value,
        }
        save.save_data()
        save_text.textdata = {
            "name_shelter": name_shelter.value,
            "adress_shelter": adress_shelter.value
        }

    page.add(name_shelter, adress_shelter, adress_img, ft.IconButton(icon=ft.icons.ADD, on_click=add_shelter))