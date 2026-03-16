from snake.snake import new_multi_game as new_multi_game_28, multi_tick as multi_tick_29, multi_render as multi_render_30, change_player_direction as change_player_direction_31, is_multi_game_over as is_multi_game_over_32, add_player as add_player_33, player_head_char as player_head_char_34, MultiSnakeGame, PlayerSnake, Direction, Right, Dead, Up, Down, Left
from temper_std.io import terminal_columns as terminal_columns_11, terminal_rows as terminal_rows_12
from temper_std.ws import ws_listen as ws_listen_14, ws_accept as ws_accept_15, ws_send as ws_send_16, ws_recv as ws_recv_17, ws_close as ws_close_18, WsConnection, WsServer
from temper_core import LoggingConsole as LoggingConsole12, adapt_generator_factory as adapt_generator_factory16, std_sleep as std_sleep0, int_sub as int_sub1, list_get_or as list_get_or4, int_add as int_add5, list_for_each as list_for_each7, async_launch as async_launch8, int_mul as int_mul9, int_to_string as int_to_string10, str_cat as str_cat11
from builtins import int as int13, bool as bool15, str as str19, Exception as Exception20, isinstance as isinstance24, RuntimeError as RuntimeError25, list as list2, len as len3, tuple as tuple6
from typing import MutableSequence as MutableSequence14, Sequence as Sequence18, Generator as Generator21, Union as Union23
sleep_10 = std_sleep0
int_sub_339 = int_sub1
list_340 = list2
len_341 = len3
list_get_or_342 = list_get_or4
int_add_344 = int_add5
tuple_345 = tuple6
list_for_each_346 = list_for_each7
async_launch_347 = async_launch8
int_mul_348 = int_mul9
int_to_string_349 = int_to_string10
str_cat_350 = str_cat11
console_61: 'LoggingConsole12' = LoggingConsole12(__name__)
detected_cols_35: 'int13' = terminal_columns_11()
detected_rows_36: 'int13' = terminal_rows_12()
board_width_37: 'int13'
if detected_cols_35 > 100:
    board_width_37 = int_sub_339(detected_cols_35, 4)
else:
    board_width_37 = 80
board_height_38: 'int13'
if detected_rows_36 > 30:
    board_height_38 = int_sub_339(detected_rows_36, 12)
else:
    board_height_38 = 30
game_39: 'MultiSnakeGame' = new_multi_game_28(board_width_37, board_height_38, 0, 42)
ws_conns_40: 'MutableSequence14[WsConnection]' = list_340()
next_id_41: 'int13' = 0
running_42: 'bool15' = True
@adapt_generator_factory16
def fn_330(do_await_17) -> 'Generator21[empty, None, None]':
    global game_39
    t_311: 'int13'
    t_312: 'Sequence18[PlayerSnake]'
    t_316: 'PlayerSnake'
    t_320: 'Sequence18[Direction]'
    t_321: 'MultiSnakeGame'
    try:
        while True:
            if not len_341(game_39.snakes) == 0:
                break
            yield do_await_17(sleep_10(500))
        console_61.log('Game starting!')
        while running_42:
            dirs_55: 'MutableSequence14[Direction]' = list_340()
            i_56: 'int13' = 0
            while True:
                t_311 = len_341(game_39.snakes)
                if not i_56 < t_311:
                    break
                t_312 = game_39.snakes
                t_316 = PlayerSnake(0, (), Right(), 0, Dead())
                snake_57: 'PlayerSnake' = list_get_or_342(t_312, i_56, t_316)
                dirs_55.append(snake_57.direction)
                i_56 = int_add_344(i_56, 1)
            t_320 = tuple_345(dirs_55)
            t_321 = multi_tick_29(game_39, t_320)
            game_39 = t_321
            frame_58: 'str19' = multi_render_30(game_39)
            conns_59: 'Sequence18[WsConnection]' = tuple_345(ws_conns_40)
            def fn_305(conn_60: 'WsConnection') -> 'None':
                ws_send_16(conn_60, frame_58)
            list_for_each_346(conns_59, fn_305)
            yield do_await_17(sleep_10(200))
    except Exception20:
        pass
async_launch_347(fn_330)
@adapt_generator_factory16
def fn_329(do_await_22) -> 'Generator21[empty, None, None]':
    global game_39, next_id_41
    t_284: 'bool15'
    t_287: 'MultiSnakeGame'
    t_289: 'str19'
    t_291: 'bool15'
    t_292: 'Up'
    t_293: 'MultiSnakeGame'
    t_294: 'Down'
    t_295: 'MultiSnakeGame'
    t_296: 'Left'
    t_297: 'MultiSnakeGame'
    t_298: 'Right'
    t_299: 'MultiSnakeGame'
    t_151: 'WsConnection'
    t_152: 'Union23[str19, None]'
    t_154: 'Union23[str19, None]'
    t_156: 'str19'
    t_171: 'str19'
    try:
        console_61.log('Snake Multiplayer Server')
        console_61.log('Starting on port 8080...')
        server_44: 'WsServer'
        server_44 = yield do_await_22(ws_listen_14(8080))
        console_61.log('Listening on ws://localhost:8080')
        console_61.log('Waiting for players to connect...')
        while running_42:
            t_151 = yield do_await_22(ws_accept_15(server_44))
            ws_45: 'WsConnection' = t_151
            try:
                t_152 = yield do_await_22(ws_recv_17(ws_45))
                t_154 = t_152
            except Exception20:
                t_154 = None
            first_msg_raw_46: 'Union23[str19, None]' = t_154
            is_spectator_47: 'bool15' = False
            if not first_msg_raw_46 is None:
                t_284 = isinstance24(first_msg_raw_46, str19)
            else:
                t_284 = False
            if t_284:
                if first_msg_raw_46 is None:
                    raise RuntimeError25()
                else:
                    t_156 = first_msg_raw_46
                if t_156 == 'spectate':
                    is_spectator_47 = True
            if is_spectator_47:
                ws_conns_40.append(ws_45)
                console_61.log('Spectator connected!')
            else:
                player_id_48: 'int13' = next_id_41
                next_id_41 = int_add_344(next_id_41, 1)
                t_287 = add_player_33(game_39, int_add_344(int_mul_348(player_id_48, 7), 13))
                game_39 = t_287
                ws_conns_40.append(ws_45)
                symbol_49: 'str19' = player_head_char_34(player_id_48)
                t_289 = int_to_string_349(player_id_48)
                console_61.log(str_cat_350('Player ', t_289, ' (', symbol_49, ') connected!'))
                if not first_msg_raw_46 is None:
                    t_291 = isinstance24(first_msg_raw_46, str19)
                else:
                    t_291 = False
                if t_291:
                    if first_msg_raw_46 is None:
                        raise RuntimeError25()
                    else:
                        t_171 = first_msg_raw_46
                    if t_171 == 'u':
                        t_292 = Up()
                        t_293 = change_player_direction_31(game_39, player_id_48, t_292)
                        game_39 = t_293
                    elif t_171 == 'd':
                        t_294 = Down()
                        t_295 = change_player_direction_31(game_39, player_id_48, t_294)
                        game_39 = t_295
                    elif t_171 == 'l':
                        t_296 = Left()
                        t_297 = change_player_direction_31(game_39, player_id_48, t_296)
                        game_39 = t_297
                    elif t_171 == 'r':
                        t_298 = Right()
                        t_299 = change_player_direction_31(game_39, player_id_48, t_298)
                        game_39 = t_299
                conn_id_50: 'int13' = player_id_48
                conn_ws_51: 'WsConnection' = ws_45
                @adapt_generator_factory16
                def fn_279(do_await_26) -> 'Generator21[empty, None, None]':
                    global game_39
                    t_265: 'bool15'
                    t_266: 'Up'
                    t_267: 'MultiSnakeGame'
                    t_268: 'Down'
                    t_269: 'MultiSnakeGame'
                    t_270: 'Left'
                    t_271: 'MultiSnakeGame'
                    t_272: 'Right'
                    t_273: 'MultiSnakeGame'
                    t_274: 'str19'
                    t_135: 'Union23[str19, None]'
                    t_146: 'str19'
                    try:
                        while running_42:
                            t_135 = yield do_await_26(ws_recv_17(conn_ws_51))
                            msg_53: 'Union23[str19, None]' = t_135
                            if not msg_53 is None:
                                t_265 = isinstance24(msg_53, str19)
                            else:
                                t_265 = False
                            if t_265:
                                if msg_53 is None:
                                    raise RuntimeError25()
                                else:
                                    t_146 = msg_53
                                if t_146 == 'u':
                                    t_266 = Up()
                                    t_267 = change_player_direction_31(game_39, conn_id_50, t_266)
                                    game_39 = t_267
                                elif t_146 == 'd':
                                    t_268 = Down()
                                    t_269 = change_player_direction_31(game_39, conn_id_50, t_268)
                                    game_39 = t_269
                                elif t_146 == 'l':
                                    t_270 = Left()
                                    t_271 = change_player_direction_31(game_39, conn_id_50, t_270)
                                    game_39 = t_271
                                elif t_146 == 'r':
                                    t_272 = Right()
                                    t_273 = change_player_direction_31(game_39, conn_id_50, t_272)
                                    game_39 = t_273
                            else:
                                t_274 = int_to_string_349(conn_id_50)
                                console_61.log(str_cat_350('Player ', t_274, ' disconnected'))
                                break
                    except Exception20:
                        pass
                async_launch_347(fn_279)
    except Exception20:
        pass
async_launch_347(fn_329)
