# ユーザー定義関数

## 型アノテーション
- 関数で使う変数の型を指定する方法

例
def sum(a: int, b: int) -> int:
    return a+b

のように引数と返り値に指定できる．

## ジェネリック型
- 中に入る型を，後から指定できる型
    - 例えば，list

```
numbers: list[int] = [1, 2, 3]
names: list[str] = ["田中", "佐藤"]
```
みたいな．

## 型エイリアス
- 自分で型の名前を指定できる仕組み
- type　で指定

```
type UserData = dict[str, str | int]

user: UserData = {
    "name": "吉住",
    "age": 24,
}
```

## キーワード引数
- 関数を呼び出す際に，どの引数に値を代入するかを明示的に指定する方法
- 定義する際に [変数名]=値　とするのと同じ
例

```
def greet(name, message):
    print(f"{name}さん、{message}")
greet(name="吉住", message="こんにちは")　#どの変数に何の値を代入するかを明示
```

## 可変長引数
- 引数の個数を固定しない仕組み

### パターン1 普通の引数を受け取るパターン　`*args`：
```
def add(*args):
    print(args)

add(1, 2, 3)
#実行結果：(1, 2, 3)
```

### パターン2 複数のキーワード引数を受け取るパターン `*kwargs`：

```
def show_user(**kwargs):
    print(kwargs)

show_user(name="吉住", age=24, city="福岡")

実行結果
{
    "name": "吉住",
    "age": 24,
    "city": "福岡"
}
```