# coloring # 주어진 좌표를 원하는 색으로 칠하기 (조건: 색을 칠할 픽셀 좌표가 주어진 경우 가능)
def coloring(what_to_color, to_which_color): # fill
    pass

# color switch # 존재하는 색 2개를 바꾸기 (조건: 한 그리드 내부에서 색을 바꾸기)
def color_switch(of_which_component1, of_which_component2):
    pass

# rotate # (오브젝트 or 그리드 or 픽셀)이 (어떠한 방향)으로 (얼마나) (어느 지점을 기준으로) 회전하는데 (원본을 자르는지 보존하는지)
def rotate(what_to_rotate, which_direction, how_many_times, pivot, keep_original):
    print(what_to_rotate, type(what_to_rotate), what_to_rotate.center)
    if pivot == None:
        pivot = what_to_rotate.center
    else:
        pivot = pivot


    return what_to_rotate

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
