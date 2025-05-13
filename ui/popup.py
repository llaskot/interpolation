import flet as ft


class Popup:
    def __init__(self, page):
        self.x_values: list = []
        self.y_values: list = []
        self.big_x_values: list = []
        self.pares = 3
        self.num_to_process = 1
        self.page = page
        self.dialog = None  # Пока нет попапа
        self.values_fields = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO
        )
        self.desired_fields = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO
        )
        self.val_buttons = ft.Row(
            controls=[
                ft.ElevatedButton('Add', on_click=self.add_row),
                ft.ElevatedButton('Remove', on_click=self.remove_row)
            ]
        )
        self.desired_buttons = ft.Row(
            controls=[
                ft.ElevatedButton('Add', on_click=self.add_x),
                ft.ElevatedButton('Remove', on_click=self.remove_x)
            ]
        )

    def get_result(self):
        all_x, all_y = zip(*sorted(zip(self.x_values, self.y_values)))
        self.x_values = list(all_x)
        self.y_values = list(all_y)
        self.big_x_values.sort()
        res = {
            'x_name': 'x',
            'func_name': 'f(x)',
            'x_val': self.x_values,
            'func_val': self.y_values,
            'var_name': 'X',
            'func_var': f'f(X)',
            'var_val': self.big_x_values,
        }
        res['fuc_var_val'] = [None for _ in range(len(res['var_val']))]
        return res

    def add_x(self, event):
        self.x_to_process_append(self.num_to_process)
        self.desired_fields.update()
        self.num_to_process += 1

    def remove_x(self, event):
        self.desired_fields.controls.pop()
        self.desired_fields.update()
        self.num_to_process -= 1

    def add_row(self, event):
        self.pare_row_append(self.pares)
        self.values_fields.update()
        self.pares += 1

    def remove_row(self, event):
        self.values_fields.controls.pop()
        self.values_fields.update()
        self.pares -= 1

    def open(self, e=None):  # e=None для вызова вручную
        self.create_popup()
        self.dialog.open = True
        self.page.update()

    def cancel(self, e):
        self.dialog.open = False
        self.page.update()
        self.dialog = None

    def create_fields_column(self):
        for i in range(self.pares):
            self.pare_row_append(i)
        return self.values_fields

    def pare_row_append(self, ind: int):
        pare_row = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f'x{ind}'),
                    self.create_new_textfield(),
                    ft.Text(f'f(x{ind})'),
                    self.create_new_textfield(),
                ]
            )
        )
        self.values_fields.controls.append(pare_row)

    def create_desired_column(self):
        for i in range(self.num_to_process):
            self.x_to_process_append(i)
        return self.desired_fields

    def x_to_process_append(self, ind: int):
        pare_row = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f'X{ind}'),
                    self.create_new_textfield(),
                ]
            )
        )
        self.desired_fields.controls.append(pare_row)

    def create_new_textfield(self):
        return ft.TextField(
            # value="0",
            width=60,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.InputFilter(
                regex_string=r"^-?\d*\.?\d*$",  # Разрешает: -, ., цифры
                allow=True,
                replacement_string=""  # Запрещает невалидные символы
            ),
            max_length=7,
            text_align=ft.TextAlign.CENTER,
            height=30,
            text_size=13,
            content_padding=ft.Padding(0, 4, 0, 0)
        )

    def create_popup(self):
        """Создает попап"""
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("fill in a minimum data"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text('Given values, minimum 3 pares:'),
                                self.create_fields_column(),
                                self.val_buttons,
                                ft.Text('X to process, minimum 1 value:'),
                                self.create_desired_column(),
                                self.desired_buttons
                            ],
                            scroll=ft.ScrollMode.AUTO

                        )

                        ,
                        # width=147 * self.matrix_len,
                        padding=0
                    )
                ],
                scroll=ft.ScrollMode.AUTO
            ),
            actions=[ft.TextButton("Confirm and close", on_click=self.close),
                     ft.TextButton("Cancel and close", )],
            inset_padding=0,  # Убираем стандартные отступы AlertDialog
        )
        self.page.overlay.append(self.dialog)
        self.page.update()

    def collect_values(self, event):
        self.x_values.clear()
        self.y_values.clear()
        self.big_x_values.clear()
        for row_container in self.values_fields.controls:
            x = row_container.content.controls[1].value
            self.x_values.append(float(x if x != '' else 0.0))
            y = row_container.content.controls[3].value
            self.y_values.append(float(y) if y != '' else 0.0)
        for row_container in self.desired_fields.controls:
            x = row_container.content.controls[1].value
            self.big_x_values.append(float(x if x != '' else 0.0))

    # def create_matrix(self):
    #     self.field_names.clear()
    #     for i in range(self.matrix_len):
    #
    #         temp = []
    #         for j in range(self.matrix_len):
    #             temp.append(f'{i}X{j + 1}')
    #         temp.append(f'{i}res')
    #
    #         self.field_names.append(temp)

    # def get_field_values(self):
    #     """
    #     gets matrix from popup
    #     :return: [[]]
    #     """
    #     self.matrix.clear()
    #
    #     for i in range(self.matrix_len):
    #         res = []
    #         for name in self.field_names[i]:
    #             try:
    #                 res.append(Fraction(self.fields[name].value))
    #             except ValueError as e:
    #                 print(e)
    #             except IndexError as e:
    #                 print(e)
    #         self.matrix.append(res)

    def close(self, e):
        self.collect_values(e)
        self.dialog.open = False
        self.page.update()
        self.dialog = None
