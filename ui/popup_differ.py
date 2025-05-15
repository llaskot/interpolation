import flet as ft
import pandas as pd
import math

from ui.output.output import Output


class Popup_differ:
    def __init__(self, page, output: Output, graph):
        self.output = output
        self.graph = graph
        self.start = None
        self.h = None
        self.m = None
        self.func = None
        self.pares = 1
        # self.num_to_process = 1
        self.page = page
        self.dialog = None  # Пока нет попапа

        self.drp = ft.Dropdown(
            value="2",
            options=[
                ft.DropdownOption(key="1", text=' SIN(X) '),
                ft.DropdownOption(key="2", text=' EXP(-X) '),
            ],
        )

        self.values_fields = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(f'start'),
                            self.create_new_textfield(),
                            ft.Text(f'h = '),
                            self.create_new_textfield(),
                            ft.Text(f'M = '),
                            self.create_new_textfield(),
                            ft.Text(f'Function'),
                            self.drp

                        ]
                    )
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        self.desired_fields = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO
        )
        self.scroll_column = ft.Column(
            controls=[
                self.create_fields_column(),
                # self.val_buttons,
                ft.Text(''),
                # self.create_desired_column(),
                # self.desired_buttons
            ],
            scroll=ft.ScrollMode.AUTO
        )

    def f1(self, x):
        return math.sin(x)

    def f1_dif(self, x):
        return math.cos(x)

    def f2(self, x):
        return math.exp(-x)

    def f2_dif(self, x):
        return -math.exp(-x)

    def get_data(self):
        x = [self.start + i * self.h for i in range(self.m)]
        if self.func == "1":
            y = [self.f1(a) for a in x]
            dy = [self.f1_dif(a) for a in x]
        else:
            y = [self.f2(a) for a in x]
            dy = [self.f2_dif(a) for a in x]

        res = {
            'x_name': 'x',
            'func_name': 'f(x)',
            'x_val': x,
            'func_val': y,
            'analytics_name': f"f'(x) analytics",
            'numeric_name': f"f'(x) numeric",
            'analytics_val': dy,
        }
        res['numeric_val'] = [None for _ in range(len(res['analytics_val']))]
        print(res)
        self.page.result = res


    def open(self, e=None):  # e=None для вызова вручную
        self.create_popup()
        self.dialog.open = True
        self.page.update()

    def cancel(self, e):
        self.dialog.open = False
        self.page.update()
        self.dialog = None

    def create_fields_column(self):
        return self.values_fields


    def create_new_textfield(self):
        return ft.TextField(
            # value="0",
            width=70,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.InputFilter(
                regex_string=r"^-?\d*\.?\d*$",  # Разрешает: -, ., цифры
                allow=True,
                replacement_string=""  # Запрещает невалидные символы
            ),
            max_length=7,
            text_align=ft.TextAlign.CENTER,
            height=40,
            text_size=13,
            content_padding=ft.Padding(0, 4, 0, 0),

        )

    def create_popup(self):
        """Создает попап"""
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Fill in a data"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=
                        self.scroll_column,
                        padding=10,
                        width=600
                    )
                ],
                scroll=ft.ScrollMode.AUTO

            ),
            actions=[ft.TextButton("Confirm and close", on_click=self.close),
                     ft.TextButton("Cancel and close", on_click=self.cancel)],
            inset_padding=10,  # Убираем стандартные отступы AlertDialog

        )
        self.page.overlay.append(self.dialog)
        self.page.update()

    def collect_values(self, event):
        self.start = None
        self.h = None
        self.m = None
        row_container = self.values_fields.controls[0]
        self.start = float(row_container.content.controls[1].value)
        self.h = float(row_container.content.controls[3].value)
        self.m = int(row_container.content.controls[5].value)
        self.func = self.drp.value
        self.get_data()
        print('self.start =',self.start , 'self.h = ',self.h , 'self.m = ' ,self.m, 'self.func =', self.func)

    def close(self, e):
        self.collect_values(e)
        self.dialog.open = False
        self.page.update()
        self.dialog = None
        # self.page.result = self.get_result()
        self.graph.set_data(self.page.result, 'f(x)')
        self.graph.build_graph_diff()
        self.graph.set_img()
        # self.page.df = self.get_df()
        self.output.update_text('Data: f(x)')
        self.output.set_tables_diff(self.page.result)
