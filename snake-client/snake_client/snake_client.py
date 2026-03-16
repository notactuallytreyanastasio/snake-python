from temper_std.ws import ws_connect as ws_connect_7, ws_send as ws_send_8, ws_recv as ws_recv_9, ws_close as ws_close_10, WsConnection
from temper_core import LoggingConsole as LoggingConsole2, adapt_generator_factory as adapt_generator_factory4, std_read_line as std_read_line0, async_launch as async_launch1
from builtins import bool as bool3, str as str7, Exception as Exception8, isinstance as isinstance10, RuntimeError as RuntimeError11
from typing import Union as Union6, Generator as Generator12
read_line_6 = std_read_line0
async_launch_112 = async_launch1
console_18: 'LoggingConsole2' = LoggingConsole2(__name__)
connected_11: 'bool3' = True
@adapt_generator_factory4
def fn_107(do_await_5) -> 'Generator12[empty, None, None]':
    global connected_11
    t_101: 'bool3'
    t_63: 'WsConnection'
    t_69: 'Union6[str7, None]'
    t_71: 'str7'
    try:
        console_18.log('Snake Multiplayer Client')
        console_18.log('Connecting to ws://localhost:8080...')
        t_63 = yield do_await_5(ws_connect_7('ws://localhost:8080'))
        ws_14: 'WsConnection' = t_63
        try:
            yield do_await_5(ws_send_8(ws_14, 'join'))
        except Exception8:
            pass
        console_18.log('Connected! Use w/a/s/d to move.')
        @adapt_generator_factory4
        def fn_95(do_await_9) -> 'Generator12[empty, None, None]':
            t_91: 'bool3'
            t_51: 'Union6[str7, None]'
            t_61: 'str7'
            try:
                while connected_11:
                    t_51 = yield do_await_9(read_line_6())
                    line_16: 'Union6[str7, None]' = t_51
                    if not line_16 is None:
                        t_91 = isinstance10(line_16, str7)
                    else:
                        t_91 = False
                    if t_91:
                        if line_16 is None:
                            raise RuntimeError11()
                        else:
                            t_61 = line_16
                        if t_61 == 'w':
                            try:
                                yield do_await_9(ws_send_8(ws_14, 'u'))
                            except Exception8:
                                pass
                        elif t_61 == 's':
                            try:
                                yield do_await_9(ws_send_8(ws_14, 'd'))
                            except Exception8:
                                pass
                        elif t_61 == 'a':
                            try:
                                yield do_await_9(ws_send_8(ws_14, 'l'))
                            except Exception8:
                                pass
                        elif t_61 == 'd':
                            try:
                                yield do_await_9(ws_send_8(ws_14, 'r'))
                            except Exception8:
                                pass
                    else:
                        break
            except Exception8:
                pass
        async_launch_112(fn_95)
        while connected_11:
            t_69 = yield do_await_5(ws_recv_9(ws_14))
            msg_17: 'Union6[str7, None]' = t_69
            if not msg_17 is None:
                t_101 = isinstance10(msg_17, str7)
            else:
                t_101 = False
            if t_101:
                if msg_17 is None:
                    raise RuntimeError11()
                else:
                    t_71 = msg_17
                console_18.log(t_71)
            else:
                console_18.log('Disconnected from server.')
                connected_11 = False
        try:
            yield do_await_5(ws_close_10(ws_14))
        except Exception8:
            pass
    except Exception8:
        pass
async_launch_112(fn_107)
