import time
import threading
import asyncio

# Синхронный подход
def sync_traffic_light():
    print("Синхронный светофор:")
    while True:
        print("Зеленый")
        time.sleep(5)
        print("Желтый")
        time.sleep(2)
        print("Красный")
        time.sleep(4)

# Асинхронный подход
async def async_traffic_light():
    print("Асинхронный светофор:")
    while True:
        print("Зеленый")
        await asyncio.sleep(5)
        print("Желтый")
        await asyncio.sleep(2)
        print("Красный")
        await asyncio.sleep(4)

# Многопоточный подход
def thread_traffic_light():
    def run_traffic_light():
        print("Многопоточный светофор:")
        while True:
            print("Зеленый")
            time.sleep(5)
            print("Желтый")
            time.sleep(2)
            print("Красный")
            time.sleep(4)

    thread = threading.Thread(target=run_traffic_light)
    thread.start()

if __name__ == "__main__":
    # Запуск синхронного светофора
    sync_traffic_light()

    # Запуск асинхронного светофора
    asyncio.run(async_traffic_light())

    # Запуск многопоточного светофора
    thread_traffic_light()
