from abc import ABCMeta as ABCMeta5
from builtins import int as int0, RuntimeError as RuntimeError1, str as str4
from concurrent.futures import Future as Future2
from typing import Union as Union3
class WsServer(metaclass = ABCMeta5):
    '*WsServer* is an opaque handle representing a listening WebSocket server.'
class WsConnection(metaclass = ABCMeta5):
    '*WsConnection* is an opaque handle representing a single WebSocket connection.'
def ws_listen(port_6: 'int0') -> 'Future2[WsServer]':
    '*wsListen* starts a WebSocket server on the given port and resolves when\nit is ready to accept connections.\n\nport__6: Int32\n'
    raise RuntimeError1()
def ws_accept(server_8: 'WsServer') -> 'Future2[WsConnection]':
    '*wsAccept* waits for and accepts the next incoming connection on a server.\n\nserver__8: WsServer\n'
    raise RuntimeError1()
def ws_connect(url_10: 'str4') -> 'Future2[WsConnection]':
    '*wsConnect* opens a WebSocket connection to the given URL\n(e.g. `"ws://localhost:8080"`).\n\nurl__10: String\n'
    raise RuntimeError1()
def ws_send(conn_12: 'WsConnection', msg_13: 'str4') -> 'Future2[empty]':
    '*wsSend* sends a text message over a connection.\n\nconn__12: WsConnection\n\nmsg__13: String\n'
    raise RuntimeError1()
def ws_recv(conn_15: 'WsConnection') -> 'Future2[(Union3[str4, None])]':
    '*wsRecv* waits for the next message from a connection.\nReturns `null` if the connection is closed.\n\nconn__15: WsConnection\n'
    raise RuntimeError1()
def ws_close(conn_17: 'WsConnection') -> 'Future2[empty]':
    '*wsClose* closes a connection.\n\nconn__17: WsConnection\n'
    raise RuntimeError1()
