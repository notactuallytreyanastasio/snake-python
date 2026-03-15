from abc import ABCMeta as ABCMeta13
from builtins import int as int14, bool as bool16, isinstance as isinstance17, Exception as Exception18, str as str21, list as list9, len as len8, tuple as tuple10
from typing import Sequence as Sequence15, MutableSequence as MutableSequence20, Union as Union22
from temper_core import Label as Label19, int_add as int_add0, int_mul as int_mul1, int_negate as int_negate2, arith_int_mod as arith_int_mod3, int_div as int_div4, list_for_each as list_for_each5, int_sub as int_sub6, list_get_or as list_get_or7, str_cat as str_cat11, int_to_string as int_to_string12
int_add_2791 = int_add0
int_mul_2792 = int_mul1
int_negate_2793 = int_negate2
arith_int_mod_2794 = arith_int_mod3
int_div_2795 = int_div4
list_for_each_2796 = list_for_each5
int_sub_2797 = int_sub6
list_get_or_2798 = list_get_or7
len_2799 = len8
list_2800 = list9
tuple_2802 = tuple10
str_cat_2805 = str_cat11
int_to_string_2806 = int_to_string12
class Direction(metaclass = ABCMeta13):
    pass
class Up(Direction):
    __slots__ = ()
    def __init__(this_35) -> None:
        pass
class Down(Direction):
    __slots__ = ()
    def __init__(this_37) -> None:
        pass
class Left(Direction):
    __slots__ = ()
    def __init__(this_39) -> None:
        pass
class Right(Direction):
    __slots__ = ()
    def __init__(this_41) -> None:
        pass
class Point:
    x_107: 'int14'
    y_108: 'int14'
    __slots__ = ('x_107', 'y_108')
    def __init__(this_43, x_110: 'int14', y_111: 'int14') -> None:
        this_43.x_107 = x_110
        this_43.y_108 = y_111
    @property
    def x(this_413) -> 'int14':
        return this_413.x_107
    @property
    def y(this_416) -> 'int14':
        return this_416.y_108
class GameStatus(metaclass = ABCMeta13):
    pass
class Playing(GameStatus):
    __slots__ = ()
    def __init__(this_45) -> None:
        pass
class GameOver(GameStatus):
    __slots__ = ()
    def __init__(this_47) -> None:
        pass
class RandomResult:
    value_122: 'int14'
    next_seed_123: 'int14'
    __slots__ = ('value_122', 'next_seed_123')
    def __init__(this_52, value_125: 'int14', next_seed_126: 'int14') -> None:
        this_52.value_122 = value_125
        this_52.next_seed_123 = next_seed_126
    @property
    def value(this_427) -> 'int14':
        return this_427.value_122
    @property
    def next_seed(this_430) -> 'int14':
        return this_430.next_seed_123
class SnakeGame:
    width_134: 'int14'
    height_135: 'int14'
    snake_136: 'Sequence15[Point]'
    direction_137: 'Direction'
    food_138: 'Point'
    score_139: 'int14'
    status_140: 'GameStatus'
    rng_seed_141: 'int14'
    __slots__ = ('width_134', 'height_135', 'snake_136', 'direction_137', 'food_138', 'score_139', 'status_140', 'rng_seed_141')
    def __init__(this_55, width_143: 'int14', height_144: 'int14', snake_145: 'Sequence15[Point]', direction_146: 'Direction', food_147: 'Point', score_148: 'int14', status_149: 'GameStatus', rng_seed_150: 'int14') -> None:
        this_55.width_134 = width_143
        this_55.height_135 = height_144
        this_55.snake_136 = snake_145
        this_55.direction_137 = direction_146
        this_55.food_138 = food_147
        this_55.score_139 = score_148
        this_55.status_140 = status_149
        this_55.rng_seed_141 = rng_seed_150
    @property
    def width(this_433) -> 'int14':
        return this_433.width_134
    @property
    def height(this_436) -> 'int14':
        return this_436.height_135
    @property
    def snake(this_439) -> 'Sequence15[Point]':
        return this_439.snake_136
    @property
    def direction(this_442) -> 'Direction':
        return this_442.direction_137
    @property
    def food(this_445) -> 'Point':
        return this_445.food_138
    @property
    def score(this_448) -> 'int14':
        return this_448.score_139
    @property
    def status(this_451) -> 'GameStatus':
        return this_451.status_140
    @property
    def rng_seed(this_454) -> 'int14':
        return this_454.rng_seed_141
class FoodPlacement_32:
    point_151: 'Point'
    seed_152: 'int14'
    __slots__ = ('point_151', 'seed_152')
    def __init__(this_58, point_154: 'Point', seed_155: 'int14') -> None:
        this_58.point_151 = point_154
        this_58.seed_152 = seed_155
    @property
    def point(this_457) -> 'Point':
        return this_457.point_151
    @property
    def seed(this_460) -> 'int14':
        return this_460.seed_152
class PlayerStatus(metaclass = ABCMeta13):
    pass
class Alive(PlayerStatus):
    __slots__ = ()
    def __init__(this_66) -> None:
        pass
class Dead(PlayerStatus):
    __slots__ = ()
    def __init__(this_68) -> None:
        pass
class PlayerSnake:
    id_216: 'int14'
    segments_217: 'Sequence15[Point]'
    direction_218: 'Direction'
    score_219: 'int14'
    status_220: 'PlayerStatus'
    __slots__ = ('id_216', 'segments_217', 'direction_218', 'score_219', 'status_220')
    def __init__(this_70, id_222: 'int14', segments_223: 'Sequence15[Point]', direction_224: 'Direction', score_225: 'int14', status_226: 'PlayerStatus') -> None:
        this_70.id_216 = id_222
        this_70.segments_217 = segments_223
        this_70.direction_218 = direction_224
        this_70.score_219 = score_225
        this_70.status_220 = status_226
    @property
    def id(this_466) -> 'int14':
        return this_466.id_216
    @property
    def segments(this_469) -> 'Sequence15[Point]':
        return this_469.segments_217
    @property
    def direction(this_472) -> 'Direction':
        return this_472.direction_218
    @property
    def score(this_475) -> 'int14':
        return this_475.score_219
    @property
    def status(this_478) -> 'PlayerStatus':
        return this_478.status_220
class MultiSnakeGame:
    width_227: 'int14'
    height_228: 'int14'
    snakes_229: 'Sequence15[PlayerSnake]'
    food_230: 'Point'
    rng_seed_231: 'int14'
    tick_count_232: 'int14'
    __slots__ = ('width_227', 'height_228', 'snakes_229', 'food_230', 'rng_seed_231', 'tick_count_232')
    def __init__(this_73, width_234: 'int14', height_235: 'int14', snakes_236: 'Sequence15[PlayerSnake]', food_237: 'Point', rng_seed_238: 'int14', tick_count_239: 'int14') -> None:
        this_73.width_227 = width_234
        this_73.height_228 = height_235
        this_73.snakes_229 = snakes_236
        this_73.food_230 = food_237
        this_73.rng_seed_231 = rng_seed_238
        this_73.tick_count_232 = tick_count_239
    @property
    def width(this_481) -> 'int14':
        return this_481.width_227
    @property
    def height(this_484) -> 'int14':
        return this_484.height_228
    @property
    def snakes(this_487) -> 'Sequence15[PlayerSnake]':
        return this_487.snakes_229
    @property
    def food(this_490) -> 'Point':
        return this_490.food_230
    @property
    def rng_seed(this_493) -> 'int14':
        return this_493.rng_seed_231
    @property
    def tick_count(this_496) -> 'int14':
        return this_496.tick_count_232
class SpawnInfo_33:
    point_256: 'Point'
    direction_257: 'Direction'
    __slots__ = ('point_256', 'direction_257')
    def __init__(this_77, point_259: 'Point', direction_260: 'Direction') -> None:
        this_77.point_256 = point_259
        this_77.direction_257 = direction_260
    @property
    def point(this_499) -> 'Point':
        return this_499.point_256
    @property
    def direction(this_502) -> 'Direction':
        return this_502.direction_257
def move(head_97: 'Point', body_98: 'Sequence15[Point]', food_99: 'Point', width_100: 'int14', height_101: 'int14') -> 'Direction':
    return Right()
def point_equals(a_114: 'Point', b_115: 'Point') -> 'bool16':
    return_49: 'bool16'
    t_2788: 'int14'
    t_2789: 'int14'
    if a_114.x == b_115.x:
        t_2788 = a_114.y
        t_2789 = b_115.y
        return_49 = t_2788 == t_2789
    else:
        return_49 = False
    return return_49
def is_opposite(a_117: 'Direction', b_118: 'Direction') -> 'bool16':
    return_50: 'bool16'
    if isinstance17(a_117, Up):
        return_50 = isinstance17(b_118, Down)
    elif isinstance17(a_117, Down):
        return_50 = isinstance17(b_118, Up)
    elif isinstance17(a_117, Left):
        return_50 = isinstance17(b_118, Right)
    elif isinstance17(a_117, Right):
        return_50 = isinstance17(b_118, Left)
    else:
        return_50 = False
    return return_50
def direction_delta(dir_120: 'Direction') -> 'Point':
    return_51: 'Point'
    if isinstance17(dir_120, Up):
        return_51 = Point(0, -1)
    elif isinstance17(dir_120, Down):
        return_51 = Point(0, 1)
    elif isinstance17(dir_120, Left):
        return_51 = Point(-1, 0)
    elif isinstance17(dir_120, Right):
        return_51 = Point(1, 0)
    else:
        return_51 = Point(0, 0)
    return return_51
def next_random(seed_127: 'int14', max_128: 'int14') -> 'RandomResult':
    t_1684: 'int14'
    t_1686: 'int14'
    raw_130: 'int14' = int_add_2791(int_mul_2792(seed_127, 1664525), 1013904223)
    masked_131: 'int14' = raw_130 & 2147483647
    pos_val_132: 'int14'
    if masked_131 < 0:
        pos_val_132 = int_negate_2793(masked_131)
    else:
        pos_val_132 = masked_131
    value_133: 'int14' = 0
    if max_128 > 0:
        try:
            t_1684 = arith_int_mod_2794(pos_val_132, max_128)
            t_1686 = t_1684
        except Exception18:
            t_1686 = 0
        value_133 = t_1686
    return RandomResult(value_133, masked_131)
def place_food_92(snake_156: 'Sequence15[Point]', width_157: 'int14', height_158: 'int14', seed_159: 'int14') -> 'FoodPlacement_32':
    return_60: 'FoodPlacement_32'
    t_2755: 'int14'
    t_2766: 'Point'
    t_1649: 'int14'
    t_1651: 'int14'
    t_1653: 'int14'
    t_1655: 'int14'
    with Label19() as fn_160:
        total_cells_161: 'int14' = int_mul_2792(width_157, height_158)
        current_seed_162: 'int14' = seed_159
        attempt_163: 'int14' = 0
        while attempt_163 < total_cells_161:
            result_164: 'RandomResult' = next_random(current_seed_162, total_cells_161)
            t_2755 = result_164.next_seed
            current_seed_162 = t_2755
            px_165: 'int14' = 0
            py_166: 'int14' = 0
            if width_157 > 0:
                try:
                    t_1649 = arith_int_mod_2794(result_164.value, width_157)
                    t_1651 = t_1649
                except Exception18:
                    t_1651 = 0
                px_165 = t_1651
                try:
                    t_1653 = int_div_2795(result_164.value, width_157)
                    t_1655 = t_1653
                except Exception18:
                    t_1655 = 0
                py_166 = t_1655
            candidate_167: 'Point' = Point(px_165, py_166)
            occupied_168: 'bool16' = False
            def fn_2754(seg_169: 'Point') -> 'None':
                nonlocal occupied_168
                if point_equals(seg_169, candidate_167):
                    occupied_168 = True
            list_for_each_2796(snake_156, fn_2754)
            if not occupied_168:
                return_60 = FoodPlacement_32(candidate_167, current_seed_162)
                fn_160.break_()
            attempt_163 = int_add_2791(attempt_163, 1)
        y_170: 'int14' = 0
        while y_170 < height_158:
            x_171: 'int14' = 0
            while x_171 < width_157:
                candidate_172: 'Point' = Point(x_171, y_170)
                free_173: 'bool16' = True
                def fn_2753(seg_174: 'Point') -> 'None':
                    nonlocal free_173
                    if point_equals(seg_174, candidate_172):
                        free_173 = False
                list_for_each_2796(snake_156, fn_2753)
                if free_173:
                    return_60 = FoodPlacement_32(candidate_172, current_seed_162)
                    fn_160.break_()
                x_171 = int_add_2791(x_171, 1)
            y_170 = int_add_2791(y_170, 1)
        t_2766 = Point(0, 0)
        return_60 = FoodPlacement_32(t_2766, current_seed_162)
    return return_60
def new_game(width_175: 'int14', height_176: 'int14', seed_177: 'int14') -> 'SnakeGame':
    t_1632: 'int14'
    t_1634: 'int14'
    t_1635: 'int14'
    t_1637: 'int14'
    center_x_179: 'int14' = 0
    center_y_180: 'int14' = 0
    if width_175 > 0:
        t_1632 = int_div_2795(width_175, 2)
        t_1634 = t_1632
        center_x_179 = t_1634
    if height_176 > 0:
        t_1635 = int_div_2795(height_176, 2)
        t_1637 = t_1635
        center_y_180 = t_1637
    snake_181: 'Sequence15[Point]' = (Point(center_x_179, center_y_180), Point(int_sub_2797(center_x_179, 1), center_y_180), Point(int_sub_2797(center_x_179, 2), center_y_180))
    food_result_182: 'FoodPlacement_32' = place_food_92(snake_181, width_175, height_176, seed_177)
    t_2748: 'Right' = Right()
    t_2749: 'Point' = food_result_182.point
    t_2750: 'Playing' = Playing()
    t_2751: 'int14' = food_result_182.seed
    return SnakeGame(width_175, height_176, snake_181, t_2748, t_2749, 0, t_2750, t_2751)
def change_direction(game_183: 'SnakeGame', dir_184: 'Direction') -> 'SnakeGame':
    return_62: 'SnakeGame'
    t_2736: 'int14'
    t_2737: 'int14'
    t_2738: 'Sequence15[Point]'
    t_2739: 'Point'
    t_2740: 'int14'
    t_2741: 'GameStatus'
    t_2742: 'int14'
    if is_opposite(game_183.direction, dir_184):
        return_62 = game_183
    else:
        t_2736 = game_183.width
        t_2737 = game_183.height
        t_2738 = game_183.snake
        t_2739 = game_183.food
        t_2740 = game_183.score
        t_2741 = game_183.status
        t_2742 = game_183.rng_seed
        return_62 = SnakeGame(t_2736, t_2737, t_2738, dir_184, t_2739, t_2740, t_2741, t_2742)
    return return_62
def tick(game_186: 'SnakeGame') -> 'SnakeGame':
    return_63: 'SnakeGame'
    t_2676: 'int14'
    t_2677: 'int14'
    t_2678: 'int14'
    t_2679: 'int14'
    t_2680: 'Sequence15[Point]'
    t_2681: 'Direction'
    t_2682: 'Point'
    t_2683: 'int14'
    t_2684: 'GameOver'
    t_2685: 'int14'
    t_2689: 'int14'
    t_2691: 'int14'
    t_2692: 'Sequence15[Point]'
    t_2693: 'Point'
    t_2695: 'int14'
    t_2696: 'int14'
    t_2697: 'Sequence15[Point]'
    t_2698: 'Direction'
    t_2699: 'Point'
    t_2700: 'int14'
    t_2701: 'GameOver'
    t_2702: 'int14'
    t_2707: 'int14'
    t_2709: 'int14'
    t_2710: 'Sequence15[Point]'
    t_2711: 'Point'
    t_2716: 'int14'
    t_2717: 'int14'
    t_2718: 'int14'
    t_2720: 'int14'
    t_2721: 'int14'
    t_2722: 'Direction'
    t_2723: 'Point'
    t_2724: 'Playing'
    t_2725: 'int14'
    t_2727: 'int14'
    t_2728: 'int14'
    t_2729: 'Direction'
    t_2730: 'Point'
    t_2731: 'int14'
    t_2732: 'GameStatus'
    t_2733: 'int14'
    t_1559: 'bool16'
    t_1560: 'bool16'
    t_1561: 'bool16'
    with Label19() as fn_187:
        if isinstance17(game_186.status, GameOver):
            return_63 = game_186
            fn_187.break_()
        delta_188: 'Point' = direction_delta(game_186.direction)
        head_189: 'Point' = list_get_or_2798(game_186.snake, 0, Point(0, 0))
        new_head_190: 'Point' = Point(int_add_2791(head_189.x, delta_188.x), int_add_2791(head_189.y, delta_188.y))
        if new_head_190.x < 0:
            t_1561 = True
        else:
            if new_head_190.x >= game_186.width:
                t_1560 = True
            else:
                if new_head_190.y < 0:
                    t_1559 = True
                else:
                    t_2676 = new_head_190.y
                    t_2677 = game_186.height
                    t_1559 = t_2676 >= t_2677
                t_1560 = t_1559
            t_1561 = t_1560
        if t_1561:
            t_2678 = game_186.width
            t_2679 = game_186.height
            t_2680 = game_186.snake
            t_2681 = game_186.direction
            t_2682 = game_186.food
            t_2683 = game_186.score
            t_2684 = GameOver()
            t_2685 = game_186.rng_seed
            return_63 = SnakeGame(t_2678, t_2679, t_2680, t_2681, t_2682, t_2683, t_2684, t_2685)
            fn_187.break_()
        eating_191: 'bool16' = point_equals(new_head_190, game_186.food)
        check_length_192: 'int14'
        if eating_191:
            t_2689 = len_2799(game_186.snake)
            check_length_192 = t_2689
        else:
            t_2691 = len_2799(game_186.snake)
            check_length_192 = int_sub_2797(t_2691, 1)
        i_193: 'int14' = 0
        while i_193 < check_length_192:
            t_2692 = game_186.snake
            t_2693 = Point(-1, -1)
            if point_equals(new_head_190, list_get_or_2798(t_2692, i_193, t_2693)):
                t_2695 = game_186.width
                t_2696 = game_186.height
                t_2697 = game_186.snake
                t_2698 = game_186.direction
                t_2699 = game_186.food
                t_2700 = game_186.score
                t_2701 = GameOver()
                t_2702 = game_186.rng_seed
                return_63 = SnakeGame(t_2695, t_2696, t_2697, t_2698, t_2699, t_2700, t_2701, t_2702)
                fn_187.break_()
            i_193 = int_add_2791(i_193, 1)
        new_snake_builder_194: 'MutableSequence20[Point]' = list_2800()
        new_snake_builder_194.append(new_head_190)
        keep_length_195: 'int14'
        if eating_191:
            t_2707 = len_2799(game_186.snake)
            keep_length_195 = t_2707
        else:
            t_2709 = len_2799(game_186.snake)
            keep_length_195 = int_sub_2797(t_2709, 1)
        i_196: 'int14' = 0
        while i_196 < keep_length_195:
            t_2710 = game_186.snake
            t_2711 = Point(0, 0)
            new_snake_builder_194.append(list_get_or_2798(t_2710, i_196, t_2711))
            i_196 = int_add_2791(i_196, 1)
        new_snake_197: 'Sequence15[Point]' = tuple_2802(new_snake_builder_194)
        if eating_191:
            new_score_198: 'int14' = int_add_2791(game_186.score, 1)
            t_2716 = game_186.width
            t_2717 = game_186.height
            t_2718 = game_186.rng_seed
            food_result_199: 'FoodPlacement_32' = place_food_92(new_snake_197, t_2716, t_2717, t_2718)
            t_2720 = game_186.width
            t_2721 = game_186.height
            t_2722 = game_186.direction
            t_2723 = food_result_199.point
            t_2724 = Playing()
            t_2725 = food_result_199.seed
            return_63 = SnakeGame(t_2720, t_2721, new_snake_197, t_2722, t_2723, new_score_198, t_2724, t_2725)
        else:
            t_2727 = game_186.width
            t_2728 = game_186.height
            t_2729 = game_186.direction
            t_2730 = game_186.food
            t_2731 = game_186.score
            t_2732 = game_186.status
            t_2733 = game_186.rng_seed
            return_63 = SnakeGame(t_2727, t_2728, new_snake_197, t_2729, t_2730, t_2731, t_2732, t_2733)
    return return_63
def cell_char_93(game_209: 'SnakeGame', p_210: 'Point') -> 'str21':
    return_65: 'str21'
    t_2655: 'int14'
    t_2656: 'Sequence15[Point]'
    t_2657: 'Point'
    t_2658: 'Point'
    t_2659: 'Point'
    with Label19() as fn_211:
        head_212: 'Point' = list_get_or_2798(game_209.snake, 0, Point(-1, -1))
        if point_equals(p_210, head_212):
            return_65 = '@'
            fn_211.break_()
        i_213: 'int14' = 1
        while True:
            t_2655 = len_2799(game_209.snake)
            if not i_213 < t_2655:
                break
            t_2656 = game_209.snake
            t_2657 = Point(-1, -1)
            t_2658 = list_get_or_2798(t_2656, i_213, t_2657)
            if point_equals(p_210, t_2658):
                return_65 = 'o'
                fn_211.break_()
            i_213 = int_add_2791(i_213, 1)
        t_2659 = game_209.food
        if point_equals(p_210, t_2659):
            return_65 = '*'
            fn_211.break_()
        return_65 = ' '
    return return_65
def render(game_200: 'SnakeGame') -> 'str21':
    t_2630: 'int14'
    t_2633: 'int14'
    t_2635: 'int14'
    t_2641: 'int14'
    sb_202: 'list9[str21]' = ['']
    sb_202.append('\x1b[2J\x1b[H')
    sb_202.append('#')
    x_203: 'int14' = 0
    while True:
        t_2630 = game_200.width
        if not x_203 < t_2630:
            break
        sb_202.append('#')
        x_203 = int_add_2791(x_203, 1)
    sb_202.append('#\r\n')
    y_204: 'int14' = 0
    while True:
        t_2633 = game_200.height
        if not y_204 < t_2633:
            break
        sb_202.append('#')
        x_205: 'int14' = 0
        while True:
            t_2635 = game_200.width
            if not x_205 < t_2635:
                break
            p_206: 'Point' = Point(x_205, y_204)
            sb_202.append(cell_char_93(game_200, p_206))
            x_205 = int_add_2791(x_205, 1)
        sb_202.append('#\r\n')
        y_204 = int_add_2791(y_204, 1)
    sb_202.append('#')
    x_207: 'int14' = 0
    while True:
        t_2641 = game_200.width
        if not x_207 < t_2641:
            break
        sb_202.append('#')
        x_207 = int_add_2791(x_207, 1)
    sb_202.append('#\r\n')
    status_text_208: 'str21'
    t_2644: 'GameStatus' = game_200.status
    if isinstance17(t_2644, Playing):
        status_text_208 = 'Playing'
    elif isinstance17(t_2644, GameOver):
        status_text_208 = 'GAME OVER'
    else:
        status_text_208 = ''
    sb_202.append(str_cat_2805('Score: ', int_to_string_2806(game_200.score), '  ', status_text_208, '\r', '\n'))
    return ''.join(sb_202)
def spawn_position_94(width_261: 'int14', height_262: 'int14', index_263: 'int14', total_264: 'int14') -> 'SpawnInfo_33':
    return_79: 'SpawnInfo_33'
    t_2615: 'Point'
    t_2616: 'Right'
    t_2618: 'Point'
    t_2619: 'Left'
    t_2621: 'Point'
    t_2622: 'Down'
    t_2624: 'Point'
    t_2625: 'Up'
    t_1458: 'int14'
    t_1460: 'int14'
    t_1461: 'int14'
    t_1463: 'int14'
    t_1464: 'int14'
    t_1466: 'int14'
    t_1467: 'int14'
    t_1469: 'int14'
    t_1470: 'int14'
    t_1472: 'int14'
    with Label19() as fn_265:
        cx_266: 'int14' = 0
        cy_267: 'int14' = 0
        if width_261 > 0:
            t_1458 = int_div_2795(width_261, 2)
            t_1460 = t_1458
            cx_266 = t_1460
        if height_262 > 0:
            t_1461 = int_div_2795(height_262, 2)
            t_1463 = t_1461
            cy_267 = t_1463
        qx_268: 'int14' = 0
        qy_269: 'int14' = 0
        if width_261 > 0:
            t_1464 = int_div_2795(width_261, 4)
            t_1466 = t_1464
            qx_268 = t_1466
        if height_262 > 0:
            t_1467 = int_div_2795(height_262, 4)
            t_1469 = t_1467
            qy_269 = t_1469
        slot_270: 'int14' = 0
        if total_264 > 0:
            t_1470 = arith_int_mod_2794(index_263, 4)
            t_1472 = t_1470
            slot_270 = t_1472
        if slot_270 == 0:
            t_2615 = Point(qx_268, cy_267)
            t_2616 = Right()
            return_79 = SpawnInfo_33(t_2615, t_2616)
            fn_265.break_()
        if slot_270 == 1:
            t_2618 = Point(int_sub_2797(int_sub_2797(width_261, qx_268), 1), cy_267)
            t_2619 = Left()
            return_79 = SpawnInfo_33(t_2618, t_2619)
            fn_265.break_()
        if slot_270 == 2:
            t_2621 = Point(cx_266, qy_269)
            t_2622 = Down()
            return_79 = SpawnInfo_33(t_2621, t_2622)
            fn_265.break_()
        t_2624 = Point(cx_266, int_sub_2797(int_sub_2797(height_262, qy_269), 1))
        t_2625 = Up()
        return_79 = SpawnInfo_33(t_2624, t_2625)
    return return_79
def collect_all_segments_95(snakes_271: 'Sequence15[PlayerSnake]') -> 'Sequence15[Point]':
    t_2602: 'int14'
    t_2606: 'PlayerSnake'
    t_2609: 'int14'
    t_2610: 'Sequence15[Point]'
    t_2611: 'Point'
    builder_273: 'MutableSequence20[Point]' = list_2800()
    i_274: 'int14' = 0
    while True:
        t_2602 = len_2799(snakes_271)
        if not i_274 < t_2602:
            break
        t_2606 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_275: 'PlayerSnake' = list_get_or_2798(snakes_271, i_274, t_2606)
        j_276: 'int14' = 0
        while True:
            t_2609 = len_2799(snake_275.segments)
            if not j_276 < t_2609:
                break
            t_2610 = snake_275.segments
            t_2611 = Point(0, 0)
            builder_273.append(list_get_or_2798(t_2610, j_276, t_2611))
            j_276 = int_add_2791(j_276, 1)
        i_274 = int_add_2791(i_274, 1)
    return tuple_2802(builder_273)
def new_multi_game(width_240: 'int14', height_241: 'int14', num_players_242: 'int14', seed_243: 'int14') -> 'MultiSnakeGame':
    t_2591: 'Alive'
    snake_builder_245: 'MutableSequence20[PlayerSnake]' = list_2800()
    current_seed_246: 'int14' = seed_243
    i_247: 'int14' = 0
    while i_247 < num_players_242:
        spawn_248: 'SpawnInfo_33' = spawn_position_94(width_240, height_241, i_247, num_players_242)
        dir_249: 'Direction' = spawn_248.direction
        start_x_250: 'int14' = spawn_248.point.x
        start_y_251: 'int14' = spawn_248.point.y
        delta_252: 'Point' = direction_delta(dir_249)
        segments_253: 'Sequence15[Point]' = (Point(start_x_250, start_y_251), Point(int_sub_2797(start_x_250, delta_252.x), int_sub_2797(start_y_251, delta_252.y)), Point(int_sub_2797(start_x_250, int_mul_2792(delta_252.x, 2)), int_sub_2797(start_y_251, int_mul_2792(delta_252.y, 2))))
        t_2591 = Alive()
        snake_builder_245.append(PlayerSnake(i_247, segments_253, dir_249, 0, t_2591))
        i_247 = int_add_2791(i_247, 1)
    t_2594: 'Sequence15[PlayerSnake]' = tuple_2802(snake_builder_245)
    all_segments_254: 'Sequence15[Point]' = collect_all_segments_95(t_2594)
    food_result_255: 'FoodPlacement_32' = place_food_92(all_segments_254, width_240, height_241, current_seed_246)
    t_2597: 'Sequence15[PlayerSnake]' = tuple_2802(snake_builder_245)
    t_2598: 'Point' = food_result_255.point
    t_2599: 'int14' = food_result_255.seed
    return MultiSnakeGame(width_240, height_241, t_2597, t_2598, t_2599, 0)
def multi_tick(game_277: 'MultiSnakeGame', directions_278: 'Sequence15[Direction]') -> 'MultiSnakeGame':
    t_2420: 'int14'
    t_2421: 'Sequence15[PlayerSnake]'
    t_2425: 'PlayerSnake'
    t_2427: 'Direction'
    t_2435: 'int14'
    t_2436: 'Sequence15[PlayerSnake]'
    t_2440: 'PlayerSnake'
    t_2444: 'Sequence15[Direction]'
    t_2445: 'Right'
    t_2463: 'int14'
    t_2464: 'Sequence15[PlayerSnake]'
    t_2468: 'PlayerSnake'
    t_2473: 'Point'
    t_2479: 'int14'
    t_2480: 'int14'
    t_2482: 'int14'
    t_2483: 'Sequence15[Point]'
    t_2484: 'Point'
    t_2487: 'int14'
    t_2488: 'Sequence15[PlayerSnake]'
    t_2492: 'PlayerSnake'
    t_2497: 'int14'
    t_2498: 'Sequence15[Point]'
    t_2499: 'Point'
    t_2502: 'int14'
    t_2503: 'Sequence15[PlayerSnake]'
    t_2507: 'PlayerSnake'
    t_2511: 'Point'
    t_2516: 'int14'
    t_2518: 'Point'
    t_2523: 'int14'
    t_2524: 'Sequence15[PlayerSnake]'
    t_2528: 'PlayerSnake'
    t_2541: 'Point'
    t_2543: 'Direction'
    t_2546: 'int14'
    t_2548: 'int14'
    t_2551: 'Sequence15[Point]'
    t_2552: 'Point'
    t_2555: 'int14'
    t_2556: 'int14'
    t_2566: 'int14'
    t_2567: 'int14'
    t_2568: 'int14'
    t_2570: 'Point'
    t_2571: 'int14'
    t_1320: 'bool16'
    t_1321: 'bool16'
    t_1322: 'bool16'
    t_1392: 'int14'
    t_1400: 'int14'
    new_dirs_280: 'MutableSequence20[Direction]' = list_2800()
    i_281: 'int14' = 0
    while True:
        t_2420 = len_2799(game_277.snakes)
        if not i_281 < t_2420:
            break
        t_2421 = game_277.snakes
        t_2425 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_282: 'PlayerSnake' = list_get_or_2798(t_2421, i_281, t_2425)
        t_2427 = snake_282.direction
        input_dir_283: 'Direction' = list_get_or_2798(directions_278, i_281, t_2427)
        if is_opposite(snake_282.direction, input_dir_283):
            new_dirs_280.append(snake_282.direction)
        else:
            new_dirs_280.append(input_dir_283)
        i_281 = int_add_2791(i_281, 1)
    new_heads_284: 'MutableSequence20[Point]' = list_2800()
    i_285: 'int14' = 0
    while True:
        t_2435 = len_2799(game_277.snakes)
        if not i_285 < t_2435:
            break
        t_2436 = game_277.snakes
        t_2440 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_286: 'PlayerSnake' = list_get_or_2798(t_2436, i_285, t_2440)
        if isinstance17(snake_286.status, Alive):
            t_2444 = tuple_2802(new_dirs_280)
            t_2445 = Right()
            dir_287: 'Direction' = list_get_or_2798(t_2444, i_285, t_2445)
            delta_288: 'Point' = direction_delta(dir_287)
            head_289: 'Point' = list_get_or_2798(snake_286.segments, 0, Point(0, 0))
            new_heads_284.append(Point(int_add_2791(head_289.x, delta_288.x), int_add_2791(head_289.y, delta_288.y)))
        else:
            new_heads_284.append(Point(-1, -1))
        i_285 = int_add_2791(i_285, 1)
    heads_list_290: 'Sequence15[Point]' = tuple_2802(new_heads_284)
    dirs_list_291: 'Sequence15[Direction]' = tuple_2802(new_dirs_280)
    alive_builder_292: 'MutableSequence20[bool16]' = list_2800()
    i_293: 'int14' = 0
    while True:
        t_2463 = len_2799(game_277.snakes)
        if not i_293 < t_2463:
            break
        t_2464 = game_277.snakes
        t_2468 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_294: 'PlayerSnake' = list_get_or_2798(t_2464, i_293, t_2468)
        if not isinstance17(snake_294.status, Alive):
            alive_builder_292.append(False)
        else:
            t_2473 = Point(-1, -1)
            nh_295: 'Point' = list_get_or_2798(heads_list_290, i_293, t_2473)
            dead_296: 'bool16' = False
            if nh_295.x < 0:
                t_1322 = True
            else:
                if nh_295.x >= game_277.width:
                    t_1321 = True
                else:
                    if nh_295.y < 0:
                        t_1320 = True
                    else:
                        t_2479 = nh_295.y
                        t_2480 = game_277.height
                        t_1320 = t_2479 >= t_2480
                    t_1321 = t_1320
                t_1322 = t_1321
            if t_1322:
                dead_296 = True
            if not dead_296:
                s_297: 'int14' = 0
                while True:
                    t_2482 = len_2799(snake_294.segments)
                    if not s_297 < int_sub_2797(t_2482, 1):
                        break
                    t_2483 = snake_294.segments
                    t_2484 = Point(-2, -2)
                    if point_equals(nh_295, list_get_or_2798(t_2483, s_297, t_2484)):
                        dead_296 = True
                    s_297 = int_add_2791(s_297, 1)
            if not dead_296:
                j_298: 'int14' = 0
                while True:
                    t_2487 = len_2799(game_277.snakes)
                    if not j_298 < t_2487:
                        break
                    if j_298 != i_293:
                        t_2488 = game_277.snakes
                        t_2492 = PlayerSnake(0, (), Right(), 0, Dead())
                        other_299: 'PlayerSnake' = list_get_or_2798(t_2488, j_298, t_2492)
                        if isinstance17(other_299.status, Alive):
                            s_300: 'int14' = 0
                            while True:
                                t_2497 = len_2799(other_299.segments)
                                if not s_300 < int_sub_2797(t_2497, 1):
                                    break
                                t_2498 = other_299.segments
                                t_2499 = Point(-2, -2)
                                if point_equals(nh_295, list_get_or_2798(t_2498, s_300, t_2499)):
                                    dead_296 = True
                                s_300 = int_add_2791(s_300, 1)
                    j_298 = int_add_2791(j_298, 1)
            if not dead_296:
                j_301: 'int14' = 0
                while True:
                    t_2502 = len_2799(game_277.snakes)
                    if not j_301 < t_2502:
                        break
                    if j_301 != i_293:
                        t_2503 = game_277.snakes
                        t_2507 = PlayerSnake(0, (), Right(), 0, Dead())
                        other_snake_302: 'PlayerSnake' = list_get_or_2798(t_2503, j_301, t_2507)
                        if isinstance17(other_snake_302.status, Alive):
                            t_2511 = Point(-3, -3)
                            other_head_303: 'Point' = list_get_or_2798(heads_list_290, j_301, t_2511)
                            if point_equals(nh_295, other_head_303):
                                dead_296 = True
                    j_301 = int_add_2791(j_301, 1)
            alive_builder_292.append(not dead_296)
        i_293 = int_add_2791(i_293, 1)
    alive_list_304: 'Sequence15[bool16]' = tuple_2802(alive_builder_292)
    eater_index_305: 'int14' = -1
    i_306: 'int14' = 0
    while True:
        t_2516 = len_2799(game_277.snakes)
        if not i_306 < t_2516:
            break
        if list_get_or_2798(alive_list_304, i_306, False):
            t_2518 = Point(-1, -1)
            nh_307: 'Point' = list_get_or_2798(heads_list_290, i_306, t_2518)
            if point_equals(nh_307, game_277.food):
                eater_index_305 = i_306
        i_306 = int_add_2791(i_306, 1)
    result_snakes_308: 'MutableSequence20[PlayerSnake]' = list_2800()
    i_309: 'int14' = 0
    while True:
        t_2523 = len_2799(game_277.snakes)
        if not i_309 < t_2523:
            break
        t_2524 = game_277.snakes
        t_2528 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_310: 'PlayerSnake' = list_get_or_2798(t_2524, i_309, t_2528)
        if not isinstance17(snake_310.status, Alive):
            result_snakes_308.append(snake_310)
        elif not list_get_or_2798(alive_list_304, i_309, False):
            result_snakes_308.append(PlayerSnake(snake_310.id, snake_310.segments, snake_310.direction, snake_310.score, Dead()))
        else:
            t_2541 = Point(0, 0)
            nh_311: 'Point' = list_get_or_2798(heads_list_290, i_309, t_2541)
            t_2543 = snake_310.direction
            dir_312: 'Direction' = list_get_or_2798(dirs_list_291, i_309, t_2543)
            is_eating_313: 'bool16' = i_309 == eater_index_305
            if is_eating_313:
                t_2546 = len_2799(snake_310.segments)
                t_1392 = t_2546
            else:
                t_2548 = len_2799(snake_310.segments)
                t_1392 = int_sub_2797(t_2548, 1)
            keep_len_314: 'int14' = t_1392
            new_segs_315: 'MutableSequence20[Point]' = list_2800()
            new_segs_315.append(nh_311)
            s_316: 'int14' = 0
            while s_316 < keep_len_314:
                t_2551 = snake_310.segments
                t_2552 = Point(0, 0)
                new_segs_315.append(list_get_or_2798(t_2551, s_316, t_2552))
                s_316 = int_add_2791(s_316, 1)
            if is_eating_313:
                t_2555 = snake_310.score
                t_1400 = int_add_2791(t_2555, 1)
            else:
                t_2556 = snake_310.score
                t_1400 = t_2556
            new_score_317: 'int14' = t_1400
            result_snakes_308.append(PlayerSnake(snake_310.id, tuple_2802(new_segs_315), dir_312, new_score_317, Alive()))
        i_309 = int_add_2791(i_309, 1)
    result_snakes_list_318: 'Sequence15[PlayerSnake]' = tuple_2802(result_snakes_308)
    t_2563: 'Point' = game_277.food
    new_food_319: 'Point' = t_2563
    t_2564: 'int14' = game_277.rng_seed
    new_seed_320: 'int14' = t_2564
    if eater_index_305 >= 0:
        all_segs_321: 'Sequence15[Point]' = collect_all_segments_95(result_snakes_list_318)
        t_2566 = game_277.width
        t_2567 = game_277.height
        t_2568 = game_277.rng_seed
        food_result_322: 'FoodPlacement_32' = place_food_92(all_segs_321, t_2566, t_2567, t_2568)
        t_2570 = food_result_322.point
        new_food_319 = t_2570
        t_2571 = food_result_322.seed
        new_seed_320 = t_2571
    t_2572: 'int14' = game_277.width
    t_2573: 'int14' = game_277.height
    t_2574: 'int14' = game_277.tick_count
    return MultiSnakeGame(t_2572, t_2573, result_snakes_list_318, new_food_319, new_seed_320, int_add_2791(t_2574, 1))
def change_player_direction(game_323: 'MultiSnakeGame', player_id_324: 'int14', dir_325: 'Direction') -> 'MultiSnakeGame':
    t_2393: 'int14'
    t_2394: 'Sequence15[PlayerSnake]'
    t_2398: 'PlayerSnake'
    t_2403: 'Direction'
    t_2404: 'int14'
    t_2405: 'Sequence15[Point]'
    t_2406: 'int14'
    t_2407: 'PlayerStatus'
    t_1245: 'bool16'
    t_1246: 'bool16'
    new_snakes_327: 'MutableSequence20[PlayerSnake]' = list_2800()
    i_328: 'int14' = 0
    while True:
        t_2393 = len_2799(game_323.snakes)
        if not i_328 < t_2393:
            break
        t_2394 = game_323.snakes
        t_2398 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_329: 'PlayerSnake' = list_get_or_2798(t_2394, i_328, t_2398)
        if snake_329.id == player_id_324:
            if isinstance17(snake_329.status, Alive):
                t_2403 = snake_329.direction
                t_1245 = not is_opposite(t_2403, dir_325)
            else:
                t_1245 = False
            t_1246 = t_1245
        else:
            t_1246 = False
        if t_1246:
            t_2404 = snake_329.id
            t_2405 = snake_329.segments
            t_2406 = snake_329.score
            t_2407 = snake_329.status
            new_snakes_327.append(PlayerSnake(t_2404, t_2405, dir_325, t_2406, t_2407))
        else:
            new_snakes_327.append(snake_329)
        i_328 = int_add_2791(i_328, 1)
    return MultiSnakeGame(game_323.width, game_323.height, tuple_2802(new_snakes_327), game_323.food, game_323.rng_seed, game_323.tick_count)
def is_multi_game_over(game_330: 'MultiSnakeGame') -> 'bool16':
    return_83: 'bool16'
    t_2378: 'int14'
    t_2379: 'Sequence15[PlayerSnake]'
    t_2383: 'PlayerSnake'
    alive_count_332: 'int14' = 0
    i_333: 'int14' = 0
    while True:
        t_2378 = len_2799(game_330.snakes)
        if not i_333 < t_2378:
            break
        t_2379 = game_330.snakes
        t_2383 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_334: 'PlayerSnake' = list_get_or_2798(t_2379, i_333, t_2383)
        if isinstance17(snake_334.status, Alive):
            alive_count_332 = int_add_2791(alive_count_332, 1)
        i_333 = int_add_2791(i_333, 1)
    if len_2799(game_330.snakes) == 0:
        return_83 = False
    elif len_2799(game_330.snakes) == 1:
        return_83 = alive_count_332 == 0
    else:
        return_83 = alive_count_332 <= 1
    return return_83
def add_player(game_335: 'MultiSnakeGame', seed_336: 'int14') -> 'MultiSnakeGame':
    t_2356: 'int14'
    t_2357: 'Sequence15[PlayerSnake]'
    t_2361: 'PlayerSnake'
    new_id_338: 'int14' = len_2799(game_335.snakes)
    spawn_339: 'SpawnInfo_33' = spawn_position_94(game_335.width, game_335.height, new_id_338, int_add_2791(new_id_338, 1))
    dir_340: 'Direction' = spawn_339.direction
    delta_341: 'Point' = direction_delta(dir_340)
    start_x_342: 'int14' = spawn_339.point.x
    start_y_343: 'int14' = spawn_339.point.y
    segments_344: 'Sequence15[Point]' = (Point(start_x_342, start_y_343), Point(int_sub_2797(start_x_342, delta_341.x), int_sub_2797(start_y_343, delta_341.y)), Point(int_sub_2797(start_x_342, int_mul_2792(delta_341.x, 2)), int_sub_2797(start_y_343, int_mul_2792(delta_341.y, 2))))
    new_snake_345: 'PlayerSnake' = PlayerSnake(new_id_338, segments_344, dir_340, 0, Alive())
    builder_346: 'MutableSequence20[PlayerSnake]' = list_2800()
    i_347: 'int14' = 0
    while True:
        t_2356 = len_2799(game_335.snakes)
        if not i_347 < t_2356:
            break
        t_2357 = game_335.snakes
        t_2361 = PlayerSnake(0, (), Right(), 0, Dead())
        builder_346.append(list_get_or_2798(t_2357, i_347, t_2361))
        i_347 = int_add_2791(i_347, 1)
    builder_346.append(new_snake_345)
    t_2365: 'Sequence15[PlayerSnake]' = tuple_2802(builder_346)
    all_segs_348: 'Sequence15[Point]' = collect_all_segments_95(t_2365)
    t_2367: 'int14' = game_335.width
    t_2368: 'int14' = game_335.height
    food_result_349: 'FoodPlacement_32' = place_food_92(all_segs_348, t_2367, t_2368, seed_336)
    return MultiSnakeGame(game_335.width, game_335.height, tuple_2802(builder_346), food_result_349.point, food_result_349.seed, game_335.tick_count)
def remove_player(game_350: 'MultiSnakeGame', player_id_351: 'int14') -> 'MultiSnakeGame':
    t_2318: 'int14'
    t_2319: 'Sequence15[PlayerSnake]'
    t_2323: 'PlayerSnake'
    builder_353: 'MutableSequence20[PlayerSnake]' = list_2800()
    i_354: 'int14' = 0
    while True:
        t_2318 = len_2799(game_350.snakes)
        if not i_354 < t_2318:
            break
        t_2319 = game_350.snakes
        t_2323 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_355: 'PlayerSnake' = list_get_or_2798(t_2319, i_354, t_2323)
        if snake_355.id != player_id_351:
            builder_353.append(snake_355)
        i_354 = int_add_2791(i_354, 1)
    return MultiSnakeGame(game_350.width, game_350.height, tuple_2802(builder_353), game_350.food, game_350.rng_seed, game_350.tick_count)
def player_head_char(id_368: 'int14') -> 'str21':
    return_87: 'str21'
    if id_368 == 0:
        return_87 = '@'
    elif id_368 == 1:
        return_87 = '#'
    elif id_368 == 2:
        return_87 = '$'
    elif id_368 == 3:
        return_87 = '%'
    else:
        return_87 = '&'
    return return_87
def player_body_char(id_370: 'int14') -> 'str21':
    return_88: 'str21'
    if id_370 == 0:
        return_88 = 'o'
    elif id_370 == 1:
        return_88 = '+'
    elif id_370 == 2:
        return_88 = '~'
    elif id_370 == 3:
        return_88 = '='
    else:
        return_88 = '.'
    return return_88
def multi_cell_char_96(game_372: 'MultiSnakeGame', p_373: 'Point') -> 'str21':
    return_89: 'str21'
    t_2288: 'int14'
    t_2289: 'Sequence15[PlayerSnake]'
    t_2293: 'PlayerSnake'
    t_2300: 'int14'
    t_2302: 'int14'
    t_2303: 'Sequence15[PlayerSnake]'
    t_2307: 'PlayerSnake'
    t_2310: 'int14'
    t_2311: 'Sequence15[Point]'
    t_2312: 'Point'
    t_2313: 'Point'
    t_2314: 'int14'
    t_2315: 'Point'
    with Label19() as fn_374:
        i_375: 'int14' = 0
        while True:
            t_2288 = len_2799(game_372.snakes)
            if not i_375 < t_2288:
                break
            t_2289 = game_372.snakes
            t_2293 = PlayerSnake(0, (), Right(), 0, Dead())
            snake_376: 'PlayerSnake' = list_get_or_2798(t_2289, i_375, t_2293)
            if len_2799(snake_376.segments) > 0:
                head_377: 'Point' = list_get_or_2798(snake_376.segments, 0, Point(-1, -1))
                if point_equals(p_373, head_377):
                    t_2300 = snake_376.id
                    return_89 = player_head_char(t_2300)
                    fn_374.break_()
            i_375 = int_add_2791(i_375, 1)
        i_378: 'int14' = 0
        while True:
            t_2302 = len_2799(game_372.snakes)
            if not i_378 < t_2302:
                break
            t_2303 = game_372.snakes
            t_2307 = PlayerSnake(0, (), Right(), 0, Dead())
            snake_379: 'PlayerSnake' = list_get_or_2798(t_2303, i_378, t_2307)
            j_380: 'int14' = 1
            while True:
                t_2310 = len_2799(snake_379.segments)
                if not j_380 < t_2310:
                    break
                t_2311 = snake_379.segments
                t_2312 = Point(-1, -1)
                t_2313 = list_get_or_2798(t_2311, j_380, t_2312)
                if point_equals(p_373, t_2313):
                    t_2314 = snake_379.id
                    return_89 = player_body_char(t_2314)
                    fn_374.break_()
                j_380 = int_add_2791(j_380, 1)
            i_378 = int_add_2791(i_378, 1)
        t_2315 = game_372.food
        if point_equals(p_373, t_2315):
            return_89 = '*'
            fn_374.break_()
        return_89 = ' '
    return return_89
def multi_render(game_356: 'MultiSnakeGame') -> 'str21':
    t_2255: 'int14'
    t_2258: 'int14'
    t_2260: 'int14'
    t_2266: 'int14'
    t_2270: 'int14'
    t_2271: 'Sequence15[PlayerSnake]'
    t_2275: 'PlayerSnake'
    t_2277: 'PlayerStatus'
    t_1116: 'str21'
    sb_358: 'list9[str21]' = ['']
    sb_358.append('\x1b[2J\x1b[H')
    sb_358.append('#')
    x_359: 'int14' = 0
    while True:
        t_2255 = game_356.width
        if not x_359 < t_2255:
            break
        sb_358.append('#')
        x_359 = int_add_2791(x_359, 1)
    sb_358.append('#\r\n')
    y_360: 'int14' = 0
    while True:
        t_2258 = game_356.height
        if not y_360 < t_2258:
            break
        sb_358.append('#')
        x_361: 'int14' = 0
        while True:
            t_2260 = game_356.width
            if not x_361 < t_2260:
                break
            p_362: 'Point' = Point(x_361, y_360)
            sb_358.append(multi_cell_char_96(game_356, p_362))
            x_361 = int_add_2791(x_361, 1)
        sb_358.append('#\r\n')
        y_360 = int_add_2791(y_360, 1)
    sb_358.append('#')
    x_363: 'int14' = 0
    while True:
        t_2266 = game_356.width
        if not x_363 < t_2266:
            break
        sb_358.append('#')
        x_363 = int_add_2791(x_363, 1)
    sb_358.append('#\r\n')
    i_364: 'int14' = 0
    while True:
        t_2270 = len_2799(game_356.snakes)
        if not i_364 < t_2270:
            break
        t_2271 = game_356.snakes
        t_2275 = PlayerSnake(0, (), Right(), 0, Dead())
        snake_365: 'PlayerSnake' = list_get_or_2798(t_2271, i_364, t_2275)
        t_2277 = snake_365.status
        if isinstance17(t_2277, Alive):
            t_1116 = 'Playing'
        elif isinstance17(t_2277, Dead):
            t_1116 = 'DEAD'
        else:
            t_1116 = ''
        status_text_366: 'str21' = t_1116
        symbol_367: 'str21' = player_head_char(snake_365.id)
        sb_358.append(str_cat_2805('P', int_to_string_2806(snake_365.id), ' ', symbol_367, ': ', int_to_string_2806(snake_365.score), '  ', status_text_366, '\r', '\n'))
        i_364 = int_add_2791(i_364, 1)
    return ''.join(sb_358)
def direction_to_string(dir_381: 'Direction') -> 'str21':
    return_90: 'str21'
    if isinstance17(dir_381, Up):
        return_90 = 'up'
    elif isinstance17(dir_381, Down):
        return_90 = 'down'
    elif isinstance17(dir_381, Left):
        return_90 = 'left'
    elif isinstance17(dir_381, Right):
        return_90 = 'right'
    else:
        return_90 = 'right'
    return return_90
def string_to_direction(s_383: 'str21') -> 'Union22[Direction, None]':
    return_91: 'Union22[Direction, None]'
    with Label19() as fn_384:
        if s_383 == 'up':
            return_91 = Up()
            fn_384.break_()
        if s_383 == 'down':
            return_91 = Down()
            fn_384.break_()
        if s_383 == 'left':
            return_91 = Left()
            fn_384.break_()
        if s_383 == 'right':
            return_91 = Right()
            fn_384.break_()
        return_91 = None
    return return_91
