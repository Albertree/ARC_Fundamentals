from DSL.hodel_utils import *
# from DSL.dsl2 import *
from DSL.dsl3 import *

# GRID
def grid_color(grid):
    return list(set([grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != 12]))

def colorgrid_to_colcoord(colorgrid):
    return [(colorgrid[i][j], (i, j)) for i in range(len(colorgrid)) for j in range(len(colorgrid[0])) if colorgrid[i][j] != 12]


# OBJECT
def object_to_pixel_list(object):
    # return a list of tuples, each tuple is a coordinate of a pixel where the object value is not 12
    return [(i, j) for i in range(len(list(object))) for j in range(len(list(object)[0])) if list(object)[i][j] != 12]

def object_colcoord_to_colorgrid(object):
    # return a list of lists, each list has a color value of a pixel
    object = list(object)

    max_col = 0
    max_row = 0
    min_col = 100
    min_row = 100
    for n in range(len(object)):
        if object[n][1][0] > max_col:
            max_col = object[n][1][0]
        if object[n][1][1] > max_row:
            max_row = object[n][1][1] 

        if object[n][1][0] < min_col:
            min_col = object[n][1][0]
        if object[n][1][1] < min_row:
            min_row = object[n][1][1]

    if min_col == 100:
        min_col = max_col
    if min_row == 100:
        min_row = max_row
    
    if min_col == 0:
        col_move = 0
    else:
        col_move = min_col

    if min_row == 0:
        row_move = 0
    else:
        row_move = min_row

    colorgrid = [[12 for j in range(max_row - min_row + 1)] for i in range(max_col - min_col + 1)]
    for n in range(len(object)):
        colorgrid[object[n][1][0]-(col_move)][object[n][1][1]-(row_move)] = object[n][0]
    return colorgrid

# def object_to_colcoord(object):
#     # return a list of integer and integer tuple (color, (row, col))
#     return [(object[i][j], (i, j)) for i in range(len(list(object))) for j in range(len(list(object)[0])) if list(object)[i][j] != 12]

def absolute_coordinate_of_object(coordinate, pos):
    return [(coordinate[i][0] + pos[0], coordinate[i][1] + pos[1]) for i in range(len(coordinate))]

def measure_shape(object):
    # return an array of 0 or 1, 0 for value 12, 1 for other values
    shape = [[0 for j in range(len(object[0]))] for i in range(len(object))]
    for i in range(len(object)):
        for j in range(len(object[0])): 
            if object[i][j] != 12:
                shape[i][j] = 1 # 0 for valid color (color between 0 and 9)
            else:
                shape[i][j] = -1 # -1 for no color (color 12)
    return shape

def measure_area(shape):
    return sum([1 for i in range(len(shape)) for j in range(len(shape[0])) if shape[i][j] == 1])

# def count_non_12(grid):
#     return sum([1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != 12])

def margin_of_grid(grid):
    margin = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                margin.append((i, j))
    return margin

def inner_of_grid(grid):
    inner = []  
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i != 0 and i != len(grid) - 1 and j != 0 and j != len(grid[0]) - 1:
                inner.append((i, j))
    return inner

def corner_of_grid(grid):
    corner = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid[0]) - 1):
                corner.append((i, j))
    return corner

def edge_of_grid(grid):
    edge = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                if not ((i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid[0]) - 1)):
                    edge.append((i, j))
    return edge

def center_of_grid(grid):
    center = []
    if len(grid) % 2 == 1:
        # vertical odd, horizontal odd
        if len(grid[0]) % 2 == 1:
            center.append((len(grid) // 2, len(grid[0]) // 2))
        # vertical odd, horizontal even
        else:
            center.append((len(grid) // 2, len(grid[0]) // 2 - 1))
            center.append((len(grid) // 2, len(grid[0]) // 2))
    else:
        # vertical even, horizontal odd
        if len(grid[0]) % 2 == 1:
            center.append((len(grid) // 2 - 1, len(grid[0]) // 2))
            center.append((len(grid) // 2, len(grid[0]) // 2))
        # vertical even, horizontal even
        else:
            center.append((len(grid) // 2 - 1, len(grid[0]) // 2 - 1))
            center.append((len(grid) // 2 - 1, len(grid[0]) // 2))
            center.append((len(grid) // 2, len(grid[0]) // 2 - 1))
            center.append((len(grid) // 2, len(grid[0]) // 2))
    return center

def grid_horizontal_symmetry(grid):
    # Check if the grid is horizontally symmetric
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows // 2 + 1):
        if grid[i] != grid[rows - i - 1]:
            return False
    return True

def grid_vertical_symmetry(grid):
    # Check if the grid is vertically symmetric
    rows = len(grid)
    cols = len(grid[0])
    for j in range(cols // 2 + 1):
        for i in range(rows):
            if grid[i][j] != grid[i][cols - j - 1]:
                return False
    return True

def grid_diagonal_symmetry(grid):
    # Check if the grid is symmetric along the main diagonal
    size = len(grid)
    for i in range(size):
        for j in range(i + 1, size):
            if grid[i][j] != grid[j][i]:
                return False
    return True

def grid_antidiagonal_symmetry(grid):
    # Check if the grid is symmetric along the anti-diagonal
    size = len(grid)
    for i in range(size):
        for j in range(size - i - 1):
            if grid[i][j] != grid[size - j - 1][size - i - 1]:
                return False
    return True





class TASK:
    def __init__(self, tasks, t):
        ############################################################
        # BASICS
        self.id = (t, None, None, None, None)
        self.type = "task"

        ############################################################
        # VIEW
        self.view = tasks[t]

        ############################################################
        # REPRESENTATIONS
        self.example_pairs = tasks[t][0]
        self.test_pairs = tasks[t][1]

        ############################################################
        # PROPERTIES
        self.number_of_examples = len(self.example_pairs)
        self.number_of_tests = len(self.test_pairs)
        
        ############################################################
        # ANCESTOR
        # None

        ############################################################
        # DESCENDANTS
        self.pair_list = None # list of PAIR classes

        ############################################################
        # RELATIONS
        self.pair_relation = None # list of PAIR_RELATION classes

        


class PAIR:
    def __init__(self, ttt, t, p):
        ############################################################
        # BASICS
        self.id = (t, p, None, None, None)
        self.type = "pair"
        
        ############################################################
        # VIEW
        self.view = ttt.example_pairs[p]
        
        ############################################################
        # REPRESENTATIONS
        self.grids = ttt.example_pairs[p] # grids in array

        ############################################################
        # PROPERTIES
        self.number_of_grids = len(self.grids) # 2

        ############################################################
        # ANCESTOR
        self.ancestor = ttt

        ############################################################
        # DESCENDANTS
        self.grid_list = None # list of GRID classes

        ############################################################
        # RELATIONS
        self.grid_relation = None # list of GRID_RELATION classes

        


class GRID:
    def __init__(self, ppp, t, p, g):
        ############################################################
        # BASICS
        self.id = (t, p, g, None, None)
        self.type = "grid"

        ############################################################
        # VIEW
        self.view = ppp.grids[g] # v

        ############################################################
        # REPRESENTATIONS
        self.colorgrid = self.view 
        self.colcoord = colorgrid_to_colcoord(self.colorgrid)

        ############################################################
        # PROPERTIES
        self.objects = find_all_objects(self.colorgrid)
        
        self.color = grid_color(self.colorgrid)
        self.row_index = range(len(self.colorgrid))
        self.col_index = range(len(self.colorgrid[0]))
        self.coordinate = [(i, j) for i in self.row_index for j in self.col_index]

        self.height = len(self.colorgrid)
        self.width = len(self.colorgrid[0])
        self.size = (self.height, self.width)
        self.shape = measure_shape(self.colorgrid)
        self.area = measure_area(self.shape)
        self.center = center_of_grid(self.colorgrid)

        self.margin = margin_of_grid(self.colorgrid)
        self.inner = inner_of_grid(self.colorgrid)
        self.corner = corner_of_grid(self.colorgrid)
        self.edge = edge_of_grid(self.colorgrid)

        self.left_top = (0, 0)
        self.right_top = (0, self.width)
        self.left_bottom = (self.height, 0)
        self.right_bottom = (self.height, self.width)

        self.hori_symm = grid_horizontal_symmetry(self.colorgrid)
        self.verti_symm = grid_vertical_symmetry(self.colorgrid)
        if self.height == self.width:
            self.diag_symm = grid_diagonal_symmetry(self.colorgrid)
            self.anti_diag_symm = grid_antidiagonal_symmetry(self.colorgrid)
        else:
            self.diag_symm = False
            self.anti_diag_symm = False
        
        ############################################################
        # ANCESTOR
        self.ancestor = ppp

        ############################################################
        # DESCENDANTS
        self.object_list = None # list of OBJECT classes

        ############################################################
        # RELATIONS
        self.object_relation = None # list of OBJECT_RELATION classes
        



class OBJECT:
    def __init__(self, ggg, t, p, g, o):
        ############################################################
        # BASICS
        self.id = (t, p, g, o, None)
        self.type = "object"

        ############################################################
        # VIEW
        # self.view = object_colcoord_to_colorgrid(ggg.objects[o]["obj"])
        self.view = object_colcoord_to_colorgrid(ggg.object_list[o]["obj"])

        ############################################################
        # REPRESENTATIONS
        self.colorgrid = self.view # list of lists, each list has a color value of a pixel
        # self.colcoord = list(ggg.objects[o]["obj"])
        # self.colcoord = list(find_all_objects(self.colorgrid)[o]["obj"])
        self.colcoord = ggg.object_list[o]["obj"]

        ############################################################
        # PROPERTIES
        self.pixels = object_to_pixel_list(self.colorgrid) # list of tuples, each tuples are coordinates
        # self.pos = ggg.objects[o]["pos"] # only in object not in grid
        # self.color = ggg.objects[o]["color"] # also in pixel
        # self.method = ggg.objects[o]["method"] # only in object not in grid
        
        self.pos = ggg.object_list[o]["pos"] # only in object not in grid
        self.color = ggg.object_list[o]["color"] # also in pixel
        self.method = ggg.object_list[o]["method"] # only in object not in grid

        self.row_index = range(len(self.colorgrid)) # also in pixel
        self.col_index = range(len(self.colorgrid[0])) # also in pixel
        self.coordinate = absolute_coordinate_of_object(self.pixels, self.pos) # also in pixel

        self.height = len(self.colorgrid)
        self.width = len(self.colorgrid[0])
        self.size = (self.height, self.width)
        self.shape = measure_shape(self.colorgrid)
        self.area = measure_area(self.shape)
        self.center = absolute_coordinate_of_object(center_of_grid(self.colorgrid), self.pos)

        self.margin = absolute_coordinate_of_object(margin_of_grid(self.colorgrid), self.pos)
        self.inner = absolute_coordinate_of_object(inner_of_grid(self.colorgrid), self.pos)
        self.corner = absolute_coordinate_of_object(corner_of_grid(self.colorgrid), self.pos)
        self.edge = absolute_coordinate_of_object(edge_of_grid(self.colorgrid), self.pos)

        self.left_top = (self.pos[0], self.pos[1])
        self.right_top = (self.pos[0], self.pos[1] + self.width)
        self.left_bottom = (self.pos[0] + self.height, self.pos[1])
        self.right_bottom = (self.pos[0] + self.height, self.pos[1] + self.width)

        self.hori_symm = grid_horizontal_symmetry(self.colorgrid) # 상하 대칭
        self.verti_symm = grid_vertical_symmetry(self.colorgrid) # 좌우 대칭
        if self.height == self.width:
            self.diag_symm = grid_diagonal_symmetry(self.colorgrid)
            self.anti_diag_symm = grid_antidiagonal_symmetry(self.colorgrid)
        else:
            self.diag_symm = False
            self.anti_diag_symm = False
        
        ############################################################
        # ANCESTOR
        self.ancestor = ggg

        ############################################################
        # DESCENDANTS
        self.pixel_list = None # list of PIXEL classes
        
        ############################################################
        # RELATIONS
        self.pixel_relation = None # list of PIXEL_RELATION classes
        # distance
        # neighboring
        ## same_color




class PIXEL:
    def __init__(self, ooo, t, p, g, o, x):
        ############################################################
        # BASICS
        self.id = (t, p, g, o, x)
        self.type = "pixel"

        ############################################################
        # VIEW
        self.view = [ooo.colcoord[x][0]] 

        ############################################################
        # REPRESENTATIONS
        self.colorgrid = self.view
        self.colcoord = [ooo.colcoord[x]]

        ############################################################
        # PROPERTIES
        self.color = ooo.colcoord[x][0]
        self.row_index = ooo.colcoord[x][1][0]
        self.col_index = ooo.colcoord[x][1][1]
        self.coordinate = (self.row_index, self.col_index)

        ############################################################
        # ANCESTOR
        self.ancestor = ooo

        ############################################################
        # DESCENDANTS
        # NONE

        ############################################################
        # RELATIONS
        # NONE
    
        

class TRANSFORMED:
    def __init__(self, xyz, t, p=None, g=None, o=None, x=None, prev=None):
        self.id = (t, p, g, o, x)
        self.type = "transformed"

        self.history = []
        self.view = xyz

        


