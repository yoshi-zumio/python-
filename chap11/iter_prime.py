import math
from collections.abc import Iterator

class Prime:
    def __init__(self, max: int) -> None:
        self.max = max
        self.__current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        while True:
            self.__current += 1
            if self.__current > self.max:
                raise StopIteration
            elif self.__is_prime(self.__current):
                return self.__current

    def __is_prime(self, value: int) -> bool:
        result = True
        for i in range(2, math.floor(math.sqrt(value)) + 1):
            if value % i == 0:
                result = False
                break
        return result

if __name__ == '__main__':
    pr = Prime(100)
    for p in pr:
        print(p)
