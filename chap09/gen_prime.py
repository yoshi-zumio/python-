from collections.abc import Generator
import math

def get_primes() -> Generator[int]:
    num = 2
    while True:
        try:
            if is_prime(num):
                yield num
            num += 1
        except ValueError as e:
            print(e.args[0])
            yield 0
            break

def is_prime(value: int) -> bool:
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result

for prime in get_primes():
    print(prime)
    if prime > 100:
        break


# 正常終了
# gen = get_primes()
# for prime in gen:
#     print(prime)
#     if prime > 100:
#         gen.close()

# 例外を投げる場合
# gen = get_primes()
# for prime in gen:
#     print(prime)
#     if prime > 100:
#         print(gen.throw(ValueError('result is over 100!')))
