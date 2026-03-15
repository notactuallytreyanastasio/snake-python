# Snake (Python)

A terminal snake game written in Python — auto-generated from [Temper](https://temperlang.dev) source code.

## How to Play

**Prerequisites:** Python 3.8+

```bash
git clone https://github.com/notactuallytreyanastasio/snake-python.git
cd snake-python
PYTHONPATH=temper-core:snake:snake-game python3 -c "from temper_core import init_simple_logging, await_safe_to_exit; init_simple_logging(); from snake_game import snake_game; await_safe_to_exit()"
```

Use **w/a/s/d** keys to steer the snake. No Enter key needed — input is raw mode.

## The Story

This code was not written by a human in Python. It was written once in [Temper](https://github.com/temperlang/temper) — a programming language that compiles to 6 other languages — and then automatically compiled and published here by CI.

The same snake game exists in 6 languages, all generated from [one Temper source](https://github.com/notactuallytreyanastasio/temper_snake):

| Language | Repository |
|----------|------------|
| JavaScript | [snake-js](https://github.com/notactuallytreyanastasio/snake-js) |
| **Python** | **snake-python** (you are here) |
| Lua | [snake-lua](https://github.com/notactuallytreyanastasio/snake-lua) |
| Rust | [snake-rust](https://github.com/notactuallytreyanastasio/snake-rust) |
| C# | [snake-csharp](https://github.com/notactuallytreyanastasio/snake-csharp) |
| Java | [snake-java](https://github.com/notactuallytreyanastasio/snake-java) |

## What We Had to Do to the Compiler

Temper had no way to pause execution or read user input. The only I/O primitive was `console.log()`. To write a game loop that ticks every 200ms and reads keyboard input, we added `sleep()` and `readLine()` to the language itself — across all six compilation backends.

The compiler changes live on the [`do-crimes-to-play-snake`](https://github.com/temperlang/temper/tree/do-crimes-to-play-snake) branch ([PR #376](https://github.com/temperlang/temper/pull/376)).

### The Temper Declaration

Two new `@connected` primitives were added to `std/io` in commit [`0f31c89`](https://github.com/temperlang/temper/commit/0f31c89fabc1c938c6a4d2e72c80af658034aa17):

```temper
@connected("stdSleep")
export let sleep(ms: Int): Promise<Empty> { panic() }

@connected("stdReadLine")
export let readLine(): Promise<String?> { panic() }
```

The `@connected` decorator tells the compiler to replace the `panic()` body with a backend-specific native implementation at compile time.

### What Changed for Python

Python's async model in Temper uses `concurrent.futures.Future` with a `ThreadPoolExecutor`. The existing `_executor` and `new_unbound_promise()` infrastructure (already used by `stdNetSend` in `std/net`) was reused. Two Kotlin compiler files were modified.

**[`PySupportNetwork.kt`](https://github.com/temperlang/temper/blob/0f31c89fabc1c938c6a4d2e72c80af658034aa17/be-py/src/commonMain/kotlin/lang/temper/be/py/PySupportNetwork.kt)** — registered the connected keys as `PySeparateCode` entries pointing to runtime functions:

```diff
 val StdNetSend = PySeparateCode("std_net_send", RUNTIME)
+val StdSleep = PySeparateCode("std_sleep", RUNTIME)
+val StdReadLine = PySeparateCode("std_read_line", RUNTIME)
```

```diff
     "stdNetSend" to StdNetSend,
+    "stdSleep" to StdSleep,
+    "stdReadLine" to StdReadLine,
 )
```

**[`temper_core/__init__.py`](https://github.com/temperlang/temper/blob/0f31c89fabc1c938c6a4d2e72c80af658034aa17/be-py/src/commonMain/resources/lang/temper/be/py/temper-core/temper_core/__init__.py)** — the native runtime implementation (this file ships inside `temper-core/` in this repo):

```python
import time as _time

def std_sleep(ms: int) -> 'Future[None]':
    f: Future[None] = new_unbound_promise()
    def _do_sleep():
        _time.sleep(ms / 1000.0)
        f.set_result(None)
    _executor.submit(_do_sleep)
    return f

def std_read_line() -> 'Future[Optional[str]]':
    f: 'Future[Optional[str]]' = new_unbound_promise()
    def _do_read():
        try:
            line = input()
            f.set_result(line)
        except EOFError:
            f.set_result(None)
    _executor.submit(_do_read)
    return f
```

The sleep happens on a worker thread via the existing `_executor` (`ThreadPoolExecutor`). The `Future` resolves when done. The main thread's generator-based coroutine system picks up the resolution via `_step_async_coro`. The `await_safe_to_exit()` call in the run command keeps the process alive until all async tasks complete — without it, Python exits before the game loop runs.

## How It Works

1. The game logic lives in [`temper_snake`](https://github.com/notactuallytreyanastasio/temper_snake) as `.temper.md` files
2. A custom Temper compiler (branch [`do-crimes-to-play-snake`](https://github.com/temperlang/temper/tree/do-crimes-to-play-snake)) adds the `sleep()` and `readLine()` I/O primitives
3. GitHub Actions builds the compiler, compiles the game for all 6 backends, runs tests
4. If tests pass, the compiled output is automatically pushed to this repo

Every push to the source repo triggers a fresh build. This code is always in sync.

## Source

[notactuallytreyanastasio/temper_snake](https://github.com/notactuallytreyanastasio/temper_snake)
