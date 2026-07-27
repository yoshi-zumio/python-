from typing import Any, TypeIs

class Magazine:
    pass

class Book:
    def __init__(self, title: str) -> None:
        self.title = title

    def short_title(self) -> str:
        return self.title[:10]


# def process(data: Book | Magazine) -> str:
#     if hasattr(data, 'title'):
#         return data.short_title()

def is_book(data: Any) -> TypeIs[Book]:
    return hasattr(data, 'title')

def process(data: Book | Magazine) -> str | None:
    if is_book(data):
        return data.short_title()

if __name__ == '__main__':
    print(process(Book('これからはじめるReact実践入門')))
