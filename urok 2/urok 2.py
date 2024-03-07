from threading import Thread
...
...
# t1 = Thread(target=Функция, args=(если есть параметры))
# t1.start() #откроет поток
# t1.run() #в том же поток

# def show_products(products):
#     for i in products:
#         print(f"{i} \nЦена: 20$")
# all_pr=['Apple', 'Bread', 'Burger']
# t1=Thread(target=show_products, args=(all_pr,))
# t1.start()
# # t1.run()
# print('Hello')

def send_message(users):
    for i in users:
        print(f'{i}')
users_list = ['Jordan', 'Pasha', 'Mikle']
t1=Thread(target=send_message, args=(users_list,))
t1.start()
print('Hello')

def check_queue(clients):
    for client in clients:
        yield client
all_clients = ['Pasha', 'Jordan', 'Vika']
hospital = check_queue(all_clients)
print(next(hospital))
print(next(hospital))
print(next(hospital))

def week_days(days):
    for day in days:
        yield day
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month = week_days(weeks)
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))
print(next(month))


