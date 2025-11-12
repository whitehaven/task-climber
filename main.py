from dataclasses import dataclass
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import pytest


@dataclass
class Tasklist:
    task_graph: nx.DiGraph

    def __init__(self, task_graph: nx.DiGraph | None = None):
        if task_graph is None:
            self.task_graph = nx.DiGraph()
        else:
            self.task_graph = task_graph

    def add_task_run(self, task_run: list[str]):
        for i in range(len(task_run) - 1):
            self.task_graph.add_edge(task_run[i], task_run[i + 1])

    def draw_task_dependency_tree(self):
        pos = graphviz_layout(self.task_graph, prog="dot")
        nx.draw(
            self.task_graph,
            pos,
            with_labels=True,
            font_size=10,
        )
        plt.margins(0.2)
        plt.show()

    def get_task_dependency_tree(self):
        return self.task_graph

    def get_available_tasks(self) -> list[str]:
        return [node for node, degree in self.task_graph.in_degree() if degree == 0]

    def get_random_task_to_get_started(self) -> str:
        import random
        return random.choice(self.get_available_tasks())
