# Algorithmic Robotics and Motion Planning - Assignment no. 1
# Dvir Ben Asuli        318208816
# Tel-Aviv University   October 2021

from Graph import Graph, Node
from InstructionParser import instruction_parser
from Scanner import Response, scan_cube, vacant_spot, track_path


class Main():
    def __init__(self):
        self.program = input("Enter arguments: ")

    def run(self):

        ## Receiving all the parameters from input
        source, destination, xy_mat, yz_mat, zx_mat = instruction_parser(self.program)

        sx = source[0]
        sy = source[1]
        sz = source[2]
        dx = destination[0]
        dy = destination[1]
        dz = destination[2]

        root = Node(sx, sy, sz)
        graph = Graph(root, xy_mat, yz_mat, zx_mat)

        # Checking destination point is valid
        if not vacant_spot(dx, dy, dz, xy_mat, yz_mat, zx_mat):
            print("No path to destination was found")
            return

        # Scanning the cube as a graph
        response, dest_node = scan_cube(graph, destination, xy_mat, yz_mat, zx_mat)

        if response == Response.FOUND:
            # If a path was found from source to destination, we need to track the steps
            steps = track_path(graph, dest_node, root)

            result_path = ""
            while not steps.empty():
                result_path = result_path + str(steps.get()) + " "

            print(f'{result_path}')
        else:
            print("No path to destination was found")


# Good Luck!
main = Main()
main.run()
