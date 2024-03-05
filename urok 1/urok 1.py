import logging


def calc(a: int, m: int):
    return a * m
calc('hello', 4)


# Типизация:
# 1-явная int number=1
# 2-неявная number=1
# 3-динамическая number:int=1

# def list(a:int, b:int) -> list:
#     return [len(a), len(b)]
# list(123, 2)

# try:
#     a = 1 / 0
# except ZeroDivisionError:
#     print('asd')
#
# spammer = (10, 12, 234)
# try:
#     spammer.append(678)
# except AttributeError:
#     print('Нельзя менять кортеж')


logging.basicConfig(format="%(name)s || %(asctime)s - %(message)s - %(levelname)s - %(filename)s - %(process)d")
logging.critical('Hello world')

format = "%(name)s"
format = "%(levelname)s"
format = "%(process)d"
format = "%(message)s"
format = "%(asctime)s"

