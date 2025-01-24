Boolean = bool
Integer = int




# coloring # 주어진 좌표를 원하는 색으로 칠하기 (조건: 색을 칠할 픽셀 좌표가 주어진 경우 가능)
# on_where          == 칠할 판     (grid or object or pixel)    == colorgrid or colcoord
# what_to_color     == 칠할 곳     (coordinates)                == list of tuples
# to_which_color    == 칠할 색     (color)                      == int between 0 and 12
def coloring(on_where, what_to_color, to_which_color): # fill
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



def rot90(grid):
    result = list(row for row in zip(*grid[::-1]))
    for i in range(len(result)):
        result[i] = list(result[i])

    return result

# rotate # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (얼마나) (어느 지점을 기준으로) 회전하는데 (원본을 자르는지 보존하는지)
# what_to_rotate    == 회전할 것        (object or grid or pixel)   == colorgrid or colcoord
# which_direction   == 회전 방향        (left or right)             == rot_dir
# how_many_times    == 회전 횟수        (int)                       == int
# pivot             == 회전 기준지점     (tuple)                     == coord or coords
# keep_original     == 원본 보존여부     (bool)                      == bool
def rotate(what_to_rotate, which_direction="cw", how_many_times=1, pivot=None, keep_original=False):
    if what_to_rotate.type == "grid":
        pivot = what_to_rotate.center
    elif what_to_rotate.type == "object":
        if pivot is None:
            pivot = what_to_rotate.center
    elif what_to_rotate.type == "pixel":
        pivot = what_to_rotate.coord
    
    # print(pivot)

    # Normalize the number of rotations
    how_many_times = how_many_times % 4  # Since 4 rotations bring it back to the original

    if which_direction == "ccw":
        how_many_times = 4 - how_many_times  # Convert counter-clockwise to equivalent clockwise rotations

    # n = len(what_to_rotate.colorgrid)
    # m = len(what_to_rotate.colorgrid[0]) if n > 0 else 0

    # for _ in range(how_many_times):
    # print(what_to_rotate.colorgrid)
    what_to_rotate.colorgrid = rot90(what_to_rotate.colorgrid)
    print(what_to_rotate.colorgrid)
    print()

    return what_to_rotate.colorgrid

# flip # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (어느 지점을 기준으로) 대칭이동 하는데 (원본을 자르는지 보존하는지)
def flip(what_to_flip, which_direction, pivot, keep_original):
    pass

# move # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (얼마나) (어느 지점을 기준으로) 이동하는데 (원본을 자르는지 보존하는지)
def move(what_to_move, which_direction, how_many_times, pivot, keep_original):
    pass

# # drag # (오브젝트 or 그리드 or 픽셀)의 (어떠한 지점을 잡아서) (어디로) 이동하는데 (원본을 자르는지 보존하는지)
# def drag(what_to_drag, grab_which_point, to_where, keep_original):
#     pass

# teleport # (오브젝트 or 그리드 or 픽셀)의 (어떠한 지점을 잡아서) (어디로) 이동하는데 (원본을 자르는지 보존하는지)
def teleport(what_to_teleport, grab_which_point, to_where, keep_original):
    pass

# connect # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 선을 그리는데 (시작점을 포함하는지 끝점을 포함하는지)
def connect(start_point, end_point, which_color, include_start_point, include_end_point):
    pass

# draw_line # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 선을 그리는데 (시작점을 포함하는지 끝점을 포함하는지)
# def draw_line(from_where, to_where, which_color, include_start_point, include_end_point):
#     pass

# area # (어떠한 색)으로 (어떠한 시작점)과 (어떠한 끝점)을 이어주는 영역-직사각형을 그리는데 (시작행과 열을 포함하는지 끝행과 열을 포함하는지)
def cover_area(start_point, end_point, which_color, include_start_point, include_end_point):
    pass


# crop # (어떠한 영역)을 잘라서 그리드로 만드는데 (선택한 영역 안쪽인지 바깥쪽인지)
def crop(where_to_crop, inout): # 그리드 사이즈 바뀔 수 있음
    pass

# cut # (어떠한 영역)을 잘라내기
def cut(where_to_cut): # 가상공간에 저장
    pass

# scale # (어떠한 그리드, 오브젝트, 픽셀)을 (얼마나) 확대하는데 (원본을 자르는지 보존하는지)
def scale(what_to_scale, scale_factor): # 그리드 사이즈 바뀔 수 있음
    pass


# make grid # (어떠한 크기의 그리드)를 (어떠한 색)으로 채우기
def make_grid(size_of_grid, color_to_fill):
    pass
