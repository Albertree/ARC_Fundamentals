from .dsl import *
from .hodel_utils import *

def get_left_top_pos(obj):
    obj = list(obj)
    leftmost_coord = 100
    topmost_coord = 100
    for i in range(len(obj)):
        if obj[i][1][0] < leftmost_coord:
            leftmost_coord = obj[i][1][0]
        if obj[i][1][1] < topmost_coord:
            topmost_coord = obj[i][1][1]
    return (leftmost_coord, topmost_coord)

def get_colorset(obj):
    obj = list(obj)
    colorset = set()
    for i in range(len(obj)):
        colorset.add(obj[i][0])
    return list(colorset)

# change object list to dictionary and save the object function parameters
def find_all_objects(grid):
    grid = totuple(grid)

    object_list = []

    
    # {"obj": [frozenset({(5, (0, 2)), (5, (2, 0)), (5, (1, 1))})],
    # "pos": [(0, 0)],
    # "colorset": [5],
    # "method": [True, True, True] }

    # 1. single color, diagonal, background
    for obj in objects(grid, True, True, True):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [True, True, True]
            object_list.append(object_info)

    # 2. single color, diagonal, no background
    for obj in objects(grid, False, True, True):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [False, True, True]
            object_list.append(object_info)

    # 3. single color, not diagonal, background
    for obj in objects(grid, True, False, True):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [True, False, True]
            object_list.append(object_info)

    # 4. single color, not diagonal, no background
    for obj in objects(grid, False, False, True):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [False, False, True]
            object_list.append(object_info)

    # 5. multiple color, diagonal, background
    for obj in objects(grid, True, True, False):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [True, True, False]
            object_list.append(object_info)

    # 6. multiple color, diagonal, no background
    for obj in objects(grid, False, True, False):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [False, True, False]
            object_list.append(object_info)

    # 7. multiple color, not diagonal, background
    for obj in objects(grid, True, False, False):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [True, False, False]
            object_list.append(object_info)

    # 8. multiple color, not diagonal, no background
    for obj in objects(grid, False, False, False):
        object_info = {"obj": [], "pos": [], "colorset": [], "method": []}
        if not any(obj == existing_obj["obj"] for existing_obj in object_list):
            object_info["obj"] = obj
            object_info["pos"] = get_left_top_pos(obj)
            object_info["colorset"] = get_colorset(obj)
            object_info["method"] = [False, False, False]
            object_list.append(object_info)

    # print("#########")
    # print(len(object_list))
    
    # # sort objects with length
    # for key in object_dict:
    #     object_dict[key].sort(key=lambda x: (len(x)))#, list(x)[0][1]))
    return object_list


def find_all_objects_sort(grid):
    all_objects = find_all_objects(grid)

    # convert frozenset to list
    all_objects_list = []
    for obj in all_objects:
        all_objects_list.append(list(obj))

    # sort each object
    for sublist in all_objects_list:
        sublist.sort(key=lambda x: x[1])

    all_objects_list.sort(key=lambda sublist: (len(sublist), sublist[0][1]))

    return all_objects_list


def find_all_objects_sort_grid(grid):
    all_objects_list = find_all_objects_sort(grid)

    # convert colcoord to grid
    all_objects_sort_grid = []
    for obj in all_objects_list:
        grid = togrid(obj)
        all_objects_sort_grid.append(grid)

    return all_objects_sort_grid