from typing import Any, Self

class MyStack:
    def __init__(self) -> None:
        self.__data = []

    def push(self, elem: Any) -> Self:
        self.__data.append(elem)
        return self

    def pop(self) -> Any:
        return self.__data.pop()

if __name__ == '__main__':
    s = MyStack()
    s.push(40)
    print(s.pop())
