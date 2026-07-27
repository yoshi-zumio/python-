from collections.abc import Callable
from typing import Any

# 関数の結果を大文字に変換
def upper_deco(func: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args, **kwargs):
        # 元の関数を実行
        result = func(*args, **kwargs)
        # str型の場合にだけ大文字化
        if isinstance(result, str):
            return result.upper()
        else:
            return result
    return inner

class MyClass:
    # メソッドにデコレーターを適用
    # クラス/staticメソッドに適用する場合は@classmethod／@staticmethodデコレーターを先に
    @upper_deco
    def greet(self, name: str) -> str:
        return f'Hello, {name}!!'

if __name__ == '__main__':
    c = MyClass()
    print(c.greet('tom'))
