from collections.abc import Callable
from typing import Any
from time import sleep
from datetime import datetime

def time_deco(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args, **kwargs):
        print(f'{func.__name__} Start: {datetime.now()}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} End: {datetime.now()}')
        return result
    return inner

@time_deco
def hoge() -> None:
    sleep(3)
    print('hoge is running.')

hoge()
