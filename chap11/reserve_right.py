from __future__ import annotations

class Left:
    def __init__(self, value: int) -> None:
        self.value = value

    def __sub__(self, other: Left) -> Left:
        print('Left#__sub__')
        return Left(self.value - other.value)

# class Right(Left):
class Right:
    def __init__(self, value: int) -> None:
        self.value = value

    def __rsub__(self, other: Left) -> Left:
        print('Right#__rsub__')
        return Left(other.value - self.value)

if __name__ == '__main__':
    lf = Left(10)
    rt = Right(5)
    result = lf - rt
    print(result.value)
