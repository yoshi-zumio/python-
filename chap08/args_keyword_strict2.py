def my_func(arg1: int, /, arg2: int = 0, arg3: int = 0) -> None:
    pass

# my_func(arg1=10, arg2=20)
my_func(10, arg2=20)
