# Algorithmic Robotics and Motion Planning - Assignment no. 1
# Dvir Ben Asuli        318208816
# Tel-Aviv University   October 2021

def instruction_parser(command):
    i = 0
    xy_mat = []
    yz_mat = []
    zx_mat = []
    xy_finished = 0
    yz_finished = 0
    zx_finished = 0

    values = command.split()

    #Get starting coordinates
    sx = int(values[0])
    sy = int(values[1])
    sz = int(values[2])

    #Get destinations coordinates
    dx = int(values[3])
    dy = int(values[4])
    dz = int(values[5])

    #Handle File
    filename = values[6]
    file = open(filename, "r")

    for line in file:
        values = line.split()
        if (i == 0):
            ## dimensions[0]= x, dimensions[1]= y, dimensions[2]= z
            dimensions = values
            i = i + 1
            continue

        if (i > 0):
            if (line == ""):
                continue

            #XY
            #The entry in row i>=0 and column j>=0 in the xy-matrix represents the value for x=j and y=i
            num_of_cols  = int(dimensions[0]) # X
            num_of_lines = int(dimensions[1]) # Y

            j = 0
            if (i < num_of_lines+1):

                line_array = []
                while ( j<num_of_cols):
                    line_array.append(int(values[j]))
                    j = j+1

                xy_mat.append(line_array)
                prev_i1 = i
                i = i + 1
                continue

            if (xy_finished == 0):
                xy_finished = 1
                continue

            #YZ
            #The entry in row i>=0 and column j>=0 in the YZ-matrix represents the value for y=j and z=i
            num_of_cols  = int(dimensions[1])  # Y
            num_of_lines = int(dimensions[2])  # Z

            j = 0
            if (i < prev_i1 + num_of_lines + 1):

                line_array = []
                while (j < num_of_cols):
                    line_array.append(int(values[j]))
                    j = j + 1

                yz_mat.append(line_array)
                prev_i2 = i
                i = i + 1
                continue

            if (yz_finished == 0):
                yz_finished = 1
                continue

            #ZX
            #The entry in row i>=0 and column j>=0 in the zx-matrix represents the value for z=j and x=i
            num_of_cols  = int(dimensions[2])  # Z
            num_of_lines = int(dimensions[0])  # X

            j = 0
            if (i < prev_i1 + prev_i2 + num_of_lines + 1):

                line_array = []
                while (j < num_of_cols):
                    line_array.append(int(values[j]))
                    j = j + 1

                zx_mat.append(line_array)
                i = i + 1
                continue

            if (zx_finished == 0):
                zx_finished = 1
                continue

    file.close()
    return [sx, sy, sz], [dx, dy, dz], xy_mat, yz_mat, zx_mat
