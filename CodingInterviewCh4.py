from queue import Queue


class Graph:
    def __init__(self):
        self.max_size = 6
        self.vertices = list()
        self.size = 0

    def add_vertice(self, x):
        if self.size < self.max_size:
            self.vertices.append(x)
            self.size += 1

    def get_nodes(self):
        return self.vertices


class DirectedEdge:
    def __init__(self,to_node,cost):
        self.to_node = to_node
        self.weight = cost


class Node:
    def __init__(self,val):
        self.edge_list = list()
        self.value = val
        self.visited = False

    def add_edge(self,e : DirectedEdge):
        self.edge_list.append(e)

    def get_edges(self):
        return self.edge_list

    def get_val(self):
        return self.value


class BTNode:
    def __init__(self,val):
        self.left_child = None
        self.right_child = None
        self.value = val


def problem41_pathfinder(initial:Node,goal:Node):
    my_q = Queue()
    my_q.put(initial)

    while not my_q.empty():
        current = my_q.get()
        for edge in current.edge_list:
            if edge.to_node == goal:
                return True
            if not edge.to_node.visited:
                edge.to_node.visited = True
                my_q.put(edge.to_node)
    return False


def problem42_minimaltree(array: list):
    if len(array) == 1:
        return BTNode(array[0])

    mid = len(array)/2
    node = BTNode(array[mid])
    node.left_child = problem42_minimaltree(array[:mid])
    node.right_child = problem42_minimaltree(array[mid+1:])
    return node

from CodingInterviewCh2 import LinkedList

def problem43_listofdepths(node: BTNode,depth=0):





