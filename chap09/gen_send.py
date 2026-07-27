from collections.abc import Generator

def gen_com() -> Generator[str, str]:
    while True:
        n = yield input('名前を教えてください：')
        yield f'こんにちは、{n}さん！'

gen = gen_com()
for name in gen:
    res = gen.send(name.upper())
    print(res)
