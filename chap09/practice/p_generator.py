from collections.abc import Generator
import random

def random_int(max: int) -> Generator[int]:
    while True:
        yield random.randint(0, max)

for num in random_int(100):
    print(num)
    if num > 80:
        break
