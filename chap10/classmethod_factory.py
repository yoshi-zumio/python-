from typing import Self
import requests

class Book:
    def __init__(self, isbn: str, title: str, price: int) -> None:
        self.isbn = isbn
        self.title = title
        self.price = price

    @classmethod
    def get_by_isbn(cls, isbn: str) -> Self:
        res = requests.get(f'https://wings.msn.to/tmp/{isbn}.json')
        bs = res.json()
        return cls(bs['isbn'], bs['title'], bs['price'])

if __name__ == '__main__':
    b = Book.get_by_isbn('978-4-7981-8055-7')
    print(b.title)
