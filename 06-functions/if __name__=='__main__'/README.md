# if **name** == "**main**" — Understanding Script Execution

## What this demonstrates

This folder contains two scripts, `script1.py` and `script2.py`, to show how
Python decides whether a file is being run directly or being imported by
another file.

## The core idea

Every Python file has a hidden built-in variable called `__name__`.

- If you run a file **directly** (e.g. `python script1.py`), Python
  automatically sets that file's `__name__` to `"__main__"`.
- If a file is **imported** into another file instead, its `__name__` is
  set to its actual filename (e.g. `"script1"`), not `"__main__"`.

The line:

```python
if __name__ == "__main__":
    main()
```

is really just asking: **"Was this file run directly, or was it just imported
by something else?"** The code inside only runs in the first case.

## What's happening in script1.py

- Defines `favorite_food()` and a `main()` function.
- `main()` calls `favorite_food("Pizza")` and prints a few lines.
- Because `script1.py` is run directly, `__name__` equals `"__main__"`, so
  `main()` executes and we see its output.

## What's happening in script2.py

- Starts with `from script1 import *`, importing everything from `script1.py`.
- At this point, Python runs `script1.py` top to bottom to load its
  functions — **but** since `script1.py` is only being _imported_ here (not
  run directly), its own `__name__` is `"script1"`, not `"__main__"`. So
  `script1`'s own `if __name__ == "__main__":` block does **not** trigger,
  and `script1`'s `main()` never runs on its own.
- `script2.py` defines its own `favorite_drink()` and its own `main()`,
  which calls both `favorite_food("Burger")` (imported from script1) and
  `favorite_drink("Tea")`.
- Since `script2.py` is the file being run directly this time, **its**
  `__name__` is `"__main__"`, so **its** `main()` runs.

## The takeaway

`if __name__ == "__main__":` lets a file be safely reused as an importable
module elsewhere, without its own standalone logic (like `script1`'s
`main()`) accidentally running every time it's imported. Only the file that
was actually executed directly gets its `main()` triggered.

## Why this matters for JARVIS

As JARVIS grows past one file, this pattern becomes essential. For example,
`commands.py` might define several command functions, and `main.py` will
import them. Without this guard, every test/debug code sitting in
`commands.py` would run automatically the moment `main.py` imports it —
which isn't what we want.
