from typing import Any

class MyInfo:
    def __init__(self) -> None:
        super().__setattr__('__data', {})

    def __getattr__(self, name: str) -> Any:
        try:
            return super().__getattribute__('__data')[name]
        except KeyError:
            return None

    def __setattr__(self, name: str, value: Any) -> None:
        super().__getattribute__('__data')[name] = value

if __name__ == '__main__':
    i = MyInfo()
    i.score = 58
    i.hobby = '卓球'
    print(i.hobby)
    print(i.__dict__)
