import asyncio
# import time
#
# async def task1():
#     await asyncio.sleep(1)
#     print('Hello world')
# async def task2():
#     await asyncio.sleep(1)
#     print('Hello world2')
# async def main():
#     t1 = asyncio.create_task(task1())
#     t2 = asyncio.create_task(task2())
#     await t1
#     await t2
# asyncio.run(main())
#
#
# async def show_products(products):
#     for i in products:
#         print(f"{i} \nЦена: 20$")
# all_pr=['Apple', 'Bread', 'Burger']
# asyncio.run(show_products(all_pr))
# print('Hello world')

# async def send_message(users):
#     for i in users:
#         await asyncio.sleep(0.5)
#         print(i)
# users = ['Jordan', 'Pasha', 'Micke']
# async def main():
#     t1 = asyncio.create_task(send_message(users))
#     await t1
# asyncio.run(main())
# print('Hello world')

async def task1():
    print('running task 1')
async def task2():
    print('running task 2')
async def main():
    task_group = await asyncio.gather(task1(), task2())
    print(task_group)

asyncio.run(main())
