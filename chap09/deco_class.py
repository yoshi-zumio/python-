from collections.abc import Callable
from typing import Any

class log_func:
    # 初期化メソッド（パラメーターを保持）
    def __init__(self, details: bool = True) -> None:
        self.details = details

    # デコレーターの実処理
    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args, **kwargs):
            print('-----------------')
            print(f'Name: {func.__name__}')
            if self.details:
                print(f'Args: {args}')
                print(f'Keywds: {kwargs}')
            print('-----------------')
            return func(*args, **kwargs)
        return inner

@log_func()
def hoge(x: int, y: int, m: str = 'bar', n: str = 'piyo') -> None:
    print(f'hoge: {x}-{y}/{m}-{n}')

hoge(15, 37, m='ほげ', n='ぴよ')
