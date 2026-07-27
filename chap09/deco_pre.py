from collections.abc import Callable
from typing import Any

def log_func(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args, **kwargs):
        print('-----------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'Keywds: {kwargs}')
        print('-----------------')
        return func(*args, **kwargs)
    return inner

def hoge(x: int, y: int, m: str = 'bar', n: str = 'piyo') -> None:
    print(f'hoge: {x}-{y}/{m}-{n}')

log_hoge = log_func(hoge)
log_hoge(15, 37, m='ほげ', n='ぴよ')
