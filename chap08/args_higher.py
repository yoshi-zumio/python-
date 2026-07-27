from collections.abc import Callable
from typing import Any

def walk_list(data: list[Any], func: Callable[[Any, int], None]) -> None:
    for key, value in enumerate(data):
        func(value, key)

def show_item(value: Any, key: int) -> None:
    print(key, ':', value)

data = [105, 53, 27, 87, 33]
walk_list(data, show_item)
