from typing import LiteralString

def build_sql(keyword: LiteralString) -> str:
    return f'SELECT * FROM items WHERE keyword = "{keyword}"'

print(build_sql('Python'))

key = input()
print(build_sql(key))
