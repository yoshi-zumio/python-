from collections.abc import Generator

def my_gen() -> Generator[str]:
    yield 'あいうえお'
    yield 'かきくけこ'
    yield 'さしすせそ'

# gen = my_gen()
# for value in gen:
for value in my_gen():
    print(value)

# print(my_gen())
