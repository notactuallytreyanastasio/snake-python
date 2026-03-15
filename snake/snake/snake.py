from abc import ABCMeta as ABCMeta13
from builtins import int as int14, bool as bool16, isinstance as isinstance17, Exception as Exception18, str as str21, list as list9, len as len8, tuple as tuple10
from typing import Sequence as Sequence15, MutableSequence as MutableSequence20
from temper_core import Label as Label19, int_add as int_add0, int_mul as int_mul1, int_negate as int_negate2, arith_int_mod as arith_int_mod3, int_div as int_div4, list_for_each as list_for_each5, int_sub as int_sub6, list_get_or as list_get_or7, str_cat as str_cat11, int_to_string as int_to_string12
int_add_947 = int_add0
int_mul_948 = int_mul1
int_negate_949 = int_negate2
arith_int_mod_950 = arith_int_mod3
int_div_951 = int_div4
list_for_each_952 = list_for_each5
int_sub_953 = int_sub6
list_get_or_954 = list_get_or7
len_955 = len8
list_956 = list9
tuple_958 = tuple10
str_cat_961 = str_cat11
int_to_string_962 = int_to_string12
class Direction(metaclass = ABCMeta13):
    pass
class Up(Direction):
    __slots__ = ()
    def __init__(this_11) -> None:
        pass
class Down(Direction):
    __slots__ = ()
    def __init__(this_13) -> None:
        pass
class Left(Direction):
    __slots__ = ()
    def __init__(this_15) -> None:
        pass
class Right(Direction):
    __slots__ = ()
    def __init__(this_17) -> None:
        pass
class Point:
    x_54: 'int14'
    y_55: 'int14'
    __slots__ = ('x_54', 'y_55')
    def __init__(this_19, x_57: 'int14', y_58: 'int14') -> None:
        this_19.x_54 = x_57
        this_19.y_55 = y_58
    @property
    def x(this_176) -> 'int14':
        return this_176.x_54
    @property
    def y(this_179) -> 'int14':
        return this_179.y_55
class GameStatus(metaclass = ABCMeta13):
    pass
class Playing(GameStatus):
    __slots__ = ()
    def __init__(this_21) -> None:
        pass
class GameOver(GameStatus):
    __slots__ = ()
    def __init__(this_23) -> None:
        pass
class RandomResult:
    value_69: 'int14'
    next_seed_70: 'int14'
    __slots__ = ('value_69', 'next_seed_70')
    def __init__(this_28, value_72: 'int14', next_seed_73: 'int14') -> None:
        this_28.value_69 = value_72
        this_28.next_seed_70 = next_seed_73
    @property
    def value(this_190) -> 'int14':
        return this_190.value_69
    @property
    def next_seed(this_193) -> 'int14':
        return this_193.next_seed_70
class SnakeGame:
    width_81: 'int14'
    height_82: 'int14'
    snake_83: 'Sequence15[Point]'
    direction_84: 'Direction'
    food_85: 'Point'
    score_86: 'int14'
    status_87: 'GameStatus'
    rng_seed_88: 'int14'
    __slots__ = ('width_81', 'height_82', 'snake_83', 'direction_84', 'food_85', 'score_86', 'status_87', 'rng_seed_88')
    def __init__(this_31, width_90: 'int14', height_91: 'int14', snake_92: 'Sequence15[Point]', direction_93: 'Direction', food_94: 'Point', score_95: 'int14', status_96: 'GameStatus', rng_seed_97: 'int14') -> None:
        this_31.width_81 = width_90
        this_31.height_82 = height_91
        this_31.snake_83 = snake_92
        this_31.direction_84 = direction_93
        this_31.food_85 = food_94
        this_31.score_86 = score_95
        this_31.status_87 = status_96
        this_31.rng_seed_88 = rng_seed_97
    @property
    def width(this_196) -> 'int14':
        return this_196.width_81
    @property
    def height(this_199) -> 'int14':
        return this_199.height_82
    @property
    def snake(this_202) -> 'Sequence15[Point]':
        return this_202.snake_83
    @property
    def direction(this_205) -> 'Direction':
        return this_205.direction_84
    @property
    def food(this_208) -> 'Point':
        return this_208.food_85
    @property
    def score(this_211) -> 'int14':
        return this_211.score_86
    @property
    def status(this_214) -> 'GameStatus':
        return this_214.status_87
    @property
    def rng_seed(this_217) -> 'int14':
        return this_217.rng_seed_88
class FoodPlacement_9:
    point_98: 'Point'
    seed_99: 'int14'
    __slots__ = ('point_98', 'seed_99')
    def __init__(this_34, point_101: 'Point', seed_102: 'int14') -> None:
        this_34.point_98 = point_101
        this_34.seed_99 = seed_102
    @property
    def point(this_220) -> 'Point':
        return this_220.point_98
    @property
    def seed(this_223) -> 'int14':
        return this_223.seed_99
def move(head_44: 'Point', body_45: 'Sequence15[Point]', food_46: 'Point', width_47: 'int14', height_48: 'int14') -> 'Direction':
    return Right()
def point_equals(a_61: 'Point', b_62: 'Point') -> 'bool16':
    return_25: 'bool16'
    t_944: 'int14'
    t_945: 'int14'
    if a_61.x == b_62.x:
        t_944 = a_61.y
        t_945 = b_62.y
        return_25 = t_944 == t_945
    else:
        return_25 = False
    return return_25
def is_opposite(a_64: 'Direction', b_65: 'Direction') -> 'bool16':
    return_26: 'bool16'
    if isinstance17(a_64, Up):
        return_26 = isinstance17(b_65, Down)
    elif isinstance17(a_64, Down):
        return_26 = isinstance17(b_65, Up)
    elif isinstance17(a_64, Left):
        return_26 = isinstance17(b_65, Right)
    elif isinstance17(a_64, Right):
        return_26 = isinstance17(b_65, Left)
    else:
        return_26 = False
    return return_26
def direction_delta(dir_67: 'Direction') -> 'Point':
    return_27: 'Point'
    if isinstance17(dir_67, Up):
        return_27 = Point(0, -1)
    elif isinstance17(dir_67, Down):
        return_27 = Point(0, 1)
    elif isinstance17(dir_67, Left):
        return_27 = Point(-1, 0)
    elif isinstance17(dir_67, Right):
        return_27 = Point(1, 0)
    else:
        return_27 = Point(0, 0)
    return return_27
def next_random(seed_74: 'int14', max_75: 'int14') -> 'RandomResult':
    t_587: 'int14'
    t_589: 'int14'
    raw_77: 'int14' = int_add_947(int_mul_948(seed_74, 1664525), 1013904223)
    masked_78: 'int14' = raw_77 & 2147483647
    pos_val_79: 'int14'
    if masked_78 < 0:
        pos_val_79 = int_negate_949(masked_78)
    else:
        pos_val_79 = masked_78
    value_80: 'int14' = 0
    if max_75 > 0:
        try:
            t_587 = arith_int_mod_950(pos_val_79, max_75)
            t_589 = t_587
        except Exception18:
            t_589 = 0
        value_80 = t_589
    return RandomResult(value_80, masked_78)
def place_food_42(snake_103: 'Sequence15[Point]', width_104: 'int14', height_105: 'int14', seed_106: 'int14') -> 'FoodPlacement_9':
    return_36: 'FoodPlacement_9'
    t_911: 'int14'
    t_922: 'Point'
    t_552: 'int14'
    t_554: 'int14'
    t_556: 'int14'
    t_558: 'int14'
    with Label19() as fn_107:
        total_cells_108: 'int14' = int_mul_948(width_104, height_105)
        current_seed_109: 'int14' = seed_106
        attempt_110: 'int14' = 0
        while attempt_110 < total_cells_108:
            result_111: 'RandomResult' = next_random(current_seed_109, total_cells_108)
            t_911 = result_111.next_seed
            current_seed_109 = t_911
            px_112: 'int14' = 0
            py_113: 'int14' = 0
            if width_104 > 0:
                try:
                    t_552 = arith_int_mod_950(result_111.value, width_104)
                    t_554 = t_552
                except Exception18:
                    t_554 = 0
                px_112 = t_554
                try:
                    t_556 = int_div_951(result_111.value, width_104)
                    t_558 = t_556
                except Exception18:
                    t_558 = 0
                py_113 = t_558
            candidate_114: 'Point' = Point(px_112, py_113)
            occupied_115: 'bool16' = False
            def fn_910(seg_116: 'Point') -> 'None':
                nonlocal occupied_115
                if point_equals(seg_116, candidate_114):
                    occupied_115 = True
            list_for_each_952(snake_103, fn_910)
            if not occupied_115:
                return_36 = FoodPlacement_9(candidate_114, current_seed_109)
                fn_107.break_()
            attempt_110 = int_add_947(attempt_110, 1)
        y_117: 'int14' = 0
        while y_117 < height_105:
            x_118: 'int14' = 0
            while x_118 < width_104:
                candidate_119: 'Point' = Point(x_118, y_117)
                free_120: 'bool16' = True
                def fn_909(seg_121: 'Point') -> 'None':
                    nonlocal free_120
                    if point_equals(seg_121, candidate_119):
                        free_120 = False
                list_for_each_952(snake_103, fn_909)
                if free_120:
                    return_36 = FoodPlacement_9(candidate_119, current_seed_109)
                    fn_107.break_()
                x_118 = int_add_947(x_118, 1)
            y_117 = int_add_947(y_117, 1)
        t_922 = Point(0, 0)
        return_36 = FoodPlacement_9(t_922, current_seed_109)
    return return_36
def new_game(width_122: 'int14', height_123: 'int14', seed_124: 'int14') -> 'SnakeGame':
    t_535: 'int14'
    t_537: 'int14'
    t_538: 'int14'
    t_540: 'int14'
    center_x_126: 'int14' = 0
    center_y_127: 'int14' = 0
    if width_122 > 0:
        t_535 = int_div_951(width_122, 2)
        t_537 = t_535
        center_x_126 = t_537
    if height_123 > 0:
        t_538 = int_div_951(height_123, 2)
        t_540 = t_538
        center_y_127 = t_540
    snake_128: 'Sequence15[Point]' = (Point(center_x_126, center_y_127), Point(int_sub_953(center_x_126, 1), center_y_127), Point(int_sub_953(center_x_126, 2), center_y_127))
    food_result_129: 'FoodPlacement_9' = place_food_42(snake_128, width_122, height_123, seed_124)
    t_904: 'Right' = Right()
    t_905: 'Point' = food_result_129.point
    t_906: 'Playing' = Playing()
    t_907: 'int14' = food_result_129.seed
    return SnakeGame(width_122, height_123, snake_128, t_904, t_905, 0, t_906, t_907)
def change_direction(game_130: 'SnakeGame', dir_131: 'Direction') -> 'SnakeGame':
    return_38: 'SnakeGame'
    t_892: 'int14'
    t_893: 'int14'
    t_894: 'Sequence15[Point]'
    t_895: 'Point'
    t_896: 'int14'
    t_897: 'GameStatus'
    t_898: 'int14'
    if is_opposite(game_130.direction, dir_131):
        return_38 = game_130
    else:
        t_892 = game_130.width
        t_893 = game_130.height
        t_894 = game_130.snake
        t_895 = game_130.food
        t_896 = game_130.score
        t_897 = game_130.status
        t_898 = game_130.rng_seed
        return_38 = SnakeGame(t_892, t_893, t_894, dir_131, t_895, t_896, t_897, t_898)
    return return_38
def tick(game_133: 'SnakeGame') -> 'SnakeGame':
    return_39: 'SnakeGame'
    t_832: 'int14'
    t_833: 'int14'
    t_834: 'int14'
    t_835: 'int14'
    t_836: 'Sequence15[Point]'
    t_837: 'Direction'
    t_838: 'Point'
    t_839: 'int14'
    t_840: 'GameOver'
    t_841: 'int14'
    t_845: 'int14'
    t_847: 'int14'
    t_848: 'Sequence15[Point]'
    t_849: 'Point'
    t_851: 'int14'
    t_852: 'int14'
    t_853: 'Sequence15[Point]'
    t_854: 'Direction'
    t_855: 'Point'
    t_856: 'int14'
    t_857: 'GameOver'
    t_858: 'int14'
    t_863: 'int14'
    t_865: 'int14'
    t_866: 'Sequence15[Point]'
    t_867: 'Point'
    t_872: 'int14'
    t_873: 'int14'
    t_874: 'int14'
    t_876: 'int14'
    t_877: 'int14'
    t_878: 'Direction'
    t_879: 'Point'
    t_880: 'Playing'
    t_881: 'int14'
    t_883: 'int14'
    t_884: 'int14'
    t_885: 'Direction'
    t_886: 'Point'
    t_887: 'int14'
    t_888: 'GameStatus'
    t_889: 'int14'
    t_462: 'bool16'
    t_463: 'bool16'
    t_464: 'bool16'
    with Label19() as fn_134:
        if isinstance17(game_133.status, GameOver):
            return_39 = game_133
            fn_134.break_()
        delta_135: 'Point' = direction_delta(game_133.direction)
        head_136: 'Point' = list_get_or_954(game_133.snake, 0, Point(0, 0))
        new_head_137: 'Point' = Point(int_add_947(head_136.x, delta_135.x), int_add_947(head_136.y, delta_135.y))
        if new_head_137.x < 0:
            t_464 = True
        else:
            if new_head_137.x >= game_133.width:
                t_463 = True
            else:
                if new_head_137.y < 0:
                    t_462 = True
                else:
                    t_832 = new_head_137.y
                    t_833 = game_133.height
                    t_462 = t_832 >= t_833
                t_463 = t_462
            t_464 = t_463
        if t_464:
            t_834 = game_133.width
            t_835 = game_133.height
            t_836 = game_133.snake
            t_837 = game_133.direction
            t_838 = game_133.food
            t_839 = game_133.score
            t_840 = GameOver()
            t_841 = game_133.rng_seed
            return_39 = SnakeGame(t_834, t_835, t_836, t_837, t_838, t_839, t_840, t_841)
            fn_134.break_()
        eating_138: 'bool16' = point_equals(new_head_137, game_133.food)
        check_length_139: 'int14'
        if eating_138:
            t_845 = len_955(game_133.snake)
            check_length_139 = t_845
        else:
            t_847 = len_955(game_133.snake)
            check_length_139 = int_sub_953(t_847, 1)
        i_140: 'int14' = 0
        while i_140 < check_length_139:
            t_848 = game_133.snake
            t_849 = Point(-1, -1)
            if point_equals(new_head_137, list_get_or_954(t_848, i_140, t_849)):
                t_851 = game_133.width
                t_852 = game_133.height
                t_853 = game_133.snake
                t_854 = game_133.direction
                t_855 = game_133.food
                t_856 = game_133.score
                t_857 = GameOver()
                t_858 = game_133.rng_seed
                return_39 = SnakeGame(t_851, t_852, t_853, t_854, t_855, t_856, t_857, t_858)
                fn_134.break_()
            i_140 = int_add_947(i_140, 1)
        new_snake_builder_141: 'MutableSequence20[Point]' = list_956()
        new_snake_builder_141.append(new_head_137)
        keep_length_142: 'int14'
        if eating_138:
            t_863 = len_955(game_133.snake)
            keep_length_142 = t_863
        else:
            t_865 = len_955(game_133.snake)
            keep_length_142 = int_sub_953(t_865, 1)
        i_143: 'int14' = 0
        while i_143 < keep_length_142:
            t_866 = game_133.snake
            t_867 = Point(0, 0)
            new_snake_builder_141.append(list_get_or_954(t_866, i_143, t_867))
            i_143 = int_add_947(i_143, 1)
        new_snake_144: 'Sequence15[Point]' = tuple_958(new_snake_builder_141)
        if eating_138:
            new_score_145: 'int14' = int_add_947(game_133.score, 1)
            t_872 = game_133.width
            t_873 = game_133.height
            t_874 = game_133.rng_seed
            food_result_146: 'FoodPlacement_9' = place_food_42(new_snake_144, t_872, t_873, t_874)
            t_876 = game_133.width
            t_877 = game_133.height
            t_878 = game_133.direction
            t_879 = food_result_146.point
            t_880 = Playing()
            t_881 = food_result_146.seed
            return_39 = SnakeGame(t_876, t_877, new_snake_144, t_878, t_879, new_score_145, t_880, t_881)
        else:
            t_883 = game_133.width
            t_884 = game_133.height
            t_885 = game_133.direction
            t_886 = game_133.food
            t_887 = game_133.score
            t_888 = game_133.status
            t_889 = game_133.rng_seed
            return_39 = SnakeGame(t_883, t_884, new_snake_144, t_885, t_886, t_887, t_888, t_889)
    return return_39
def cell_char_43(game_156: 'SnakeGame', p_157: 'Point') -> 'str21':
    return_41: 'str21'
    t_811: 'int14'
    t_812: 'Sequence15[Point]'
    t_813: 'Point'
    t_814: 'Point'
    t_815: 'Point'
    with Label19() as fn_158:
        head_159: 'Point' = list_get_or_954(game_156.snake, 0, Point(-1, -1))
        if point_equals(p_157, head_159):
            return_41 = '@'
            fn_158.break_()
        i_160: 'int14' = 1
        while True:
            t_811 = len_955(game_156.snake)
            if not i_160 < t_811:
                break
            t_812 = game_156.snake
            t_813 = Point(-1, -1)
            t_814 = list_get_or_954(t_812, i_160, t_813)
            if point_equals(p_157, t_814):
                return_41 = 'o'
                fn_158.break_()
            i_160 = int_add_947(i_160, 1)
        t_815 = game_156.food
        if point_equals(p_157, t_815):
            return_41 = '*'
            fn_158.break_()
        return_41 = ' '
    return return_41
def render(game_147: 'SnakeGame') -> 'str21':
    t_786: 'int14'
    t_789: 'int14'
    t_791: 'int14'
    t_797: 'int14'
    sb_149: 'list9[str21]' = ['']
    sb_149.append('\x1b[2J\x1b[H')
    sb_149.append('#')
    x_150: 'int14' = 0
    while True:
        t_786 = game_147.width
        if not x_150 < t_786:
            break
        sb_149.append('#')
        x_150 = int_add_947(x_150, 1)
    sb_149.append('#\r\n')
    y_151: 'int14' = 0
    while True:
        t_789 = game_147.height
        if not y_151 < t_789:
            break
        sb_149.append('#')
        x_152: 'int14' = 0
        while True:
            t_791 = game_147.width
            if not x_152 < t_791:
                break
            p_153: 'Point' = Point(x_152, y_151)
            sb_149.append(cell_char_43(game_147, p_153))
            x_152 = int_add_947(x_152, 1)
        sb_149.append('#\r\n')
        y_151 = int_add_947(y_151, 1)
    sb_149.append('#')
    x_154: 'int14' = 0
    while True:
        t_797 = game_147.width
        if not x_154 < t_797:
            break
        sb_149.append('#')
        x_154 = int_add_947(x_154, 1)
    sb_149.append('#\r\n')
    status_text_155: 'str21'
    t_800: 'GameStatus' = game_147.status
    if isinstance17(t_800, Playing):
        status_text_155 = 'Playing'
    elif isinstance17(t_800, GameOver):
        status_text_155 = 'GAME OVER'
    else:
        status_text_155 = ''
    sb_149.append(str_cat_961('Score: ', int_to_string_962(game_147.score), '  ', status_text_155, '\r', '\n'))
    return ''.join(sb_149)
