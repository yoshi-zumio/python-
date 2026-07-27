from types import TracebackType
from typing import Self

class MyContext:
    def __enter__(self) -> Self:
        print('**Enter**')
        return self

    def __exit__(self, t: type, value: Exception, tb: TracebackType) -> bool:
        if t is None:
            print('**Exit**')
        else:
            print(f'**{value}**')
            return True

    def hoge(self) -> None:
        print('Hoge')

with MyContext() as c:
    print('With Start')
    c.hoge()
    # raise ValueError('値が不正です。')
