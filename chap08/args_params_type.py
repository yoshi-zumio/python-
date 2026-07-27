from typing import TypedDict, Unpack, NotRequired

class KeywordArgs(TypedDict):
    title: str
    size: int
    full: NotRequired[bool]

def hoge(**kwargs: Unpack[KeywordArgs]) -> None:
    print(kwargs)

hoge(title='Hello', size=100, full=True)
hoge(title='Hello', size=100)
hoge(title='Hello', full=True)
hoge(title='Hello', size='100px')
hoge(title='Hello', size=100, none='none')
