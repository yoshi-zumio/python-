def total_products(init: int, *values: int) -> int:
    result = init
    for value in values:
        result *= value
    return result

print(total_products())
