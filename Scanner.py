# Algorithmic Robotics and Motion Planning - Assignment no. 1
# Dvir Ben Asuli        318208816
# Tel-Aviv University   October 2021

from enum import Enum
from queue import Queue, LifoQueue

class Response(Enum):
    NOT_FOUND = 0
    FOUND = 1

def scan_cube(graph, source, destination, xy, yz, zx):
    sx = source[0]
    sy = source[1]
    sz = source[2]
    dx = destination[0]
    dy = destination[1]
    dz = destination[2]

    while not graph.queue.empty():
        curr_option = graph.queue.get()

        x = curr_option.x
        y = curr_option.y
        z = curr_option.z
        if x == dx and y == dy and z == dz:
            return Response.FOUND, curr_option


        try_direction(graph, curr_option, x+1, y, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y+1, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y, z+1, xy, yz, zx)
        try_direction(graph, curr_option, x-1, y, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y-1, z, xy, yz, zx)
        try_direction(graph, curr_option, x, y, z-1, xy, yz, zx)

    return Response.NOT_FOUND


def vacant_spot(x, y, z, xy, yz, zx):
    cond1 = xy[y][x] == 0
    cond2 = yz[z][y] == 0
    cond3 = zx[x][z] == 0

    return cond1 and cond2 and cond3

def try_direction(graph, curr_node, x, y, z, xy, yz, zx):
    if not vacant_spot(x, y, z, xy, yz, zx):
        return 0

    graph.add_node(curr_node, x, y, z)
    return 1


def track_path(grpah, destNode, sourceNode):
    path = LifoQueue(maxsize = grpah.xy_size*grpah.yz_size*grpah.zx_size)

    curr_node = destNode

    while (curr_node != sourceNode):
        curr_step = get_step(curr_node)
        path.put(curr_step)
        curr_node = curr_node.get_parent()

    return path

def get_step(node):
    prev_node = node.get_parent()

    if prev_node.x+1 == node.x:
        return 0

    if prev_node.x-1 == node.x:
        return 1

    if prev_node.y+1 == node.y:
        return 2

    if prev_node.y-1 == node.y:
        return 3

    if prev_node.z+1 == node.z:
        return 4

    if prev_node.z-1 == node.z:
        return 5


