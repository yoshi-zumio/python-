from typing import Required, TypedDict

class PersonDict(TypedDict, total=False):
    name: Required[str]
    age: int
    married: bool

p1: PersonDict = {'name': 'Yamada', 'age': 25}
# p2: PersonDict = {'name': 'Yamada', 'age': 25, 'married': True, 'gender': 'male'}
