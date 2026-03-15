# Snake (Python)

A terminal snake game written in Python — auto-generated from [Temper](https://temperlang.dev) source code.

## How to Play

**Prerequisites:** Python 3.11+

```bash
git clone https://github.com/notactuallytreyanastasio/snake-python.git
cd snake-python
PYTHONPATH=temper-core:std:snake:snake-game python3 -c "from temper_core import init_simple_logging, await_safe_to_exit; init_simple_logging(); from snake_game import snake_game; await_safe_to_exit()"
```

Use **w/a/s/d** keys to steer the snake. No Enter key needed — input is raw mode.

## What Is This?

This code was not written by a human in Python. It was written once in [Temper](https://temperlang.dev) — a programming language that compiles to JavaScript, Python, Lua, Rust, Java, and C# — and then automatically compiled to Python and published here by CI.

Temper had no way to pause execution or read input. The only I/O was `console.log()`. To play snake, we had to add `sleep(ms)` and `readLine()` to the language itself — modifying the Temper compiler across all six backends.

## What Changed in the Temper Compiler for Python

Python's async model uses `concurrent.futures.Future` with a `ThreadPoolExecutor`. Connected functions run blocking I/O on worker threads and resolve futures when done.

**Compiler changes** (`PySupportNetwork.kt`): `StdSleep` and `StdReadLine` registered as `PySeparateCode` entries pointing to runtime functions.

**Runtime** (`temper_core/__init__.py`): `std_sleep` submits a `time.sleep()` call to the thread pool. `std_read_line` uses `tty.setraw()` + `termios` for single-keypress input on Unix, falling back to `input()` on non-TTY. The main thread's generator-based coroutine system picks up resolutions via `_step_async_coro`. Programs need `await_safe_to_exit()` to keep the process alive until all async tasks complete.

## All 6 Backends

The same snake game exists in 6 languages, all generated from [one Temper source](https://github.com/notactuallytreyanastasio/temper_snake):

| Language | Repository |
|----------|------------|
| JavaScript | [snake-js](https://github.com/notactuallytreyanastasio/snake-js) |
| Python | [snake-python](https://github.com/notactuallytreyanastasio/snake-python) |
| Lua | [snake-lua](https://github.com/notactuallytreyanastasio/snake-lua) |
| Rust | [snake-rust](https://github.com/notactuallytreyanastasio/snake-rust) |
| C# | [snake-csharp](https://github.com/notactuallytreyanastasio/snake-csharp) |
| Java | [snake-java](https://github.com/notactuallytreyanastasio/snake-java) |

## Source

- Game source: [notactuallytreyanastasio/temper_snake](https://github.com/notactuallytreyanastasio/temper_snake)
- Compiler branch: [`do-crimes-to-play-snake`](https://github.com/temperlang/temper/tree/do-crimes-to-play-snake) ([PR #376](https://github.com/temperlang/temper/pull/376))

---

*Auto-generated from commit [`a39098b041de1619f89cf75b20e1b9365fc7ee3c`](https://github.com/notactuallytreyanastasio/temper_snake/commit/a39098b041de1619f89cf75b20e1b9365fc7ee3c)*
