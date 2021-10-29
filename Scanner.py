# Algorithmic Robotics and Motion Planning - Assignment no. 1
# Dvir Ben Asuli        318208816
# Tel-Aviv University   October 2021

from enum import Enum
from queue import Queue, LifoQueue


class Response(Enum):
    NOT_FOUND = 0
    FOUND = 1


# BFS scan to check if a path exists between the source and destination nodes
def scan_cube(graph, destination, xy, yz, zx):
    dx = destination[0]
    dy = destination[1]
    dz = destination[2]

    while not graph.queue.empty():
        # BFS Scan- going over every possible direction from current placement and if
        #           it's a valid position adding it to the queue for further checking
        curr_option = graph.queue.get()

        x = curr_option.x
        y = curr_option.y
        z = curr_option.z
        if x == dx and y == dy and z == dz:
            # We reached the destination, scanning can stop
            return Response.FOUND, curr_option

        try_direction(graph, curr_option, x + 1, y, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y + 1, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y, z + 1, xy, yz, zx)
        try_direction(graph, curr_option, x - 1, y, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y - 1, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y, z - 1, xy, yz, zx)

    # If the queue is empty and we never reached destination- no path exists
    return Response.NOT_FOUND


# Checking if we can move to a certain location
def vacant_spot(x, y, z, xy, yz, zx):
    cond1 = xy[y][x] == 0
    cond2 = yz[z][y] == 0
    cond3 = zx[x][z] == 0

    return cond1 and cond2 and cond3


# Receives a possible step and in case its valid adds it to the graph
# and to the queue for future BFS scan
def try_direction(graph, curr_node, x, y, z, xy, yz, zx):
    if not vacant_spot(x, y, z, xy, yz, zx):
        return 0

    graph.add_node(curr_node, x, y, z)
    return 1


# After we found a path, track the steps from destination to source
# in reverse order (hence the LIFO)
def track_path(grpah, destNode, sourceNode):
    path = LifoQueue(maxsize=grpah.xy_size * grpah.yz_size * grpah.zx_size)

    curr_node = destNode

    while (curr_node != sourceNode):
        curr_step = get_step(curr_node)
        path.put(curr_step)
        curr_node = curr_node.get_parent()

    return path


# Mapping every transitiion from one placement to the other to the
# defined output format of the assignement
def get_step(node):
    prev_node = node.get_parent()

    if prev_node.x + 1 == node.x:
        return 0

    if prev_node.x - 1 == node.x:
        return 1

    if prev_node.y + 1 == node.y:
        return 2

    if prev_node.y - 1 == node.y:
        return 3

    if prev_node.z + 1 == node.z:
        return 4

    if prev_node.z - 1 == node.z:
        return 5
