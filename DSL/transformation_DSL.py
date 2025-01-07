
# rotate
def rotate(what_to_rotate, which_direction, how_many_times, pivot):
    print(what_to_rotate, type(what_to_rotate), what_to_rotate.center)
    if pivot == None:
        pivot = what_to_rotate.center
    else:
        pivot = pivot

    if which_direction == 'cw':
        for _ in range(how_many_times):
            what_to_rotate = rotate_cw(what_to_rotate, pivot)
    elif which_direction == 'ccw':
        for _ in range(how_many_times):
            what_to_rotate = rotate_ccw(what_to_rotate)

    return what_to_rotate

# flip
def flip(what_to_flip, which_direction, pivot):
    pass

# move
def move(what_to_move, which_direction, how_many_times, pivot):
    pass

# coloring
def coloring(what_to_color, to_which_color):
    pass

# color switch
def color_switch(of_which_component1, of_which_component2):
    pass

# scale up
def scale(original_grid, scale):
    pass

# crop
def crop(where_to_crop, from_where):
    pass

# set grid
def set_grid(size_of_grid, color_to_fill):
    pass

# connect
def connect(from_where, to_where, which_color):
    pass

# rectangle
def rectangle(from_where, to_where, which_color):
    pass