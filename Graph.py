# Algorithmic Robotics and Motion Planning - Assignment no. 1
# Dvir Ben Asuli        318208816
# Tel-Aviv University   October 2021

from queue import Queue


class Node:
    counter = 0
    registry = {}

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None
        self.rid = str(x) + str(y) + str(z)
        Node.counter += 1

    def update_parent(self, c):
        self.parent = c

    def get_parent(self):
        return self.parent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neq__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __repr__(self):
        return f'{self.x} {self.y} {self.z}\n'


class Graph:
    # The Control Flow Graph, represented by its root node
    def __init__(self, root: Node, xy, yz, zx):
        self.root = root
        self.registry = {}
        self.registry[root.rid] = root
        self.xy_size = len(xy)
        self.yz_size = len(yz)
        self.zx_size = len(zx)
        self.queue = Queue(maxsize=len(xy) * len(yz) * len(zx))
        self.queue.put(root)

    def add_node(self, predecessor, x, y, z):
        node = Node(x, y, z)
        # Checking if the incoming and outgoing nodes already exist in the graph
        # If not create new ones
        if node.rid not in self.registry.keys():
            self.registry[node.rid] = node
            node.update_parent(predecessor)
            self.queue.put(node)
