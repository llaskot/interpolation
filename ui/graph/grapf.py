import os
import time
from copy import copy

import matplotlib
import flet as ft

matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, name, data=None):
        self.img = None
        if data is None:
            data = {'x_name': 'x', 'func_name': 'f(x)', 'x_val': [1, 10],
                    'func_val': [1, 10], 'var_name': 'X', 'func_var': 'f(X)',
                    'var_val': [None], 'fuc_var_val': [None]}
        self.data = data
        self.x = data['x_val']
        self.y = data['func_val']
        self.x_name = data['x_name']
        self.y_name = data['func_name']
        self.X = data['var_val']
        self.Y = data['fuc_var_val']
        self.x_name = data['var_name']
        self.y_name = data['func_var']
        self.graph_name = name
        self.dir_path = self.build_dir_path()
        self.save_path = None
        self.img = ft.Container(
            content=ft.Image(
                src=self.save_path,
                fit=ft.ImageFit.CONTAIN,
                expand=True
            ))

    def set_img(self):
        self.img.content = None
        self.img.content = ft.Image(
            src=self.save_path,
            fit=ft.ImageFit.CONTAIN,
            expand=True
        )
        self.img.update()

    def set_data(self, name, data):
        self.graph_name = name
        self.img.content = None
        self.data = data
        self.x = data['x_val']
        self.y = data['func_val']
        self.X = data['var_val']
        self.Y = data['fuc_var_val']
        # self.build_graph()
        # self.set_img()

    def build_path(self):
        self.save_path = os.path.join(self.dir_path, f"graph_{int(time.time())}.png")

    def build_dir_path(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
        return os.path.join(project_root, "ui", "graph")

    def build_graph(self):
        plt.figure(facecolor='black', figsize=(20.05, 12))
        ax = plt.gca()
        ax.set_facecolor('black')
        ax.tick_params(colors='white', labelsize=18)
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_size(18)

        # plt.plot(self.x, self.y, label=f'Graph {self.y_name}', color="blue")
        # plt.plot(x, y2, label="Вторая строка", color="green")

        plt.plot(
            self.x,
            self.y,
            label=f'Graph {self.y_name}',
            color='#1f77b4',
            marker='o',
            linewidth=6,  # толщина линии
            markersize=20  # размер точек
        )
        print('self.Y[0] = ', self.Y[0])
        if self.Y[0]:
            second_graph = self.merge_data()
            plt.plot(
                second_graph[0],
                second_graph[1],
                label=f'Graph {self.y_name}',
                color='red',
                marker='o',
                linewidth=1,  # толщина линии
                markersize=10  # размер точек
            )

        for xi, yi in zip(self.x, self.y):
            plt.axvline(x=xi, color='blue', linestyle='--', linewidth=0.5)
            plt.axhline(y=yi, color='blue', linestyle='--', linewidth=0.5)  # проекции на оси

        plt.xlabel(self.x_name)
        plt.ylabel(self.y_name)
        plt.title(self.graph_name)
        ax.title.set_size(30)
        plt.legend()
        plt.legend(fontsize=18)
        # plt.grid(True)
        # plt.show()
        for file in os.listdir(self.dir_path):
            if file.endswith(".png"):
                self.img.content = None
                os.remove(os.path.join(self.dir_path, file))
        self.build_path()
        plt.savefig(self.save_path, dpi=300, bbox_inches='tight')
        plt.close()

    def merge_data(self):
        all_x = self.x + self.X
        all_y = self.y + self.Y
        all_x, all_y = zip(*sorted(zip(all_x, all_y)))
        return all_x, all_y
