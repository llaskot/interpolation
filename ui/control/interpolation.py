import time

import flet as ft

from data_process.interpolation_process import Interpolation_process
from file_process.excel_process import Excel_process
from ui.graph.grapf import Graph
from ui.output.output import Output
from ui.popup import Popup


class Interpolation:
    def __init__(self, page, output: Output, graph):
        self.page = page
        self.output = output
        self.graph = graph
        self.file_picker = ft.FilePicker()
        self.file_picker.on_result = self.file_picker_result
        self.btn_select_file = ft.IconButton(ft.Icons.FOLDER, on_click=self.pick_file)
        self.btn_manual_input = ft.IconButton(ft.Icons.KEYBOARD, on_click=self.open_popup)
        self.page.add(self.file_picker)

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
                                ft.ElevatedButton('Lagrange', on_click=self.process_lagrange),
                                ft.ElevatedButton('Newton', on_click=self.process_newton),
                            ]
                        )
                    )
                ]
            )

        )

    def process_lagrange(self, event):
        interp = Interpolation_process(self.page.result)
        # print(interp.data)
        interp.process_lagrange()
        self.output.update_text(f'Data: Lagrange f(x) + f(X)')
        self.output.set_tables(self.page.result)
        self.graph.set_data(interp.data, 'Lagrange f(x) + f(x,X)')
        self.graph.build_graph()
        self.graph.set_img()

    def process_newton(self, event):
        interp = Interpolation_process(self.page.result)
        # print(interp.data)
        interp.process_newton()
        self.output.update_text(f'Data: Newton f(x) + f(X)')
        self.output.set_tables(self.page.result)
        self.graph.set_data(interp.data, 'Newton f(x) + f(x,X)')
        self.graph.build_graph()
        self.graph.set_img()

    def pick_file(self, event):
        self.file_picker.pick_files()

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            exl = Excel_process(selected_file)
            self.page.result = exl.read_xls()
            # self.page.df = exl.df
            self.output.update_text(f'Data: {self.page.result["func_name"]}')
            self.output.set_tables(self.page.result)
            self.graph.set_data(self.page.result, self.page.result["func_name"])
            self.graph.build_graph()
            self.graph.set_img()

    def open_popup(self, event):
        popup = Popup(self.page, self.output, self.graph)
        popup.open()
