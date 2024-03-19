## оператор assert
import doctest
# минусы = не переходит на следующий этап если получил fail в прошлом
# плюс = легкий синтаксис

# def check_positive_number(x, y) -> int or float:
# #     assert x > 0 and y > 0, 'Число отрицательное'
#     if x > 0 and y > 0:
#         return x, y
#     else:
#         raise AssertionError('Число отрицательное')
#     # return x, y
#
# check_positive_number(23, 45)
# check_positive_number(-15, -85)
# check_positive_number(13, 4)

def check(x, y) -> int or float:
    """Что делает тест
    >>> check(5, 2)
    10
    >>> check(5, {'key': 'value'})
    None
    """
    return x * y
doctest.testfile('urok5.py')
#
# a = "123k"
# if a.isdigit():
#     print(a)
# else:
#     print('Не цифра')
#
# a = "фывф2ы"
# if a.isalpha():
#     print(a)
# else:
#     print("Не буквы")

# import unittest
# def check(x, y) -> int or float:
#     return x * y
#
# class TestOne(unittest.TestCase):
#     def test_check(self):
#         self.assertEqual(check(5, 2), 10, 'э')
#     def test_checker2(self):
#         self.assertNotEqual(check(5, 2), 10, 'э')