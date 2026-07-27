from typing import Any

class LogProp:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: object, t: type) -> Any:
        print(f'{self.name}: get')
        return obj.__dict__[self.name]

    def __set__(self, obj: object, value: Any) -> None:
        print(f'{self.name}: set {value}')
        obj.__dict__[self.name] = value

class App:
    title = LogProp('title')

if __name__ == '__main__':
    app = App()
    app.title = '独習Python'
    print(app.title)
