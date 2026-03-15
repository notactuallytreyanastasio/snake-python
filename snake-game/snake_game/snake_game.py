from snake.snake import new_game as new_game_16, change_direction as change_direction_17, tick as tick_18, render as render_19, Direction, Right, Up, Down, Left, SnakeGame, Playing
from temper_core import LoggingConsole as LoggingConsole5, adapt_generator_factory as adapt_generator_factory8, std_sleep as std_sleep0, std_read_line as std_read_line1, async_launch as async_launch2, int_to_string as int_to_string3, str_cat as str_cat4
from builtins import str as str6, bool as bool10, isinstance as isinstance11, RuntimeError as RuntimeError12, Exception as Exception13
from typing import Union as Union7, Generator as Generator14
sleep_7 = std_sleep0
read_line_8 = std_read_line1
async_launch_153 = async_launch2
int_to_string_154 = int_to_string3
str_cat_155 = str_cat4
console_28: 'LoggingConsole5' = LoggingConsole5(__name__)
input_direction_20: 'Direction' = Right()
def parse_input_6(line_21: 'str6') -> 'Union7[Direction, None]':
    return_5: 'Union7[Direction, None]'
    if line_21 == 'w':
        return_5 = Up()
    elif line_21 == 's':
        return_5 = Down()
    elif line_21 == 'a':
        return_5 = Left()
    elif line_21 == 'd':
        return_5 = Right()
    else:
        return_5 = None
    return return_5
@adapt_generator_factory8
def fn_145(do_await_9) -> 'Generator14[empty, None, None]':
    global input_direction_20
    t_135: 'bool10'
    t_136: 'bool10'
    t_78: 'Union7[str6, None]'
    t_82: 'str6'
    try:
        while True:
            t_78 = yield do_await_9(read_line_8())
            line_24: 'Union7[str6, None]' = t_78
            if not line_24 is None:
                t_135 = isinstance11(line_24, str6)
            else:
                t_135 = False
            if t_135:
                if line_24 is None:
                    raise RuntimeError12()
                else:
                    t_82 = line_24
                dir_25: 'Union7[Direction, None]' = parse_input_6(t_82)
                if not dir_25 is None:
                    t_136 = isinstance11(dir_25, Direction)
                else:
                    t_136 = False
                if t_136:
                    if dir_25 is None:
                        raise RuntimeError12()
                    else:
                        input_direction_20 = dir_25
            else:
                break
    except Exception13:
        pass
async_launch_153(fn_145)
@adapt_generator_factory8
def fn_144(do_await_15) -> 'Generator14[empty, None, None]':
    t_121: 'SnakeGame'
    t_124: 'SnakeGame'
    t_125: 'str6'
    t_127: 'str6'
    t_130: 'str6'
    try:
        console_28.log('Snake! Use w/a/s/d + Enter to move.')
        console_28.log('Starting in 1 second...')
        yield do_await_15(sleep_7(1000))
        t_121 = new_game_16(20, 10, 42)
        game_27: 'SnakeGame' = t_121
        while True:
            if not isinstance11(game_27.status, Playing):
                break
            game_27 = change_direction_17(game_27, input_direction_20)
            t_124 = tick_18(game_27)
            game_27 = t_124
            t_125 = render_19(game_27)
            console_28.log(t_125)
            yield do_await_15(sleep_7(200))
        t_127 = render_19(game_27)
        console_28.log(t_127)
        t_130 = int_to_string_154(game_27.score)
        console_28.log(str_cat_155('Final score: ', t_130))
    except Exception13:
        pass
async_launch_153(fn_144)
