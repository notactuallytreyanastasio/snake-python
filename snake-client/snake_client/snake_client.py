from temper_std.ws import ws_connect as ws_connect_7, ws_send as ws_send_8, ws_recv as ws_recv_9, ws_close as ws_close_10, WsConnection
from temper_core import LoggingConsole as LoggingConsole2, adapt_generator_factory as adapt_generator_factory4, std_read_line as std_read_line0, async_launch as async_launch1
from builtins import bool as bool3, str as str7, isinstance as isinstance9, RuntimeError as RuntimeError10, Exception as Exception11
from typing import Union as Union6, Generator as Generator12
read_line_6 = std_read_line0
async_launch_107 = async_launch1
console_18: 'LoggingConsole2' = LoggingConsole2(__name__)
connected_11: 'bool3' = True
@adapt_generator_factory4
def fn_102(do_await_5) -> 'Generator12[empty, None, None]':
    global connected_11
    t_96: 'bool3'
    t_61: 'WsConnection'
    t_64: 'Union6[str7, None]'
    t_66: 'str7'
    try:
        console_18.log('Snake Multiplayer Client')
        console_18.log('Connecting to ws://localhost:8080...')
        t_61 = yield do_await_5(ws_connect_7('ws://localhost:8080'))
        ws_14: 'WsConnection' = t_61
        console_18.log('Connected! Use w/a/s/d to move.')
        @adapt_generator_factory4
        def fn_90(do_await_8) -> 'Generator12[empty, None, None]':
            t_86: 'bool3'
            t_49: 'Union6[str7, None]'
            t_59: 'str7'
            try:
                while connected_11:
                    t_49 = yield do_await_8(read_line_6())
                    line_16: 'Union6[str7, None]' = t_49
                    if not line_16 is None:
                        t_86 = isinstance9(line_16, str7)
                    else:
                        t_86 = False
                    if t_86:
                        if line_16 is None:
                            raise RuntimeError10()
                        else:
                            t_59 = line_16
                        if t_59 == 'w':
                            try:
                                yield do_await_8(ws_send_8(ws_14, 'u'))
                            except Exception11:
                                pass
                        elif t_59 == 's':
                            try:
                                yield do_await_8(ws_send_8(ws_14, 'd'))
                            except Exception11:
                                pass
                        elif t_59 == 'a':
                            try:
                                yield do_await_8(ws_send_8(ws_14, 'l'))
                            except Exception11:
                                pass
                        elif t_59 == 'd':
                            try:
                                yield do_await_8(ws_send_8(ws_14, 'r'))
                            except Exception11:
                                pass
                    else:
                        break
            except Exception11:
                pass
        async_launch_107(fn_90)
        while connected_11:
            t_64 = yield do_await_5(ws_recv_9(ws_14))
            msg_17: 'Union6[str7, None]' = t_64
            if not msg_17 is None:
                t_96 = isinstance9(msg_17, str7)
            else:
                t_96 = False
            if t_96:
                if msg_17 is None:
                    raise RuntimeError10()
                else:
                    t_66 = msg_17
                console_18.log(t_66)
            else:
                console_18.log('Disconnected from server.')
                connected_11 = False
        try:
            yield do_await_5(ws_close_10(ws_14))
        except Exception11:
            pass
    except Exception11:
        pass
async_launch_107(fn_102)
