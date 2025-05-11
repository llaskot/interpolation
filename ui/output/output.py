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

    def set_table(self, df: pd.DataFrame):
        table = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(val, selectable=True, no_wrap=True, max_lines=1)) for val in
                             df.values.tolist()[0]],
                    rows=[
                        ft.DataRow(
                            cells=[ft.DataCell(ft.Text(str(cell), selectable=True, no_wrap=True, max_lines=1)) for cell
                                   in
                                   row]
                        )
                        for row in df.values.tolist()[1:]
                    ],
                )
            ])
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(table)
        self.scroll_column.update()
