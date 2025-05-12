import time

import flet as ft

from data_process.interpolation_process import Interpolation_process
from file_process.excel_process import Excel_process
from ui.graph.grapf import Graph


class Interpolation:
    def __init__(self, page, output, graph):
        self.page = page
        self.output = output
        self.graph = graph
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.file_picker_result
        self.btn_select_file = ft.IconButton(ft.Icons.FOLDER, on_click=self.pick_file)
        self.btn_manual_input = ft.IconButton(ft.Icons.KEYBOARD)

        self.control = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text('Select file'),
                                            self.btn_select_file,
                                        ]
                                    )
                                ),

                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Text('Manual input'),
                                            self.btn_manual_input,
                                        ]
                                    )
                                )

                            ]
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ElevatedButton('Lagrange'),
                                ft.ElevatedButton('Newton'),
                            ]
                        )
                    )
                ]
            )

        )

    def pick_file(self, event):
        self.file_picker.pick_files()

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            print(selected_file)
            exl = Excel_process(selected_file)
            a = exl.read_xls()
            self.output.update_text(f'Data: {a["func_name"]}')
            self.output.set_table(exl.df)
            self.graph.set_data('Inter', a)
            self.graph.build_graph()
            self.graph.set_img()
            b = Interpolation_process(a)
            b.process_lagrange()
            time.sleep(1.5)
            self.graph.set_data('new', b.data)
            self.graph.build_graph()
            self.graph.set_img()





