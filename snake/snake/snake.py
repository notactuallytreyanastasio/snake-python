from abc import ABCMeta as ABCMeta13
from builtins import int as int14, bool as bool16, isinstance as isinstance17, Exception as Exception18, str as str21, list as list9, len as len8, tuple as tuple10
from typing import Sequence as Sequence15, MutableSequence as MutableSequence20, Union as Union22
from temper_core import Label as Label19, int_add as int_add0, int_mul as int_mul1, int_negate as int_negate2, arith_int_mod as arith_int_mod3, int_div as int_div4, list_for_each as list_for_each5, int_sub as int_sub6, list_get_or as list_get_or7, str_cat as str_cat11, int_to_string as int_to_string12
int_add_2806 = int_add0
int_mul_2807 = int_mul1
int_negate_2808 = int_negate2
arith_int_mod_2809 = arith_int_mod3
int_div_2810 = int_div4
list_for_each_2811 = list_for_each5
int_sub_2812 = int_sub6
list_get_or_2813 = list_get_or7
len_2814 = len8
list_2815 = list9
tuple_2817 = tuple10
str_cat_2820 = str_cat11
int_to_string_2821 = int_to_string12
class Direction(metaclass = ABCMeta13):
    pass
class Up(Direction):
    __slots__ = ()
    def __init__(this_36) -> None:
        pass
class Down(Direction):
    __slots__ = ()
    def __init__(this_38) -> None:
        pass
class Left(Direction):
    __slots__ = ()
    def __init__(this_40) -> None:
        pass
class Right(Direction):
    __slots__ = ()
    def __init__(this_42) -> None:
        pass
class Point:
    x_108: 'int14'
    y_109: 'int14'
    __slots__ = ('x_108', 'y_109')
    def __init__(this_44, x_111: 'int14', y_112: 'int14') -> None:
        this_44.x_108 = x_111
        this_44.y_109 = y_112
    @property
    def x(this_418) -> 'int14':
        return this_418.x_108
    @property
    def y(this_421) -> 'int14':
        return this_421.y_109
class GameStatus(metaclass = ABCMeta13):
    pass
class Playing(GameStatus):
    __slots__ = ()
    def __init__(this_46) -> None:
        pass
class GameOver(GameStatus):
    __slots__ = ()
    def __init__(this_48) -> None:
        pass
class RandomResult:
    value_123: 'int14'
    next_seed_124: 'int14'
    __slots__ = ('value_123', 'next_seed_124')
    def __init__(this_53, value_126: 'int14', next_seed_127: 'int14') -> None:
        this_53.value_123 = value_126
        this_53.next_seed_124 = next_seed_127
    @property
    def value(this_432) -> 'int14':
        return this_432.value_123
    @property
    def next_seed(this_435) -> 'int14':
        return this_435.next_seed_124
class SnakeGame:
    width_135: 'int14'
    height_136: 'int14'
    snake_137: 'Sequence15[Point]'
    direction_138: 'Direction'
    food_139: 'Point'
    score_140: 'int14'
    status_141: 'GameStatus'
    rng_seed_142: 'int14'
    __slots__ = ('width_135', 'height_136', 'snake_137', 'direction_138', 'food_139', 'score_140', 'status_141', 'rng_seed_142')
    def __init__(this_56, width_144: 'int14', height_145: 'int14', snake_146: 'Sequence15[Point]', direction_147: 'Direction', food_148: 'Point', score_149: 'int14', status_150: 'GameStatus', rng_seed_151: 'int14') -> None:
        this_56.width_135 = width_144
        this_56.height_136 = height_145
        this_56.snake_137 = snake_146
        this_56.direction_138 = direction_147
        this_56.food_139 = food_148
        this_56.score_140 = score_149
        this_56.status_141 = status_150
        this_56.rng_seed_142 = rng_seed_151
    @property
    def width(this_438) -> 'int14':
        return this_438.width_135
    @property
    def height(this_441) -> 'int14':
        return this_441.height_136
    @property
    def snake(this_444) -> 'Sequence15[Point]':
        return this_444.snake_137
    @property
    def direction(this_447) -> 'Direction':
        return this_447.direction_138
    @property
    def food(this_450) -> 'Point':
        return this_450.food_139
    @property
    def score(this_453) -> 'int14':
        return this_453.score_140
    @property
    def status(this_456) -> 'GameStatus':
        return this_456.status_141
    @property
    def rng_seed(this_459) -> 'int14':
        return this_459.rng_seed_142
class FoodPlacement_33:
    point_152: 'Point'
    seed_153: 'int14'
    __slots__ = ('point_152', 'seed_153')
    def __init__(this_59, point_155: 'Point', seed_156: 'int14') -> None:
        this_59.point_152 = point_155
        this_59.seed_153 = seed_156
    @property
    def point(this_462) -> 'Point':
        return this_462.point_152
    @property
    def seed(this_465) -> 'int14':
        return this_465.seed_153
class PlayerStatus(metaclass = ABCMeta13):
    pass
class Alive(PlayerStatus):
    __slots__ = ()
    def __init__(this_67) -> None:
        pass
class Dead(PlayerStatus):
    __slots__ = ()
    def __init__(this_69) -> None:
        pass
class PlayerSnake:
    id_217: 'int14'
    segments_218: 'Sequence15[Point]'
    direction_219: 'Direction'
    score_220: 'int14'
    status_221: 'PlayerStatus'
    __slots__ = ('id_217', 'segments_218', 'direction_219', 'score_220', 'status_221')
    def __init__(this_71, id_223: 'int14', segments_224: 'Sequence15[Point]', direction_225: 'Direction', score_226: 'int14', status_227: 'PlayerStatus') -> None:
        this_71.id_217 = id_223
        this_71.segments_218 = segments_224
        this_71.direction_219 = direction_225
        this_71.score_220 = score_226
        this_71.status_221 = status_227
    @property
    def id(this_471) -> 'int14':
        return this_471.id_217
    @property
    def segments(this_474) -> 'Sequence15[Point]':
        return this_474.segments_218
    @property
    def direction(this_477) -> 'Direction':
        return this_477.direction_219
    @property
    def score(this_480) -> 'int14':
        return this_480.score_220
    @property
    def status(this_483) -> 'PlayerStatus':
        return this_483.status_221
class MultiSnakeGame:
    width_228: 'int14'
    height_229: 'int14'
    snakes_230: 'Sequence15[PlayerSnake]'
    food_231: 'Point'
    rng_seed_232: 'int14'
    tick_count_233: 'int14'
    __slots__ = ('width_228', 'height_229', 'snakes_230', 'food_231', 'rng_seed_232', 'tick_count_233')
    def __init__(this_74, width_235: 'int14', height_236: 'int14', snakes_237: 'Sequence15[PlayerSnake]', food_238: 'Point', rng_seed_239: 'int14', tick_count_240: 'int14') -> None:
        this_74.width_228 = width_235
        this_74.height_229 = height_236
        this_74.snakes_230 = snakes_237
        this_74.food_231 = food_238
        this_74.rng_seed_232 = rng_seed_239
        this_74.tick_count_233 = tick_count_240
    @property
    def width(this_486) -> 'int14':
        return this_486.width_228
    @property
    def height(this_489) -> 'int14':
        return this_489.height_229
    @property
    def snakes(this_492) -> 'Sequence15[PlayerSnake]':
        return this_492.snakes_230
    @property
    def food(this_495) -> 'Point':
        return this_495.food_231
    @property
    def rng_seed(this_498) -> 'int14':
        return this_498.rng_seed_232
    @property
    def tick_count(this_501) -> 'int14':
        return this_501.tick_count_233
class SpawnInfo_34:
    point_257: 'Point'
    direction_258: 'Direction'
    __slots__ = ('point_257', 'direction_258')
    def __init__(this_78, point_260: 'Point', direction_261: 'Direction') -> None:
        this_78.point_257 = point_260
        this_78.direction_258 = direction_261
    @property
    def point(this_504) -> 'Point':
        return this_504.point_257
    @property
    def direction(this_507) -> 'Direction':
        return this_507.direction_258
def move(head_98: 'Point', body_99: 'Sequence15[Point]', food_100: 'Point', width_101: 'int14', height_102: 'int14') -> 'Direction':
    return Right()
def point_equals(a_115: 'Point', b_116: 'Point') -> 'bool16':
    return_50: 'bool16'
    t_2803: 'int14'
    t_2804: 'int14'
    if a_115.x == b_116.x:
        t_2803 = a_115.y
        t_2804 = b_116.y
        return_50 = t_2803 == t_2804
    else:
        return_50 = False
    return return_50
def is_opposite(a_118: 'Direction', b_119: 'Direction') -> 'bool16':
    return_51: 'bool16'
    if isinstance17(a_118, Up):
        return_51 = isinstance17(b_119, Down)
    elif isinstance17(a_118, Down):
        return_51 = isinstance17(b_119, Up)
    elif isinstance17(a_118, Left):
        return_51 = isinstance17(b_119, Right)
    elif isinstance17(a_118, Right):
        return_51 = isinstance17(b_119, Left)
    else:
        return_51 = False
    return return_51
def direction_delta(dir_121: 'Direction') -> 'Point':
    return_52: 'Point'
    if isinstance17(dir_121, Up):
        return_52 = Point(0, -1)
    elif isinstance17(dir_121, Down):
        return_52 = Point(0, 1)
    elif isinstance17(dir_121, Left):
        return_52 = Point(-1, 0)
    elif isinstance17(dir_121, Right):
        return_52 = Point(1, 0)
    else:
        return_52 = Point(0, 0)
    return return_52
def next_random(seed_128: 'int14', max_129: 'int14') -> 'RandomResult':
    t_1687: 'int14'
    t_1689: 'int14'
    raw_131: 'int14' = int_add_2806(int_mul_2807(seed_128, 1664525), 1013904223)
    masked_132: 'int14' = raw_131 & 2147483647
    pos_val_133: 'int14'
    if masked_132 < 0:
        pos_val_133 = int_negate_2808(masked_132)
    else:
        pos_val_133 = masked_132
    value_134: 'int14' = 0
    if max_129 > 0:
        try:
            t_1687 = arith_int_mod_2809(pos_val_133, max_129)
            t_1689 = t_1687
        except Exception18:
            t_1689 = 0
        value_134 = t_1689
    return RandomResult(value_134, masked_132)
def place_food_93(snake_157: 'Sequence15[Point]', width_158: 'int14', height_159: 'int14', seed_160: 'int14') -> 'FoodPlacement_33':
    return_61: 'FoodPlacement_33'
    t_2770: 'int14'
    t_2781: 'Point'
    t_1652: 'int14'
    t_1654: 'int14'
    t_1656: 'int14'
    t_1658: 'int14'
    with Label19() as fn_161:
        total_cells_162: 'int14' = int_mul_2807(width_158, height_159)
        current_seed_163: 'int14' = seed_160
        attempt_164: 'int14' = 0
        while attempt_164 < total_cells_162:
            result_165: 'RandomResult' = next_random(current_seed_163, total_cells_162)
            t_2770 = result_165.next_seed
            current_seed_163 = t_2770
            px_166: 'int14' = 0
            py_167: 'int14' = 0
            if width_158 > 0:
                try:
                    t_1652 = arith_int_mod_2809(result_165.value, width_158)
                    t_1654 = t_1652
                except Exception18:
                    t_1654 = 0
                px_166 = t_1654
                try:
                    t_1656 = int_div_2810(result_165.value, width_158)
                    t_1658 = t_1656
                except Exception18:
                    t_1658 = 0
                py_167 = t_1658
            candidate_168: 'Point' = Point(px_166, py_167)
            occupied_169: 'bool16' = False
            def fn_2769(seg_170: 'Point') -> 'None':
                nonlocal occupied_169
                if point_equals(seg_170, candidate_168):
                    occupied_169 = True
            list_for_each_2811(snake_157, fn_2769)
            if not occupied_169:
                return_61 = FoodPlacement_33(candidate_168, current_seed_163)
                fn_161.break_()
            attempt_164 = int_add_2806(attempt_164, 1)
        y_171: 'int14' = 0
        while y_171 < height_159:
            x_172: 'int14' = 0
            while x_172 < width_158:
                candidate_173: 'Point' = Point(x_172, y_171)
                free_174: 'bool16' = True
                def fn_2768(seg_175: 'Point') -> 'None':
                    nonlocal free_174
                    if point_equals(seg_175, candidate_173):
                        free_174 = False
                list_for_each_2811(snake_157, fn_2768)
                if free_174:
                    return_61 = FoodPlacement_33(candidate_173, current_seed_163)
                    fn_161.break_()
                x_172 = int_add_2806(x_172, 1)
            y_171 = int_add_2806(y_171, 1)
        t_2781 = Point(0, 0)
        return_61 = FoodPlacement_33(t_2781, current_seed_163)
    return return_61
def new_game(width_176: 'int14', height_177: 'int14', seed_178: 'int14') -> 'SnakeGame':
    t_1635: 'int14'
    t_1637: 'int14'
    t_1638: 'int14'
    t_1640: 'int14'
    center_x_180: 'int14' = 0
    center_y_181: 'int14' = 0
    if width_176 > 0:
        t_1635 = int_div_2810(width_176, 2)
        t_1637 = t_1635
        center_x_180 = t_1637
    if height_177 > 0:
        t_1638 = int_div_2810(height_177, 2)
        t_1640 = t_1638
        center_y_181 = t_1640
    snake_182: 'Sequence15[Point]' = (Point(center_x_180, center_y_181), Point(int_sub_2812(center_x_180, 1), center_y_181), Point(int_sub_2812(center_x_180, 2), center_y_181))
    food_result_183: 'FoodPlacement_33' = place_food_93(snake_182, width_176, height_177, seed_178)
    t_2763: 'Right' = Right()
    t_2764: 'Point' = food_result_183.point
    t_2765: 'Playing' = Playing()
    t_2766: 'int14' = food_result_183.seed
    return SnakeGame(width_176, height_177, snake_182, t_2763, t_2764, 0, t_2765, t_2766)
def change_direction(game_184: 'SnakeGame', dir_185: 'Direction') -> 'SnakeGame':
    return_63: 'SnakeGame'
    t_2751: 'int14'
    t_2752: 'int14'
    t_2753: 'Sequence15[Point]'
    t_2754: 'Point'
    t_2755: 'int14'
    t_2756: 'GameStatus'
    t_2757: 'int14'
    if is_opposite(game_184.direction, dir_185):
        return_63 = game_184
    else:
        t_2751 = game_184.width
        t_2752 = game_184.height
        t_2753 = game_184.snake
        t_2754 = game_184.food
        t_2755 = game_184.score
        t_2756 = game_184.status
        t_2757 = game_184.rng_seed
        return_63 = SnakeGame(t_2751, t_2752, t_2753, dir_185, t_2754, t_2755, t_2756, t_2757)
    return return_63
def tick(game_187: 'SnakeGame') -> 'SnakeGame':
    return_64: 'SnakeGame'
    t_2691: 'int14'
    t_2692: 'int14'
    t_2693: 'int14'
    t_2694: 'int14'
    t_2695: 'Sequence15[Point]'
    t_2696: 'Direction'
    t_2697: 'Point'
    t_2698: 'int14'
    t_2699: 'GameOver'
    t_2700: 'int14'
    t_2704: 'int14'
    t_2706: 'int14'
    t_2707: 'Sequence15[Point]'
    t_2708: 'Point'
    t_2710: 'int14'
    t_2711: 'int14'
    t_2712: 'Sequence15[Point]'
    t_2713: 'Direction'
    t_2714: 'Point'
    t_2715: 'int14'
    t_2716: 'GameOver'
    t_2717: 'int14'
    t_2722: 'int14'
    t_2724: 'int14'
    t_2725: 'Sequence15[Point]'
    t_2726: 'Point'
    t_2731: 'int14'
    t_2732: 'int14'
    t_2733: 'int14'
    t_2735: 'int14'
    t_2736: 'int14'
    t_2737: 'Direction'
    t_2738: 'Point'
    t_2739: 'Playing'
    t_2740: 'int14'
    t_2742: 'int14'
    t_2743: 'int14'
    t_2744: 'Direction'
    t_2745: 'Point'
    t_2746: 'int14'
    t_2747: 'GameStatus'
    t_2748: 'int14'
    t_1562: 'bool16'
    t_1563: 'bool16'
    t_1564: 'bool16'
    with Label19() as fn_188:
        if isinstance17(game_187.status, GameOver):
            return_64 = game_187
            fn_188.break_()
        delta_189: 'Point' = direction_delta(game_187.direction)
        head_190: 'Point' = list_get_or_2813(game_187.snake, 0, Point(0, 0))
        new_head_191: 'Point' = Point(int_add_2806(head_190.x, delta_189.x), int_add_2806(head_190.y, delta_189.y))
        if new_head_191.x < 0:
            t_1564 = True
        else:
            if new_head_191.x >= game_187.width:
                t_1563 = True
            else:
                if new_head_191.y < 0:
                    t_1562 = True
                else:
                    t_2691 = new_head_191.y
                    t_2692 = game_187.height
                    t_1562 = t_2691 >= t_2692
                t_1563 = t_1562
            t_1564 = t_1563
        if t_1564:
            t_2693 = game_187.width
            t_2694 = game_187.height
            t_2695 = game_187.snake
            t_2696 = game_187.direction
            t_2697 = game_187.food
            t_2698 = game_187.score
            t_2699 = GameOver()
            t_2700 = game_187.rng_seed
            return_64 = SnakeGame(t_2693, t_2694, t_2695, t_2696, t_2697, t_2698, t_2699, t_2700)
            fn_188.break_()
        eating_192: 'bool16' = point_equals(new_head_191, game_187.food)
        check_length_193: 'int14'
        if eating_192:
            t_2704 = len_2814(game_187.snake)
            check_length_193 = t_2704
        else:
            t_2706 = len_2814(game_187.snake)
            check_length_193 = int_sub_2812(t_2706, 1)
        i_194: 'int14' = 0
        while i_194 < check_length_193:
            t_2707 = game_187.snake
            t_2708 = Point(-1, -1)
            if point_equals(new_head_191, list_get_or_2813(t_2707, i_194, t_2708)):
                t_2710 = game_187.width
                t_2711 = game_187.height
                t_2712 = game_187.snake
                t_2713 = game_187.direction
                t_2714 = game_187.food
                t_2715 = game_187.score
                t_2716 = GameOver()
                t_2717 = game_187.rng_seed
                return_64 = SnakeGame(t_2710, t_2711, t_2712, t_2713, t_2714, t_2715, t_2716, t_2717)
                fn_188.break_()
            i_194 = int_add_2806(i_194, 1)
        new_snake_builder_195: 'MutableSequence20[Point]' = list_2815()
        new_snake_builder_195.append(new_head_191)
        keep_length_196: 'int14'
        if eating_192:
            t_2722 = len_2814(game_187.snake)
            keep_length_196 = t_2722
        else:
            t_2724 = len_2814(game_187.snake)
            keep_length_196 = int_sub_2812(t_2724, 1)
        i_197: 'int14' = 0
        while i_197 < keep_length_196:
            t_2725 = game_187.snake
            t_2726 = Point(0, 0)
            new_snake_builder_195.append(list_get_or_2813(t_2725, i_197, t_2726))
            i_197 = int_add_2806(i_197, 1)
        new_snake_198: 'Sequence15[Point]' = tuple_2817(new_snake_builder_195)
        if eating_192:
            new_score_199: 'int14' = int_add_2806(game_187.score, 1)
            t_2731 = game_187.width
            t_2732 = game_187.height
            t_2733 = game_187.rng_seed
            food_result_200: 'FoodPlacement_33' = place_food_93(new_snake_198, t_2731, t_2732, t_2733)
            t_2735 = game_187.width
            t_2736 = game_187.height
            t_2737 = game_187.direction
            t_2738 = food_result_200.point
            t_2739 = Playing()
            t_2740 = food_result_200.seed
            return_64 = SnakeGame(t_2735, t_2736, new_snake_198, t_2737, t_2738, new_score_199, t_2739, t_2740)
        else:
            t_2742 = game_187.width
            t_2743 = game_187.height
            t_2744 = game_187.direction
            t_2745 = game_187.food
            t_2746 = game_187.score
            t_2747 = game_187.status
            t_2748 = game_187.rng_seed
            return_64 = SnakeGame(t_2742, t_2743, new_snake_198, t_2744, t_2745, t_2746, t_2747, t_2748)
    return return_64
def cell_char_94(game_210: 'SnakeGame', p_211: 'Point') -> 'str21':
    return_66: 'str21'
    t_2670: 'int14'
    t_2671: 'Sequence15[Point]'
    t_2672: 'Point'
    t_2673: 'Point'
    t_2674: 'Point'
    with Label19() as fn_212:
        head_213: 'Point' = list_get_or_2813(game_210.snake, 0, Point(-1, -1))
        if point_equals(p_211, head_213):
            return_66 = '@'
            fn_212.break_()
        i_214: 'int14' = 1
        while True:
            t_2670 = len_2814(game_210.snake)
            if not i_214 < t_2670:
                break
            t_2671 = game_210.snake
            t_2672 = Point(-1, -1)
            t_2673 = list_get_or_2813(t_2671, i_214, t_2672)
            if point_equals(p_211, t_2673):
                return_66 = 'o'
                fn_212.break_()
            i_214 = int_add_2806(i_214, 1)
        t_2674 = game_210.food
        if point_equals(p_211, t_2674):
            return_66 = '*'
            fn_212.break_()
        return_66 = ' '
    return return_66
def render(game_201: 'SnakeGame') -> 'str21':
    t_2645: 'int14'
    t_2648: 'int14'
    t_2650: 'int14'
    t_2656: 'int14'
    sb_203: 'list9[str21]' = ['']
    sb_203.append('\x1b[2J\x1b[H')
    sb_203.append('#')
    x_204: 'int14' = 0
    while True:
        t_2645 = game_201.width
        if not x_204 < t_2645:
            break
        sb_203.append('#')
        x_204 = int_add_2806(x_204, 1)
    sb_203.append('#\r\n')
    y_205: 'int14' = 0
    while True:
        t_2648 = game_201.height
        if not y_205 < t_2648:
            break
        sb_203.append('#')
        x_206: 'int14' = 0
        while True:
            t_2650 = game_201.width
            if not x_206 < t_2650:
                break
            p_207: 'Point' = Point(x_206, y_205)
            sb_203.append(cell_char_94(game_201, p_207))
            x_206 = int_add_2806(x_206, 1)
        sb_203.append('#\r\n')
        y_205 = int_add_2806(y_205, 1)
    sb_203.append('#')
    x_208: 'int14' = 0
    while True:
        t_2656 = game_201.width
        if not x_208 < t_2656:
            break
        sb_203.append('#')
        x_208 = int_add_2806(x_208, 1)
    sb_203.append('#\r\n')
    status_text_209: 'str21'
    t_2659: 'GameStatus' = game_201.status
    if isinstance17(t_2659, Playing):
        status_text_209 = 'Playing'
    elif isinstance17(t_2659, GameOver):
        status_text_209 = 'GAME OVER'
    else:
        status_text_209 = ''
    sb_203.append(str_cat_2820('Score: ', int_to_string_2821(game_201.score), '  ', status_text_209, '\r', '\n'))
    return ''.join(sb_203)
def spawn_position_95(width_262: 'int14', height_263: 'int14', index_264: 'int14', seed_265: 'int14') -> 'SpawnInfo_34':
    return_80: 'SpawnInfo_34'
    t_2624: 'Point'
    t_2625: 'Right'
    t_2631: 'Direction'
    t_2633: 'Direction'
    t_2635: 'Direction'
    t_2637: 'Direction'
    t_2639: 'Direction'
    t_2640: 'Point'
    t_1463: 'bool16'
    t_1464: 'int14'
    t_1466: 'int14'
    t_1467: 'int14'
    t_1469: 'int14'
    with Label19() as fn_266:
        buf_267: 'int14' = 5
        safe_w_268: 'int14' = int_sub_2812(width_262, 10)
        safe_h_269: 'int14' = int_sub_2812(height_263, 10)
        if safe_w_268 < 1:
            t_1463 = True
        else:
            t_1463 = safe_h_269 < 1
        if t_1463:
            t_1464 = int_div_2810(width_262, 2)
            t_1466 = t_1464
            t_1467 = int_div_2810(height_263, 2)
            t_1469 = t_1467
            t_2624 = Point(t_1466, t_1469)
            t_2625 = Right()
            return_80 = SpawnInfo_34(t_2624, t_2625)
            fn_266.break_()
        r1_270: 'RandomResult' = next_random(int_add_2806(int_add_2806(int_mul_2807(seed_265, 7), int_mul_2807(index_264, 131)), 37), safe_w_268)
        r2_271: 'RandomResult' = next_random(r1_270.next_seed, safe_h_269)
        x_272: 'int14' = int_add_2806(5, r1_270.value)
        y_273: 'int14' = int_add_2806(5, r2_271.value)
        r3_274: 'RandomResult' = next_random(r2_271.next_seed, 4)
        t_2631 = Right()
        dir_275: 'Direction' = t_2631
        if r3_274.value == 0:
            t_2633 = Right()
            dir_275 = t_2633
        if r3_274.value == 1:
            t_2635 = Left()
            dir_275 = t_2635
        if r3_274.value == 2:
            t_2637 = Down()
            dir_275 = t_2637
        if r3_274.value == 3:
            t_2639 = Up()
            dir_275 = t_2639
        t_2640 = Point(x_272, y_273)
        return_80 = SpawnInfo_34(t_2640, dir_275)
    return return_80
def collect_all_segments_96(snakes_276: 'Sequence15[PlayerSnake]') -> 'Sequence15[Point]':
    t_2611: 'int14'
    t_2615: 'PlayerSnake'
    t_2618: 'int14'
    t_2619: 'Sequence15[Point]'
    t_2620: 'Point'
    builder_278: 'MutableSequence20[Point]' = list_2815()
    i_279: 'int14' = 0
    while True:
        t_2611 = len_2814(snakes_276)
        if not i_279 < t_2611:
            break
        t_2615 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_280: 'PlayerSnake' = list_get_or_2813(snakes_276, i_279, t_2615)
        j_281: 'int14' = 0
        while True:
            t_2618 = len_2814(snake_280.segments)
            if not j_281 < t_2618:
                break
            t_2619 = snake_280.segments
            t_2620 = Point(0, 0)
            builder_278.append(list_get_or_2813(t_2619, j_281, t_2620))
            j_281 = int_add_2806(j_281, 1)
        i_279 = int_add_2806(i_279, 1)
    return tuple_2817(builder_278)
def new_multi_game(width_241: 'int14', height_242: 'int14', num_players_243: 'int14', seed_244: 'int14') -> 'MultiSnakeGame':
    t_2600: 'Alive'
    snake_builder_246: 'MutableSequence20[PlayerSnake]' = list_2815()
    current_seed_247: 'int14' = seed_244
    i_248: 'int14' = 0
    while i_248 < num_players_243:
        spawn_249: 'SpawnInfo_34' = spawn_position_95(width_241, height_242, i_248, current_seed_247)
        dir_250: 'Direction' = spawn_249.direction
        start_x_251: 'int14' = spawn_249.point.x
        start_y_252: 'int14' = spawn_249.point.y
        delta_253: 'Point' = direction_delta(dir_250)
        segments_254: 'Sequence15[Point]' = (Point(start_x_251, start_y_252), Point(int_sub_2812(start_x_251, delta_253.x), int_sub_2812(start_y_252, delta_253.y)), Point(int_sub_2812(start_x_251, int_mul_2807(delta_253.x, 2)), int_sub_2812(start_y_252, int_mul_2807(delta_253.y, 2))))
        t_2600 = Alive()
        snake_builder_246.append(PlayerSnake(i_248, segments_254, dir_250, 0, t_2600))
        i_248 = int_add_2806(i_248, 1)
    t_2603: 'Sequence15[PlayerSnake]' = tuple_2817(snake_builder_246)
    all_segments_255: 'Sequence15[Point]' = collect_all_segments_96(t_2603)
    food_result_256: 'FoodPlacement_33' = place_food_93(all_segments_255, width_241, height_242, current_seed_247)
    t_2606: 'Sequence15[PlayerSnake]' = tuple_2817(snake_builder_246)
    t_2607: 'Point' = food_result_256.point
    t_2608: 'int14' = food_result_256.seed
    return MultiSnakeGame(width_241, height_242, t_2606, t_2607, t_2608, 0)
def multi_tick(game_282: 'MultiSnakeGame', directions_283: 'Sequence15[Direction]') -> 'MultiSnakeGame':
    t_2429: 'int14'
    t_2430: 'Sequence15[PlayerSnake]'
    t_2434: 'PlayerSnake'
    t_2436: 'Direction'
    t_2444: 'int14'
    t_2445: 'Sequence15[PlayerSnake]'
    t_2449: 'PlayerSnake'
    t_2453: 'Sequence15[Direction]'
    t_2454: 'Right'
    t_2472: 'int14'
    t_2473: 'Sequence15[PlayerSnake]'
    t_2477: 'PlayerSnake'
    t_2482: 'Point'
    t_2488: 'int14'
    t_2489: 'int14'
    t_2491: 'int14'
    t_2492: 'Sequence15[Point]'
    t_2493: 'Point'
    t_2496: 'int14'
    t_2497: 'Sequence15[PlayerSnake]'
    t_2501: 'PlayerSnake'
    t_2506: 'int14'
    t_2507: 'Sequence15[Point]'
    t_2508: 'Point'
    t_2511: 'int14'
    t_2512: 'Sequence15[PlayerSnake]'
    t_2516: 'PlayerSnake'
    t_2520: 'Point'
    t_2525: 'int14'
    t_2527: 'Point'
    t_2532: 'int14'
    t_2533: 'Sequence15[PlayerSnake]'
    t_2537: 'PlayerSnake'
    t_2550: 'Point'
    t_2552: 'Direction'
    t_2555: 'int14'
    t_2557: 'int14'
    t_2560: 'Sequence15[Point]'
    t_2561: 'Point'
    t_2564: 'int14'
    t_2565: 'int14'
    t_2575: 'int14'
    t_2576: 'int14'
    t_2577: 'int14'
    t_2579: 'Point'
    t_2580: 'int14'
    t_1325: 'bool16'
    t_1326: 'bool16'
    t_1327: 'bool16'
    t_1397: 'int14'
    t_1405: 'int14'
    new_dirs_285: 'MutableSequence20[Direction]' = list_2815()
    i_286: 'int14' = 0
    while True:
        t_2429 = len_2814(game_282.snakes)
        if not i_286 < t_2429:
            break
        t_2430 = game_282.snakes
        t_2434 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_287: 'PlayerSnake' = list_get_or_2813(t_2430, i_286, t_2434)
        t_2436 = snake_287.direction
        input_dir_288: 'Direction' = list_get_or_2813(directions_283, i_286, t_2436)
        if is_opposite(snake_287.direction, input_dir_288):
            new_dirs_285.append(snake_287.direction)
        else:
            new_dirs_285.append(input_dir_288)
        i_286 = int_add_2806(i_286, 1)
    new_heads_289: 'MutableSequence20[Point]' = list_2815()
    i_290: 'int14' = 0
    while True:
        t_2444 = len_2814(game_282.snakes)
        if not i_290 < t_2444:
            break
        t_2445 = game_282.snakes
        t_2449 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_291: 'PlayerSnake' = list_get_or_2813(t_2445, i_290, t_2449)
        if isinstance17(snake_291.status, Alive):
            t_2453 = tuple_2817(new_dirs_285)
            t_2454 = Right()
            dir_292: 'Direction' = list_get_or_2813(t_2453, i_290, t_2454)
            delta_293: 'Point' = direction_delta(dir_292)
            head_294: 'Point' = list_get_or_2813(snake_291.segments, 0, Point(0, 0))
            new_heads_289.append(Point(int_add_2806(head_294.x, delta_293.x), int_add_2806(head_294.y, delta_293.y)))
        else:
            new_heads_289.append(Point(-1, -1))
        i_290 = int_add_2806(i_290, 1)
    heads_list_295: 'Sequence15[Point]' = tuple_2817(new_heads_289)
    dirs_list_296: 'Sequence15[Direction]' = tuple_2817(new_dirs_285)
    alive_builder_297: 'MutableSequence20[bool16]' = list_2815()
    i_298: 'int14' = 0
    while True:
        t_2472 = len_2814(game_282.snakes)
        if not i_298 < t_2472:
            break
        t_2473 = game_282.snakes
        t_2477 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_299: 'PlayerSnake' = list_get_or_2813(t_2473, i_298, t_2477)
        if not isinstance17(snake_299.status, Alive):
            alive_builder_297.append(False)
        else:
            t_2482 = Point(-1, -1)
            nh_300: 'Point' = list_get_or_2813(heads_list_295, i_298, t_2482)
            dead_301: 'bool16' = False
            if nh_300.x < 0:
                t_1327 = True
            else:
                if nh_300.x >= game_282.width:
                    t_1326 = True
                else:
                    if nh_300.y < 0:
                        t_1325 = True
                    else:
                        t_2488 = nh_300.y
                        t_2489 = game_282.height
                        t_1325 = t_2488 >= t_2489
                    t_1326 = t_1325
                t_1327 = t_1326
            if t_1327:
                dead_301 = True
            if not dead_301:
                s_302: 'int14' = 0
                while True:
                    t_2491 = len_2814(snake_299.segments)
                    if not s_302 < int_sub_2812(t_2491, 1):
                        break
                    t_2492 = snake_299.segments
                    t_2493 = Point(-2, -2)
                    if point_equals(nh_300, list_get_or_2813(t_2492, s_302, t_2493)):
                        dead_301 = True
                    s_302 = int_add_2806(s_302, 1)
            if not dead_301:
                j_303: 'int14' = 0
                while True:
                    t_2496 = len_2814(game_282.snakes)
                    if not j_303 < t_2496:
                        break
                    if j_303 != i_298:
                        t_2497 = game_282.snakes
                        t_2501 = PlayerSnake(0, (), Right(), 0, Dead())
                        other_304: 'PlayerSnake' = list_get_or_2813(t_2497, j_303, t_2501)
                        if isinstance17(other_304.status, Alive):
                            s_305: 'int14' = 0
                            while True:
                                t_2506 = len_2814(other_304.segments)
                                if not s_305 < int_sub_2812(t_2506, 1):
                                    break
                                t_2507 = other_304.segments
                                t_2508 = Point(-2, -2)
                                if point_equals(nh_300, list_get_or_2813(t_2507, s_305, t_2508)):
                                    dead_301 = True
                                s_305 = int_add_2806(s_305, 1)
                    j_303 = int_add_2806(j_303, 1)
            if not dead_301:
                j_306: 'int14' = 0
                while True:
                    t_2511 = len_2814(game_282.snakes)
                    if not j_306 < t_2511:
                        break
                    if j_306 != i_298:
                        t_2512 = game_282.snakes
                        t_2516 = PlayerSnake(0, (), Right(), 0, Dead())
                        other_snake_307: 'PlayerSnake' = list_get_or_2813(t_2512, j_306, t_2516)
                        if isinstance17(other_snake_307.status, Alive):
                            t_2520 = Point(-3, -3)
                            other_head_308: 'Point' = list_get_or_2813(heads_list_295, j_306, t_2520)
                            if point_equals(nh_300, other_head_308):
                                dead_301 = True
                    j_306 = int_add_2806(j_306, 1)
            alive_builder_297.append(not dead_301)
        i_298 = int_add_2806(i_298, 1)
    alive_list_309: 'Sequence15[bool16]' = tuple_2817(alive_builder_297)
    eater_index_310: 'int14' = -1
    i_311: 'int14' = 0
    while True:
        t_2525 = len_2814(game_282.snakes)
        if not i_311 < t_2525:
            break
        if list_get_or_2813(alive_list_309, i_311, False):
            t_2527 = Point(-1, -1)
            nh_312: 'Point' = list_get_or_2813(heads_list_295, i_311, t_2527)
            if point_equals(nh_312, game_282.food):
                eater_index_310 = i_311
        i_311 = int_add_2806(i_311, 1)
    result_snakes_313: 'MutableSequence20[PlayerSnake]' = list_2815()
    i_314: 'int14' = 0
    while True:
        t_2532 = len_2814(game_282.snakes)
        if not i_314 < t_2532:
            break
        t_2533 = game_282.snakes
        t_2537 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_315: 'PlayerSnake' = list_get_or_2813(t_2533, i_314, t_2537)
        if not isinstance17(snake_315.status, Alive):
            result_snakes_313.append(snake_315)
        elif not list_get_or_2813(alive_list_309, i_314, False):
            result_snakes_313.append(PlayerSnake(snake_315.id, snake_315.segments, snake_315.direction, snake_315.score, Dead()))
        else:
            t_2550 = Point(0, 0)
            nh_316: 'Point' = list_get_or_2813(heads_list_295, i_314, t_2550)
            t_2552 = snake_315.direction
            dir_317: 'Direction' = list_get_or_2813(dirs_list_296, i_314, t_2552)
            is_eating_318: 'bool16' = i_314 == eater_index_310
            if is_eating_318:
                t_2555 = len_2814(snake_315.segments)
                t_1397 = t_2555
            else:
                t_2557 = len_2814(snake_315.segments)
                t_1397 = int_sub_2812(t_2557, 1)
            keep_len_319: 'int14' = t_1397
            new_segs_320: 'MutableSequence20[Point]' = list_2815()
            new_segs_320.append(nh_316)
            s_321: 'int14' = 0
            while s_321 < keep_len_319:
                t_2560 = snake_315.segments
                t_2561 = Point(0, 0)
                new_segs_320.append(list_get_or_2813(t_2560, s_321, t_2561))
                s_321 = int_add_2806(s_321, 1)
            if is_eating_318:
                t_2564 = snake_315.score
                t_1405 = int_add_2806(t_2564, 1)
            else:
                t_2565 = snake_315.score
                t_1405 = t_2565
            new_score_322: 'int14' = t_1405
            result_snakes_313.append(PlayerSnake(snake_315.id, tuple_2817(new_segs_320), dir_317, new_score_322, Alive()))
        i_314 = int_add_2806(i_314, 1)
    result_snakes_list_323: 'Sequence15[PlayerSnake]' = tuple_2817(result_snakes_313)
    t_2572: 'Point' = game_282.food
    new_food_324: 'Point' = t_2572
    t_2573: 'int14' = game_282.rng_seed
    new_seed_325: 'int14' = t_2573
    if eater_index_310 >= 0:
        all_segs_326: 'Sequence15[Point]' = collect_all_segments_96(result_snakes_list_323)
        t_2575 = game_282.width
        t_2576 = game_282.height
        t_2577 = game_282.rng_seed
        food_result_327: 'FoodPlacement_33' = place_food_93(all_segs_326, t_2575, t_2576, t_2577)
        t_2579 = food_result_327.point
        new_food_324 = t_2579
        t_2580 = food_result_327.seed
        new_seed_325 = t_2580
    t_2581: 'int14' = game_282.width
    t_2582: 'int14' = game_282.height
    t_2583: 'int14' = game_282.tick_count
    return MultiSnakeGame(t_2581, t_2582, result_snakes_list_323, new_food_324, new_seed_325, int_add_2806(t_2583, 1))
def change_player_direction(game_328: 'MultiSnakeGame', player_id_329: 'int14', dir_330: 'Direction') -> 'MultiSnakeGame':
    t_2402: 'int14'
    t_2403: 'Sequence15[PlayerSnake]'
    t_2407: 'PlayerSnake'
    t_2412: 'Direction'
    t_2413: 'int14'
    t_2414: 'Sequence15[Point]'
    t_2415: 'int14'
    t_2416: 'PlayerStatus'
    t_1250: 'bool16'
    t_1251: 'bool16'
    new_snakes_332: 'MutableSequence20[PlayerSnake]' = list_2815()
    i_333: 'int14' = 0
    while True:
        t_2402 = len_2814(game_328.snakes)
        if not i_333 < t_2402:
            break
        t_2403 = game_328.snakes
        t_2407 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_334: 'PlayerSnake' = list_get_or_2813(t_2403, i_333, t_2407)
        if snake_334.id == player_id_329:
            if isinstance17(snake_334.status, Alive):
                t_2412 = snake_334.direction
                t_1250 = not is_opposite(t_2412, dir_330)
            else:
                t_1250 = False
            t_1251 = t_1250
        else:
            t_1251 = False
        if t_1251:
            t_2413 = snake_334.id
            t_2414 = snake_334.segments
            t_2415 = snake_334.score
            t_2416 = snake_334.status
            new_snakes_332.append(PlayerSnake(t_2413, t_2414, dir_330, t_2415, t_2416))
        else:
            new_snakes_332.append(snake_334)
        i_333 = int_add_2806(i_333, 1)
    return MultiSnakeGame(game_328.width, game_328.height, tuple_2817(new_snakes_332), game_328.food, game_328.rng_seed, game_328.tick_count)
def is_multi_game_over(game_335: 'MultiSnakeGame') -> 'bool16':
    return_84: 'bool16'
    t_2387: 'int14'
    t_2388: 'Sequence15[PlayerSnake]'
    t_2392: 'PlayerSnake'
    alive_count_337: 'int14' = 0
    i_338: 'int14' = 0
    while True:
        t_2387 = len_2814(game_335.snakes)
        if not i_338 < t_2387:
            break
        t_2388 = game_335.snakes
        t_2392 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_339: 'PlayerSnake' = list_get_or_2813(t_2388, i_338, t_2392)
        if isinstance17(snake_339.status, Alive):
            alive_count_337 = int_add_2806(alive_count_337, 1)
        i_338 = int_add_2806(i_338, 1)
    if len_2814(game_335.snakes) == 0:
        return_84 = False
    elif len_2814(game_335.snakes) == 1:
        return_84 = alive_count_337 == 0
    else:
        return_84 = alive_count_337 <= 1
    return return_84
def add_player(game_340: 'MultiSnakeGame', seed_341: 'int14') -> 'MultiSnakeGame':
    t_2365: 'int14'
    t_2366: 'Sequence15[PlayerSnake]'
    t_2370: 'PlayerSnake'
    new_id_343: 'int14' = len_2814(game_340.snakes)
    spawn_344: 'SpawnInfo_34' = spawn_position_95(game_340.width, game_340.height, new_id_343, seed_341)
    dir_345: 'Direction' = spawn_344.direction
    delta_346: 'Point' = direction_delta(dir_345)
    start_x_347: 'int14' = spawn_344.point.x
    start_y_348: 'int14' = spawn_344.point.y
    segments_349: 'Sequence15[Point]' = (Point(start_x_347, start_y_348), Point(int_sub_2812(start_x_347, delta_346.x), int_sub_2812(start_y_348, delta_346.y)), Point(int_sub_2812(start_x_347, int_mul_2807(delta_346.x, 2)), int_sub_2812(start_y_348, int_mul_2807(delta_346.y, 2))))
    new_snake_350: 'PlayerSnake' = PlayerSnake(new_id_343, segments_349, dir_345, 0, Alive())
    builder_351: 'MutableSequence20[PlayerSnake]' = list_2815()
    i_352: 'int14' = 0
    while True:
        t_2365 = len_2814(game_340.snakes)
        if not i_352 < t_2365:
            break
        t_2366 = game_340.snakes
        t_2370 = PlayerSnake(0, (), Right(), 0, Dead())
        builder_351.append(list_get_or_2813(t_2366, i_352, t_2370))
        i_352 = int_add_2806(i_352, 1)
    builder_351.append(new_snake_350)
    t_2374: 'Sequence15[PlayerSnake]' = tuple_2817(builder_351)
    all_segs_353: 'Sequence15[Point]' = collect_all_segments_96(t_2374)
    t_2376: 'int14' = game_340.width
    t_2377: 'int14' = game_340.height
    food_result_354: 'FoodPlacement_33' = place_food_93(all_segs_353, t_2376, t_2377, seed_341)
    return MultiSnakeGame(game_340.width, game_340.height, tuple_2817(builder_351), food_result_354.point, food_result_354.seed, game_340.tick_count)
def remove_player(game_355: 'MultiSnakeGame', player_id_356: 'int14') -> 'MultiSnakeGame':
    t_2327: 'int14'
    t_2328: 'Sequence15[PlayerSnake]'
    t_2332: 'PlayerSnake'
    builder_358: 'MutableSequence20[PlayerSnake]' = list_2815()
    i_359: 'int14' = 0
    while True:
        t_2327 = len_2814(game_355.snakes)
        if not i_359 < t_2327:
            break
        t_2328 = game_355.snakes
        t_2332 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_360: 'PlayerSnake' = list_get_or_2813(t_2328, i_359, t_2332)
        if snake_360.id != player_id_356:
            builder_358.append(snake_360)
        i_359 = int_add_2806(i_359, 1)
    return MultiSnakeGame(game_355.width, game_355.height, tuple_2817(builder_358), game_355.food, game_355.rng_seed, game_355.tick_count)
def player_head_char(id_373: 'int14') -> 'str21':
    return_88: 'str21'
    if id_373 == 0:
        return_88 = '@'
    elif id_373 == 1:
        return_88 = '#'
    elif id_373 == 2:
        return_88 = '$'
    elif id_373 == 3:
        return_88 = '%'
    else:
        return_88 = '&'
    return return_88
def player_body_char(id_375: 'int14') -> 'str21':
    return_89: 'str21'
    if id_375 == 0:
        return_89 = 'o'
    elif id_375 == 1:
        return_89 = '+'
    elif id_375 == 2:
        return_89 = '~'
    elif id_375 == 3:
        return_89 = '='
    else:
        return_89 = '.'
    return return_89
def multi_cell_char_97(game_377: 'MultiSnakeGame', p_378: 'Point') -> 'str21':
    return_90: 'str21'
    t_2297: 'int14'
    t_2298: 'Sequence15[PlayerSnake]'
    t_2302: 'PlayerSnake'
    t_2309: 'int14'
    t_2311: 'int14'
    t_2312: 'Sequence15[PlayerSnake]'
    t_2316: 'PlayerSnake'
    t_2319: 'int14'
    t_2320: 'Sequence15[Point]'
    t_2321: 'Point'
    t_2322: 'Point'
    t_2323: 'int14'
    t_2324: 'Point'
    with Label19() as fn_379:
        i_380: 'int14' = 0
        while True:
            t_2297 = len_2814(game_377.snakes)
            if not i_380 < t_2297:
                break
            t_2298 = game_377.snakes
            t_2302 = PlayerSnake(0, (), Right(), 0, Dead())
            snake_381: 'PlayerSnake' = list_get_or_2813(t_2298, i_380, t_2302)
            if len_2814(snake_381.segments) > 0:
                head_382: 'Point' = list_get_or_2813(snake_381.segments, 0, Point(-1, -1))
                if point_equals(p_378, head_382):
                    t_2309 = snake_381.id
                    return_90 = player_head_char(t_2309)
                    fn_379.break_()
            i_380 = int_add_2806(i_380, 1)
        i_383: 'int14' = 0
        while True:
            t_2311 = len_2814(game_377.snakes)
            if not i_383 < t_2311:
                break
            t_2312 = game_377.snakes
            t_2316 = PlayerSnake(0, (), Right(), 0, Dead())
            snake_384: 'PlayerSnake' = list_get_or_2813(t_2312, i_383, t_2316)
            j_385: 'int14' = 1
            while True:
                t_2319 = len_2814(snake_384.segments)
                if not j_385 < t_2319:
                    break
                t_2320 = snake_384.segments
                t_2321 = Point(-1, -1)
                t_2322 = list_get_or_2813(t_2320, j_385, t_2321)
                if point_equals(p_378, t_2322):
                    t_2323 = snake_384.id
                    return_90 = player_body_char(t_2323)
                    fn_379.break_()
                j_385 = int_add_2806(j_385, 1)
            i_383 = int_add_2806(i_383, 1)
        t_2324 = game_377.food
        if point_equals(p_378, t_2324):
            return_90 = '*'
            fn_379.break_()
        return_90 = ' '
    return return_90
def multi_render(game_361: 'MultiSnakeGame') -> 'str21':
    t_2264: 'int14'
    t_2267: 'int14'
    t_2269: 'int14'
    t_2275: 'int14'
    t_2279: 'int14'
    t_2280: 'Sequence15[PlayerSnake]'
    t_2284: 'PlayerSnake'
    t_2286: 'PlayerStatus'
    t_1121: 'str21'
    sb_363: 'list9[str21]' = ['']
    sb_363.append('\x1b[2J\x1b[H')
    sb_363.append('#')
    x_364: 'int14' = 0
    while True:
        t_2264 = game_361.width
        if not x_364 < t_2264:
            break
        sb_363.append('#')
        x_364 = int_add_2806(x_364, 1)
    sb_363.append('#\r\n')
    y_365: 'int14' = 0
    while True:
        t_2267 = game_361.height
        if not y_365 < t_2267:
            break
        sb_363.append('#')
        x_366: 'int14' = 0
        while True:
            t_2269 = game_361.width
            if not x_366 < t_2269:
                break
            p_367: 'Point' = Point(x_366, y_365)
            sb_363.append(multi_cell_char_97(game_361, p_367))
            x_366 = int_add_2806(x_366, 1)
        sb_363.append('#\r\n')
        y_365 = int_add_2806(y_365, 1)
    sb_363.append('#')
    x_368: 'int14' = 0
    while True:
        t_2275 = game_361.width
        if not x_368 < t_2275:
            break
        sb_363.append('#')
        x_368 = int_add_2806(x_368, 1)
    sb_363.append('#\r\n')
    i_369: 'int14' = 0
    while True:
        t_2279 = len_2814(game_361.snakes)
        if not i_369 < t_2279:
            break
        t_2280 = game_361.snakes
        t_2284 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_370: 'PlayerSnake' = list_get_or_2813(t_2280, i_369, t_2284)
        t_2286 = snake_370.status
        if isinstance17(t_2286, Alive):
            t_1121 = 'Playing'
        elif isinstance17(t_2286, Dead):
            t_1121 = 'DEAD'
        else:
            t_1121 = ''
        status_text_371: 'str21' = t_1121
        symbol_372: 'str21' = player_head_char(snake_370.id)
        sb_363.append(str_cat_2820('P', int_to_string_2821(snake_370.id), ' ', symbol_372, ': ', int_to_string_2821(snake_370.score), '  ', status_text_371, '\r', '\n'))
        i_369 = int_add_2806(i_369, 1)
    return ''.join(sb_363)
def direction_to_string(dir_386: 'Direction') -> 'str21':
    return_91: 'str21'
    if isinstance17(dir_386, Up):
        return_91 = 'up'
    elif isinstance17(dir_386, Down):
        return_91 = 'down'
    elif isinstance17(dir_386, Left):
        return_91 = 'left'
    elif isinstance17(dir_386, Right):
        return_91 = 'right'
    else:
        return_91 = 'right'
    return return_91
def string_to_direction(s_388: 'str21') -> 'Union22[Direction, None]':
    return_92: 'Union22[Direction, None]'
    with Label19() as fn_389:
        if s_388 == 'up':
            return_92 = Up()
            fn_389.break_()
        if s_388 == 'down':
            return_92 = Down()
            fn_389.break_()
        if s_388 == 'left':
            return_92 = Left()
            fn_389.break_()
        if s_388 == 'right':
            return_92 = Right()
            fn_389.break_()
        return_92 = None
    return return_92
