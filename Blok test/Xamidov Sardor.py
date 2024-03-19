import logging
#  1. Что такое типизация? Какие виды типизации бывают?
"Типизация бывает 3 видов = 1) явная(строгая); 2) неявная(не строгая); 3) динамическая. Нужна для выделение значения текста"


#  2. Какой вид типизации в пайтон?
"динамическая"


#  3. Приведите пример к типизации переменной и функции
int number = 1
number = 1
number: int = 1

#  4. Для чего нужен модуль Pydantic
"Pydantic - для валидации входящий сообщений"


#  5. Пример использования Pydantic
from pydantic import BaseModel
from typing import List, Dict, Optional, Union
class Student(BaseModel):
    name: str
    age: int
    surname: str
    friends: List[str] = 0

#  6. Как производится логирование в Python
#  Как производится такого рода логирование (показать кодом)
logging.basicConfig(format='%(levelname), %(actime)s, %(message)s', level=logging.WARNING)
[WARNING] || 2022-12-23 21:07:41,022 || some message
logging.basicConfig(format='%(levelname), %(actime)s, %(message)s', level=logging.INFO)
[INFO] || 2022-12-23 21:11:26,131 || some message


#  7. Как работает синхронный и асинхронный код? В чем разница и что их объединяет
"Синхронный код - читается сверху вниз, слева на право. Последновательный код"
"Асинхронный код - работает паралелльно в одном потоке"


#  8. Приведите пример реализации асинхронного кода
from threading import Thread
import asyncio
async def task1():
    print('Hello world')
async def main():
    t1 = asyncio.create_task(task1())
    await t1
asyncio.run(main())

#  9. Что такое корутина?
"AWAIT = корутина, служит для того, чтобы связаться для работы в асинхронном коде"


#  10. Что такое потоки и как они работают?
"Это последовательность кода, выполняющиеся независимо друг от друга."
"Позволяет выполнять несколько задачь одновременно в асинхронном коде"


#  11. Пример многопоточного кода
async def task3():
    print('running task 1')
async def task5():
    print('running task 2')
async def main():
    task_group = await asyncio.gather(task3(), task5())
    print(task_group)

asyncio.run(main())

#  12. Привести пример на абстрактный класс?
from abc import ABC, abstractmethod
class DataBase(ABC):
    @abstractmethod
    def add_user(self, user_id):
        pass
    @abstractmethod
    def delete_user(self, user_id):
        pass
class SQL(DataBase):
    def add_table(self):
        print('sql.execute')

#  13. Что такое парсинг в программировании
"Парсинг в программировании — это процесс анализа данных для извлечения информации."
"Он часто используется в обработки текстовых данных или данных, представленных в определенном формате"

#  14. Как создается подключение к сайту через aiohttp(пример кода)
import aiohttp
import asyncio
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'http://books.toscrape.com/'
        async with session.get(url) as response:
            html = await response.text()
            print(html)

#  15. Для чего нужны генераторы?
"Генераторы в Python. Next = выводит перечень значение по очереди"
"Yield = не останавливая процесс работает, нежели как return"


#  16. Привести пример на генератор
def check(tolpa):
    for client in tolpa:
        yield client
all_clients = ['client', 'client1', 'client2', 'client3', 'client4']
cafe = check(all_clients)
print(next(cafe))

#  17. Виды тестирования
"Assert. Unit test. Doctest"


#  18. Что такое TDD? Какие категории имеет
"TDD (Test-Driven Development) в Python — для проверки написнного кода и для записи самого кода,"
"Процесс TDD состоит из трех основных шагов: написание тестов, написание кода и рефакторинг"


#  19. Какую функцию выполняет assert?
"Assert в используется для проверки условий. Предположений или ожиданий в коде во время разработки программы"


#  20. Пример реализации assert
x = 5
assert x == 5 , 'Значение не равно 5'

#  21. Как работает doctest?
"Работает с документами и типами docstring. Нужно для проверки во время написании кода"


#  22. Пример doctest
def check(x, y) -> int or float:
    """
    >>> check(5, 2)
    10
    >>> check(5, {'key': 'value'})
    None или неверно
    """
    return x * y

#  23. Особенность синтаксиса(на что выдает ошибку) доктест?
"Ошибку выдает на не правильную функцию или же, если прописанная логика была не верна при проверки кода"


#  24. В чем суть unit тестов?
"Целью unit-тестирования является изолирование и тестирование самостоятельных частей кода (обычно функций, методов или классов) с целью обеспечения их правильной работы"


#  25. Пример реализации unit тестов
import unittest
def checker(x, y) -> int or float:
    return x * y
class Calculator:
    def plus(self, x, y):
        return x + y
    def minus(self, x, y):
        return x - y
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.plus(1, 2), 3)
        self.assertEqual(self.calculator.plus(-1, 1), 0)
    def test_minus(self):
        self.assertEqual(self.calculator.minus(5, 2), 3)
        self.assertEqual(self.calculator.minus(-1, -1), 0)
if __name__ == '__main__':
    unittest.main()