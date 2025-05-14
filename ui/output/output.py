import flet as ft
import pandas as pd


class Output:
    def __init__(self):
        self.scroll_column = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    def update_text(self, *update):
        current_output = []
        current_output.extend(update)
        text = ft.Text(
            '\n\n'.join(current_output),
            color=ft.Colors.GREEN_ACCENT_400,
            font_family="Courier New",
            size=18,
            selectable=True,
            expand=True,
        )
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(text)
        self.scroll_column.scroll_to(offset=-1, duration=300)
        self.scroll_column.update()

    def set_tables(self, data: dict):
        max_len = max(len(data['x_val']), len(data['var_val']))
        table = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(data['x_name']))] + [ft.DataColumn(
                        ft.Text(data['x_val'][i] if i < len(data['x_val']) else '', selectable=True, no_wrap=True,
                                max_lines=1)) for i in range(max_len)],
                    rows=[
                        ft.DataRow(
                            cells=[ft.DataCell(ft.Text(ind))] + [ft.DataCell(
                                ft.Text(str(row[i]) if i < len(row) else '', selectable=True, no_wrap=True,
                                        max_lines=1)) for i in range(max_len)]
                        )
                        for row, ind in ((data['func_val'], data['func_name']), (data['var_val'], data['var_name']),
                                         (data['fuc_var_val'], data['func_var']))
                    ],
                )
            ])
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(table)
        self.scroll_column.update()

    def set_tables_diff(self, data: dict):
        max_len = len(data['x_val'])
        table = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(data['x_name']))] + [ft.DataColumn(
                        ft.Text(data['x_val'][i] if i < len(data['x_val']) else '', selectable=True, no_wrap=True,
                                max_lines=1)) for i in range(max_len)],
                    rows=[
                        ft.DataRow(
                            cells=[ft.DataCell(ft.Text(ind))] + [ft.DataCell(
                                ft.Text(str(row[i]) if i < len(row) else '', selectable=True, no_wrap=True,
                                        max_lines=1)) for i in range(max_len)]
                        )
                        for row, ind in ((data['func_val'], data['func_name']),
                                         (data['analytics_val'], data['analytics_name']),
                                         (data['numeric_val'], data['numeric_name']))
                    ],
                )
            ])
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(table)
        self.scroll_column.update()
