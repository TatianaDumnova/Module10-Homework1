# Домашнее задание по теме "Создание потоков".

# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#
# Примечание:
# Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации,
# пока процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep() из модуля time,
# предварительно импортировав его.

import threading
import time

my_lock = threading.Lock()
def print_numbers():
    for i in range(1, 11):
        with my_lock:
            print(i)
            time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        with my_lock:
            print(letter)
            time.sleep(1)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
