obj = -123
# obj = 'hello'

match obj:
    case int():
        print(abs(obj))
    case str():
        print(obj[0])
    case _:
        print('意図しない型です。')
