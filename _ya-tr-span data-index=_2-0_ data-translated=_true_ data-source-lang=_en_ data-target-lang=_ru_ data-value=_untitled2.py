import math
import time

def print_info(func):
 
 def wrapper(a, b):
 start_time = time.time()
 result = func(a, b)
 end_time = time.time()
 execution_time = end_time - start_time

 print("Функция:", func.__name__)
 print("Длина катета a:", a)
 print("Длина катета b:", b)
 print("Результат (гипотенуза):", result)
 print("Время выполнения:", execution_time, "секунды\n")

 return result
 return wrapper

@print_info

def calculate_hypotenuse(a, b):
 return math.sqrt(a**2 + b**2)

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

result = calculate_hypotenuse(a, b)
print("Результат вычисления:", result)
