def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
try:
    n = int(input("Введите число членов последовательности:"))
except ValueError:
    print("Неверный формат данных")
else:
    print("Последовательность Фибоначчи:")
    for i in range(n):
        print(fibonacci(i))