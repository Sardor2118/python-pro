def plus(a: int, b: int) -> dict:
    result = a + b
    return {'result': result}

def minus(a: int, b: int) -> dict:
    result = a - b
    return {'result': result}

def multiplication(a: int, b: int) -> dict:
    result = a * b
    return {'result': result}

# Пример использования функций
a = 5
b = 3

add_result = plus(a, b)
sub_result = minus(a, b)
mul_result = multiplication(a, b)

print(add_result)
print(sub_result)
print(mul_result)
