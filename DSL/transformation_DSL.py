from typing import Tuple, List

Boolean = bool
Integer = int
Grid = Tuple[Tuple[Integer]]

# grid operation 과 object operation 을 나누어야 하는가
# grid operation 은 grid를 return 하는 것이기 때문에, object select 시 crop -> operation -> paste 가 포함되어 있는 것과 같다
# object operation 은 object에만 operation 을 적용하는 것이기 때문에, crop and paste를 포함하지 않는다
# 그럼 모든 operation은 모두 object operation 이라고 하면 crop and paste function을 만들었을 때, 문제가 되는 것이 없는가.
# 모든 operation을 생각해보자
# crop -> operation -> paste 인 경우: rotate, flip, move, teleport
# make empty layer -> operation -> paste 인 경우: connect, draw_line, cover_area
# duplicate layer -> operation -> paste 인 경우: 
# crop -> operation -> make it as a new grid 인 경우


# 이렇게 경우의 수를 나누어 생각하는 것이 인간이 생각하는 transformation의 적용방식인가?
# 인간은 grid transformation을 어떻게 생각할까?

# grid coloring: grid 위에 주어진 좌표대로 색칠하는 것
# object coloring: object 위에 주어진 좌표대로 색칠하는 것
# pixel coloring: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)

# grid color switch: grid에 있는 색상 두 개를 바꾸는 것 -> return grid
# object color switch: object에 있는 색상 두 개를 바꾸는 것 -> return object
# pixel color switch: 불가능

# grid rotate: grid 전체를 회전하고 이를 이전 grid에 업데이트 하는 것 (grid의 크기가 바뀔 수 있음)
# object rotate: grid에 있는 object를 가상의 차원에 복제/잘라내기 하여 회전 및 회전이동 한 후, 원래의 grid에 덧붙이기 하는 것
# pixel rotate: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)

# grid flip: grid 전체를 반전하고 이를 이전의 grid에 업데이트 하는 것 (grid의 크기가 바뀔 수 있음)
# object flip: grid에 있는 object를 가상의 차원에 복제/잘라내기 하여 대칭 및 대칭이동 한 후, 원래의 grid에 덧붙이기 하는 것
# pixle flip: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)

# grid move: 불가능
# object move: grid에 있는 object를 가상의 차원에 복제/잘라내기 하여 이동 한 후, 원래의 grid에 덧붙이기 하는 것 ** 잘라내기 했다면 잘린 곳은 어떻게 되는가 (background color를 확실히 정의 하는 것)
# pixel move: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)

# grid teleport: 불가능
# object teleport: grid에 있는 object를 가상의 차원에 복제/잘라내기 하여 이동 한 후, 원래의 grid에 덧붙이기 하는 것 ** 잘라내기 했다면 잘린 곳은 어떻게 되는가 (background color를 확실히 정의 하는 것)
# pixel teleport: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)

# grid connect: grid에 있는 두 점을 가상의 차원에서 잇고 원래의 grid에 덧붙이기 하는 것
# object connect: object에 있는 두 점을 가상의 차원에서 잇고 원래의 object에 덧붙이기 하는 것
# pixel connect: 불가능

# grid straight_line: grid에 있는 점을 가상의 차원에서 방향과 거리로 확장하고 원래의 grid에 덧붙이기 하는 것
# object straight_line: object에 있는 점을 가상의 차원에서 방향과 거리로 확장하고 원래의 object에 덧붙이기 하는 것
# pixel straight_line: 불가능

# grid rectangle: grid에 있는 두 점을 가상의 차원에서 색칠하고 원래의 grid에 덧붙이기 하는 것
# object rectangle: object에 있는 두 점을 가상의 차원에서 색칠하고 원래의 object에 덧붙이기 하는 것
# pixel rectangle: 불가능

# grid scale: grid 전체를 확대/축소하고 이를 이전 grid에 업데이트 하는 것 (grid의 크기가 바뀔 수 있음)
# object scale: grid에 있는 object를 가상의 차원에 복제/잘라내기 하여 확대/축소 한 후, 새로운 object로 정의하는 것
# pixel scale: * pixel은 선택 시 1x1 크기의 object로 취급된다. (object 연산에 포함)


# crop
# cut 
# paste 

# split_layer
# split_crop_layer
# split_cut_layer
# split_empty_layer

# merge_layer



# make frame
# 절대적 rule을 정한다면
# 0. transformation DSL은 GRID 이상의 level에서 적용할 수 없다.
# 1. 모든 함수는 벗어날 수 없는 틀을 input으로 받는다. => 이것은 사용자가 원하는 return의 level과 같다.
# 예) 사용자가 grid를 원하면 grid를 input 으로 하고, 사용자가 object를 원한다면 object를 input으로 한다.
# 2. return level이 달라지는 함수는 단 3개, to_grid, to_object, to_pixel 이다.
# 3. 





# # to_grid
# # 적용 대상: Object, Pixel -> 결과: Grid
# # what_to_grid == 변환할 것 (object or pixel) == colorgrid or colcoord
# def to_grid(what_to_grid):
#     if what_to_grid.type == "object":
#         result = what_to_grid.colorgrid
#     elif what_to_grid.type == "pixel":
#         result = [[what_to_grid.colorgrid[what_to_grid.coord[0]][what_to_grid.coord[1]]]]
#     return result

# # to_object
# # 적용 대상: Grid -> 결과: Object
# # what_to_object == 변환할 것 (grid) == colorgrid
# def to_object(what_to_object):
#     result = Object(what_to_object)
#     return result

# # to_pixel
# # 적용 대상: Grid, Object -> 결과: Pixel
# # what_to_pixel == 변환할 것 (grid or object) == colorgrid or colcoord
# def to_pixel(what_to_pixel):
#     assert what_to_pixel.size == 1
#     result = Pixel(what_to_pixel.coord)
#     return result









# coloring # 주어진 좌표를 원하는 색으로 칠하기 (조건: 색을 칠할 픽셀 좌표가 주어진 경우 가능)
# on_where          == 칠할 판     (grid or object or pixel)    == colorgrid or colcoord
# what_to_color     == 칠할 곳     (coordinates)                == list of tuples
# to_which_color    == 칠할 색     (color)                      == int between 0 and 12
def coloring(on_where, what_to_color, to_which_color):
    for i in range(len(what_to_color)):
        on_where.colorgrid[what_to_color[i][0]][what_to_color[i][1]] = to_which_color
    return on_where

# color switch # 존재하는 색 2개를 바꾸기 (조건: 한 그리드 내부에서 색을 바꾸기)
# on_where              == 바뀔 판      (grid or object)   == colorgrid or colcoord
# of_which_component1   == 바꿀 색 1    (color)            == int between 0 and 12
# of_which_component2   == 바꿀 색 2    (color)            == int between 0 and 12
def color_switch(on_where, of_which_component1, of_which_component2):
    assert of_which_component1 != of_which_component2
    assert of_which_component1 in on_where.colorset
    assert of_which_component2 in on_where.colorset

    for i in range(len(on_where.colorgrid)):
        for j in range(len(on_where.colorgrid[i])):
            if on_where.colorgrid[i][j] == of_which_component1:
                on_where.colorgrid[i][j] = of_which_component2
            elif on_where.colorgrid[i][j] == of_which_component2:
                on_where.colorgrid[i][j] = of_which_component1
    return on_where


# hodel
def rot90(grid):
    return tuple(row for row in zip(*grid[::-1]))

def rot180(grid):
    grid = grid.colorgrid
    return tuple(tuple(row[::-1]) for row in grid[::-1])

def rot270(grid):
    grid = grid.colorgrid
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]

def horizontal_flip(grid):
    grid = grid.colorgrid
    return tuple(row[::-1] for row in grid)

def vertical_flip(grid):
    grid = grid.colorgrid
    return tuple(row for row in grid[::-1])

def diagonal_flip(grid):
    grid = grid.colorgrid
    return tuple(tuple(row[::-1]) for row in zip(*grid))[::-1]

def antidiag_flip(grid):
    grid = grid.colorgrid
    return tuple(row[::-1] for row in zip(*grid[::-1]))



# rotate # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (얼마나) (어느 지점을 기준으로) 회전하는데 (원본을 자르는지 보존하는지)
# grid 를 회전하는 경우 -> return grid
# object를 회전하는 경우 -> return object or grid
# pixel을 회전하는 경우 -> return pixel or object or grid
# what_to_rotate    == 회전할 것        (object or grid or pixel)   == colorgrid or colcoord
# which_direction   == 회전 방향        (left or right)             == rot_dir
# how_many_times    == 회전 횟수        (int)                       == int
# pivot             == 회전 기준지점     (tuple)                     == coord or coords
# keep_original     == 원본 보존여부     (bool)                      == bool
def rotate(what_to_rotate, which_direction="cw", how_many_times=1, pivot=None):
    if what_to_rotate.type == "grid":
        object_center = what_to_rotate.center
        pivot = what_to_rotate.center
        mother_grid = what_to_rotate

    elif what_to_rotate.type == "object":
        if pivot is None:
            object_center = what_to_rotate.center
            pivot = what_to_rotate.center
            mother_grid = what_to_rotate.ancestor
        else:
            object_center = what_to_rotate.center
            pivot = pivot
            mother_grid = what_to_rotate.ancestor
    
    rotations = how_many_times % 4

    if which_direction == "ccw":
        rotations = (4 - rotations) % 4

    for _ in range(rotations):
        what_to_rotate.colorgrid = rot90(what_to_rotate.colorgrid)

    print(what_to_rotate.colorgrid)

    if len(object_center) != 1:
        object_center_rep = tuple(float(sum(p) / len(p)) for p in zip(*object_center))
    else:
        object_center_rep = object_center[0]

    if len(pivot) != 1:
        pivot_rep = tuple(float(sum(p) / len(p)) for p in zip(*pivot))
    else:
        pivot_rep = pivot[0]

    print(object_center, pivot)
    print(object_center_rep, pivot_rep)

    rotated_center = object_center_rep
    rotated_center = (rotated_center[0] - pivot_rep[0], rotated_center[1] - pivot_rep[1])
    for _ in range(rotations):
        rotated_center = (rotated_center[1], -rotated_center[0])
        print(rotated_center)

    rotated_center = (rotated_center[0] + pivot_rep[0], rotated_center[1] + pivot_rep[1])
    print(rotated_center)


    if rotated_center[0] != int(rotated_center[0]):
        rc_split1 = (int(rotated_center[0]), int(rotated_center[0])+1)
    else:
        rc_split1 = (int(rotated_center[0]), int(rotated_center[0]))

    if rotated_center[1] != int(rotated_center[1]):
        rc_split2 = (int(rotated_center[1]), int(rotated_center[1])+1)
    else:
        rc_split2 = (int(rotated_center[1]), int(rotated_center[1]))
    print(rc_split1, rc_split2, "*****")

    
    rotated_center = tuple(set((x, y) for y in rc_split2 for x in rc_split1))
    print(rotated_center)



    # rotated_object = teleport(what_to_rotate, what_to_rotate.center, rotated_center)

    # print(pivot)

    # Normalize the number of rotations
    # how_many_times = how_many_times % 4  # Since 4 rotations bring it back to the original

    # if which_direction == "ccw":
    #     how_many_times = 4 - how_many_times  # Convert counter-clockwise to equivalent clockwise rotations

    # n = len(what_to_rotate.colorgrid)
    # m = len(what_to_rotate.colorgrid[0]) if n > 0 else 0

    # for _ in range(how_many_times):
    # print(what_to_rotate.colorgrid)
    # what_to_rotate.colorgrid = rot90(what_to_rotate.colorgrid)
    # print(what_to_rotate.colorgrid)
    # print()

    return what_to_rotate.colorgrid




# flip # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (어느 지점을 기준으로) 대칭이동 하는데 (원본을 자르는지 보존하는지)
# grid 를 flip 하는 경우 -> return grid
# object를 flip 하는 경우 -> return object or grid
# pixel을 flip 하는 경우 -> return pixel or object or grid
# what_to_flip    == 대칭이동할 것     (object or grid or pixel)   == colorgrid or colcoord
# which_direction  == 대칭이동 방향    (horizontal or vertical)    == flip_dir
# pivot           == 대칭이동 기준점    (tuple)                     == coord or coords
# keep_original   == 원본 보존여부     (bool)                      == bool
def flip(what_to_flip, which_direction, pivot):  
    pass

# move # (오브젝트 or 픽셀)이 (어떠한 방향)으로 (얼마나) (어느 지점을 기준으로) 이동하는데 (원본을 자르는지 보존하는지)
# what_to_move    == 이동할 것        (object or pixel)                 == colorgrid or colcoord
# which_direction  == 이동 방향        (up or down or left or right)    == move_dir
# how_many_times   == 이동 횟수        (int)                            == int
# keep_original   == 원본 보존여부     (bool)                            == bool
def move(what_to_move, which_direction, how_many_times):
    pass

# # drag # (오브젝트 or 그리드 or 픽셀)의 (어떠한 지점을 잡아서) (어디로) 이동하는데 (원본을 자르는지 보존하는지)
# def drag(what_to_drag, grab_which_point, to_where, keep_original):
#     pass

# teleport # (오브젝트 or 픽셀)의 (어떠한 지점을 잡아서) (어디로) 이동하는데 (원본을 자르는지 보존하는지)
# what_to_teleport == 이동할 것        (object or pixel)   == colorgrid or colcoord
# grab_which_point  == 이동 기준점     (tuple)             == coord or coords
# to_where          == 이동 목적지      (tuple)             == coord or coords
# keep_original     == 원본 보존여부     (bool)              == bool
# return            == 이동된 것        (grid or object)   == colorgrid or colcoord    
def teleport(what_to_teleport, grab_which_point, to_where):
    if what_to_teleport.type == "object":
        if grab_which_point is None:
            grab_which_point = what_to_teleport.left_top
        result = what_to_teleport.colorgrid[grab_which_point[0]:grab_which_point[0]+what_to_teleport.height, grab_which_point[1]:grab_which_point[1]+what_to_teleport.width]
    elif what_to_teleport.type == "pixel":
        grab_which_point = what_to_teleport.coord

    if what_to_teleport.type == "object":
        what_to_teleport.left_top = to_where
    elif what_to_teleport.type == "pixel":
        what_to_teleport.coord = to_where
    return what_to_teleport

# connect # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 선을 그리는데 (시작점을 포함하는지 끝점을 포함하는지)
def connect(start_point, end_point, which_color, include_start_point, include_end_point):
    pass

# line # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 선을 그리는데 (시작점을 포함하는지 끝점을 포함하는지)
def straight_line(starting_point, direction, length, which_color):
    pass

# rectangle # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 영역-직사각형을 그리는데 (시작행과 열을 포함하는지 끝행과 열을 포함하는지)
def rectangle(start_point, end_point, which_color, include_start_point, include_end_point):
    pass


# scale # (어떠한 그리드, 오브젝트, 픽셀)을 (얼마나) 확대하는데 (원본을 자르는지 보존하는지)
# 적용 대상: Grid, Object, Pixel -> 결과: Grid, Object
# what_to_scale    == 확대할 것        (grid or object or pixel)   == colorgrid or colcoord
# scale_factor      == 확대 배율       (int)                       == -5 to 5 except 0 and -1
def scale(what_to_scale, scale_factor): # 그리드 사이즈 바뀔 수 있음
    pass



# crop # (어떠한 영역)을 잘라서 그리드로 만드는데 (선택한 영역 안쪽인지 바깥쪽인지)
def crop(where_to_crop, inout): # 그리드 사이즈 바뀔 수 있음
    pass

# cut # (어떠한 영역)을 잘라내기
def cut(where_to_cut): # 가상공간에 저장
    pass



# make frame # (어떠한 크기의 프레임)을 (어떠한 색)으로 채우기
# height_of_frame == 프레임 높이    (int)
# width_of_frame  == 프레임 너비    (int)
# color_to_fill   == 프레임 채울 색  (int)
def make_frame(height_of_frame, width_of_frame, color_to_fill=-1):
    return [[color_to_fill for _ in range(width_of_frame)] for _ in range(height_of_frame)]