from data_process.differentiation_process import Differentiation_process
from file_process.excel_process import Excel_process
from ui.control.interpolation import Interpolation
from ui.output.output import Output
import flet as ft

from ui.popup_differ import Popup_differ


class Differentiation(Interpolation):
    def __init__(self, page, output: Output, graph):
        super().__init__(page, output, graph)

    def get_buttons(self):
        return [
            ft.ElevatedButton('Interpolation', on_click=self.process_interp),
            ft.ElevatedButton('Approximation', on_click=self.process_approximation),
        ]

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            exl = Excel_process(selected_file)
            self.page.result = exl.read_xls_diff()
            self.output.update_text(f'Data: {self.page.result["func_name"]}')
            self.output.set_tables_diff(self.page.result)
            self.graph.set_data(self.page.result, self.page.result["func_name"])
            self.graph.build_graph_diff()
            self.graph.set_img()

    def process_approximation(self, event):
        interp = Differentiation_process(self.page.result)
        # print(interp.data)
        interp.get_approximation_differential()
        self.output.update_text(f'Approximation method')
        self.output.set_tables_diff(self.page.result)
        self.graph.set_data(interp.data, "f'(x) approximation method")
        self.graph.build_graph_diff()
        self.graph.set_img()

    def process_interp(self, event):
        interp = Differentiation_process(self.page.result)
        # print(interp.data)
        interp.get_interp_differential()
        self.output.update_text(f'Interpolation method')
        self.output.set_tables_diff(self.page.result)
        self.graph.set_data(interp.data, "f'(x) Interpolation method")
        self.graph.build_graph_diff()
        self.graph.set_img()

    def open_popup(self, event):
        popup = Popup_differ(self.page, self.output, self.graph)
        popup.open()
