from file_process.excel_process import Excel_process
from ui.control.interpolation import Interpolation
from ui.output.output import Output


class Differentiation(Interpolation):
    def __init__(self, page, output: Output, graph):
        super().__init__(page, output, graph)

    def file_picker_result(self, event):
        if event.files:
            selected_file = event.files[0]
            exl = Excel_process(selected_file)
            self.page.result = exl.read_xls_diff()
            # self.page.df = exl.df
            self.output.update_text(f'Data: {self.page.result["func_name"]}')
            self.output.set_tables_diff(self.page.result)
            self.graph.set_data(self.page.result, self.page.result["func_name"])
            self.graph.build_graph_diff()
            self.graph.set_img()

