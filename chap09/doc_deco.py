from collections.abc import Callable
from typing import Any
from functools import wraps

def log_func(func: Callable[..., Any]) -> Callable[..., Any]:
    """関数の情報を出力するデコレーター"""
    @wraps(func)
    def inner(*args, **kwargs):
        """関数の情報を出力"""
        print('-----------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'Keywds: {kwargs}')
        print('-----------------')
        return func(*args, **kwargs)
    return inner

@log_func
def hoge(x: int, y: int, m: str = 'bar', n: str = 'piyo') -> None:
    """デコレーター確認のための関数"""
    print(f'hoge: {x}-{y}/{m}-{n}')

if __name__ == '__main__':
    print(hoge.__name__)
    print(hoge.__doc__)
