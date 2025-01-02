"""
for educational purpose
"""

__author__ = "alunkeit"
__description__ = "A sample implementation of Dijkstra's algorithm"

from typing import List


class Node:
    """
    Represents a node in the graph. A node is a helper object for modeling graphs
    """

    def __init__(self, name: str):
        self.name = name
        self.distance = None
        self.predecessor = None

    def name(self):
        return self.name

    def __str__(self):
        return f"{self.name}: distance: {self.distance}"


class DirectedEdge:
    """
    Represents a directed edge in the graph
    """

    def __init__(self, node1: Node, node2: Node, weight=1):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        return f"{self.node1}: {self.node2}: {self.weight}"


def dijkstra(s: Node, t: Node, graph: List[DirectedEdge]) -> int:
    """
    A version of the Dijkstra algorithm
    :param s: the node to start from
    :param graph: edges to traverse
    :return: the distance traveled between s and t
    """
    target_nodes = [s]
    temp = s
    while len(target_nodes) > 0:
        for edge in graph:
            if edge.node1 == temp:
                target_node = edge.node2
                if target_node not in target_nodes:
                    target_nodes.append(target_node)
                if target_node.distance is None or target_node.distance > edge.weight:
                    target_node.distance = edge.weight
                    target_node.predecessor = edge.node1
        temp = target_nodes.pop(0)

    iter_node = t
    distance = 0
    while iter_node is not s:
        distance = distance + iter_node.distance
        iter_node = iter_node.predecessor
    return distance


if __name__ == "__main__":
    nodes = {"Frankfurt": Node(name="Frankfurt"),
             "Karlsruhe": Node(name="Karlsruhe"),
             "Mannheim": Node(name="Mannheim"),
             "Stuttgart": Node(name="Stuttgart"),
             "Würzburg": Node(name="Würzburg"),
             "Kassel": Node(name="Kassel"),
             "Nürnberg": Node(name="Nürnberg"),
             "Erfurt": Node(name="Erfurt"),
             "Augsburg": Node(name="Augsburg"),
             "München": Node(name="München")}

    edges = [DirectedEdge(nodes["Frankfurt"], nodes["Mannheim"], 85),
             DirectedEdge(nodes["Frankfurt"], nodes["Kassel"], 173),
             DirectedEdge(nodes["Mannheim"], nodes["Karlsruhe"], 80),
             DirectedEdge(nodes["Frankfurt"], nodes["Würzburg"], 217),
             DirectedEdge(nodes["Nürnberg"], nodes["Stuttgart"], 183),
             DirectedEdge(nodes["Würzburg"], nodes["Erfurt"], 186),
             DirectedEdge(nodes["Würzburg"], nodes["Nürnberg"], 103),
             DirectedEdge(nodes["Karlsruhe"], nodes["Augsburg"], 250),
             DirectedEdge(nodes["Augsburg"], nodes["München"], 84),
             DirectedEdge(nodes["Nürnberg"], nodes["München"], 167),
             DirectedEdge(nodes["Kassel"], nodes["München"], 502)]

    nodes["Frankfurt"].distance = 0

    dist = dijkstra(s=nodes["Frankfurt"], t=nodes["München"], graph=edges)
    print(f"dist : {dist}")
