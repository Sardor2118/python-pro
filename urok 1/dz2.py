import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def add(a: int, b: int) -> dict:
    try:
        result = a + b
        return {'result': result}
    except Exception as e:
        logging.error(f"Error in addition function: {e}")
        return {'error': f"Error in addition function: {e}"}

def minus(a: int, b: int) -> dict:
    try:
        result = a - b
        return {'result': result}
    except Exception as e:
        logging.error(f"Error in subtraction function: {e}")
        return {'error': f"Error in subtraction function: {e}"}

def multiplication(a: int, b: int) -> dict:
    try:
        result = a * b
        return {'result': result}
    except Exception as e:
        logging.error(f"Error in multiplication function: {e}")
        return {'error': f"Error in multiplication function: {e}"}

a = 5
b = 0

add_result = add(a, b)
sub_result = minus(a, b)
mul_result = multiplication(a, b)

print(add_result)
print(sub_result)
print(mul_result)
