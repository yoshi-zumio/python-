from collections.abc import Callable
from typing import Any

def log_func(details: bool = True) -> Callable[[Callable[..., Any]],
                                               Callable[..., Any]]:
    def outer(func: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args, **kwargs):
            print('-----------------')
            print(f'Name: {func.__name__}')
            if details:
                print(f'Args: {args}')
                print(f'Keywds: {kwargs}')
            print('-----------------')
            return func(*args, **kwargs)
        return inner
    return outer

@log_func(details=False)
def hoge(x: int, y: int, m: str = 'bar', n: str = 'piyo') -> None:
    print(f'hoge: {x}-{y}/{m}-{n}')

hoge(15, 37, m='ほげ', n='ぴよ')
