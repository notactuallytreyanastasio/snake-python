from snake.snake import new_multi_game as new_multi_game_24, multi_tick as multi_tick_25, multi_render as multi_render_26, change_player_direction as change_player_direction_27, is_multi_game_over as is_multi_game_over_28, add_player as add_player_29, player_head_char as player_head_char_30, MultiSnakeGame, PlayerSnake, Direction, Right, Dead, Up, Down, Left
from temper_std.io import terminal_columns as terminal_columns_7, terminal_rows as terminal_rows_8
from temper_std.ws import ws_listen as ws_listen_10, ws_accept as ws_accept_11, ws_send as ws_send_12, ws_recv as ws_recv_13, ws_close as ws_close_14, WsConnection, WsServer
from temper_core import LoggingConsole as LoggingConsole12, adapt_generator_factory as adapt_generator_factory16, std_sleep as std_sleep0, int_sub as int_sub1, list_get_or as list_get_or4, int_add as int_add5, list_get as list_get7, async_launch as async_launch8, int_mul as int_mul9, int_to_string as int_to_string10, str_cat as str_cat11
from builtins import int as int13, bool as bool15, str as str19, Exception as Exception20, isinstance as isinstance25, RuntimeError as RuntimeError26, list as list2, len as len3, tuple as tuple6
from typing import MutableSequence as MutableSequence14, Sequence as Sequence18, Generator as Generator21, Union as Union24
sleep_6 = std_sleep0
int_sub_278 = int_sub1
list_279 = list2
len_280 = len3
list_get_or_281 = list_get_or4
int_add_283 = int_add5
tuple_284 = tuple6
list_get_285 = list_get7
async_launch_286 = async_launch8
int_mul_287 = int_mul9
int_to_string_288 = int_to_string10
str_cat_289 = str_cat11
console_56: 'LoggingConsole12' = LoggingConsole12(__name__)
detected_cols_31: 'int13' = terminal_columns_7()
detected_rows_32: 'int13' = terminal_rows_8()
board_width_33: 'int13'
if detected_cols_31 > 100:
    board_width_33 = int_sub_278(detected_cols_31, 4)
else:
    board_width_33 = 80
board_height_34: 'int13'
if detected_rows_32 > 30:
    board_height_34 = int_sub_278(detected_rows_32, 12)
else:
    board_height_34 = 30
game_35: 'MultiSnakeGame' = new_multi_game_24(board_width_33, board_height_34, 0, 42)
ws_conns_36: 'MutableSequence14[WsConnection]' = list_279()
next_id_37: 'int13' = 0
running_38: 'bool15' = True
@adapt_generator_factory16
def fn_269(do_await_17) -> 'Generator21[empty, None, None]':
    global game_35
    t_250: 'int13'
    t_251: 'Sequence18[PlayerSnake]'
    t_255: 'PlayerSnake'
    t_259: 'Sequence18[Direction]'
    t_260: 'MultiSnakeGame'
    t_263: 'int13'
    try:
        while True:
            if not len_280(game_35.snakes) == 0:
                break
            yield do_await_17(sleep_6(500))
        console_56.log('Game starting!')
        while running_38:
            dirs_49: 'MutableSequence14[Direction]' = list_279()
            i_50: 'int13' = 0
            while True:
                t_250 = len_280(game_35.snakes)
                if not i_50 < t_250:
                    break
                t_251 = game_35.snakes
                t_255 = PlayerSnake(0, (), Right(), 0, Dead())
                snake_51: 'PlayerSnake' = list_get_or_281(t_251, i_50, t_255)
                dirs_49.append(snake_51.direction)
                i_50 = int_add_283(i_50, 1)
            t_259 = tuple_284(dirs_49)
            t_260 = multi_tick_25(game_35, t_259)
            game_35 = t_260
            frame_52: 'str19' = multi_render_26(game_35)
            conns_53: 'Sequence18[WsConnection]' = tuple_284(ws_conns_36)
            ci_54: 'int13' = 0
            while True:
                t_263 = len_280(conns_53)
                if not ci_54 < t_263:
                    break
                try:
                    conn_55: 'WsConnection' = list_get_285(conns_53, ci_54)
                    yield do_await_17(ws_send_12(conn_55, frame_52))
                except Exception20:
                    pass
                ci_54 = int_add_283(ci_54, 1)
            yield do_await_17(sleep_6(200))
    except Exception20:
        pass
async_launch_286(fn_269)
@adapt_generator_factory16
def fn_268(do_await_22) -> 'Generator21[empty, None, None]':
    global game_35, next_id_37
    t_238: 'str19'
    t_132: 'WsConnection'
    try:
        console_56.log('Snake Multiplayer Server')
        console_56.log('Starting on port 8080...')
        server_40: 'WsServer'
        server_40 = yield do_await_22(ws_listen_10(8080))
        console_56.log('Listening on ws://localhost:8080')
        console_56.log('Waiting for players to connect...')
        while running_38:
            t_132 = yield do_await_22(ws_accept_11(server_40))
            ws_41: 'WsConnection' = t_132
            player_id_42: 'int13' = next_id_37
            next_id_37 = int_add_283(next_id_37, 1)
            game_35 = add_player_29(game_35, int_add_283(int_mul_287(player_id_42, 7), 13))
            ws_conns_36.append(ws_41)
            symbol_43: 'str19' = player_head_char_30(player_id_42)
            t_238 = int_to_string_288(player_id_42)
            console_56.log(str_cat_289('Player ', t_238, ' (', symbol_43, ') connected!'))
            conn_id_44: 'int13' = player_id_42
            conn_ws_45: 'WsConnection' = ws_41
            @adapt_generator_factory16
            def fn_231(do_await_23) -> 'Generator21[empty, None, None]':
                global game_35
                t_217: 'bool15'
                t_218: 'Up'
                t_219: 'MultiSnakeGame'
                t_220: 'Down'
                t_221: 'MultiSnakeGame'
                t_222: 'Left'
                t_223: 'MultiSnakeGame'
                t_224: 'Right'
                t_225: 'MultiSnakeGame'
                t_226: 'str19'
                t_116: 'Union24[str19, None]'
                t_127: 'str19'
                try:
                    while running_38:
                        t_116 = yield do_await_23(ws_recv_13(conn_ws_45))
                        msg_47: 'Union24[str19, None]' = t_116
                        if not msg_47 is None:
                            t_217 = isinstance25(msg_47, str19)
                        else:
                            t_217 = False
                        if t_217:
                            if msg_47 is None:
                                raise RuntimeError26()
                            else:
                                t_127 = msg_47
                            if t_127 == 'u':
                                t_218 = Up()
                                t_219 = change_player_direction_27(game_35, conn_id_44, t_218)
                                game_35 = t_219
                            elif t_127 == 'd':
                                t_220 = Down()
                                t_221 = change_player_direction_27(game_35, conn_id_44, t_220)
                                game_35 = t_221
                            elif t_127 == 'l':
                                t_222 = Left()
                                t_223 = change_player_direction_27(game_35, conn_id_44, t_222)
                                game_35 = t_223
                            elif t_127 == 'r':
                                t_224 = Right()
                                t_225 = change_player_direction_27(game_35, conn_id_44, t_224)
                                game_35 = t_225
                        else:
                            t_226 = int_to_string_288(conn_id_44)
                            console_56.log(str_cat_289('Player ', t_226, ' disconnected'))
                            break
                except Exception20:
                    pass
            async_launch_286(fn_231)
    except Exception20:
        pass
async_launch_286(fn_268)
