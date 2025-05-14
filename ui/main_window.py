import flet as ft

from ui.control.differentiation import Differentiation
from ui.control.interpolation import Interpolation
from ui.graph.grapf import Graph
from ui.output.output import Output


def main(page: ft.Page):
    page.title = "SLAE solutions"
    page.theme_mode = "dark"
    page.df = None
    page.result = None
    output = Output()
    graph = Graph('No name')
    graph.build_graph()
    interp = Interpolation(page, output, graph)
    differ = Differentiation(page, output, graph)
    # page.add(interp.file_picker)
    # page.add(differ.file_picker)

    res = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.BLUE_100,
                    # padding=10,
                    expand=True,
                    content=graph.img,
                ),
                ft.Container(
                    # bgcolor=ft.Colors.GREEN_100,
                    padding=10,
                    expand=True,
                    content=output.scroll_column,
                ),
            ]
        ),
        bgcolor=ft.Colors.GREY_900,
        padding=5,
        border_radius=5,
        expand=True
    )
    page.add(res)
    graph.set_img()

    control = ft.Container(
        content=ft.Row(
            controls=[
                differ.control
            ]
        ),
        bgcolor=ft.Colors.TEAL,
        padding=5,
        border_radius=5,
        height=250

    )

    page.add(control)


if __name__ == "__main__":
    ft.app(target=main)
