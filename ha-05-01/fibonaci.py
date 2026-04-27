def caching_fibonacci():

    # Словник cache зберігається завдяки замиканню
    cache = {}

    def fibonacci(n):
        # Базові випадки для ряду Фібоначчі
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевіряємо, чи є значення вже в кеші
        if n in cache:
            return cache[n]

        # Рекурсивно обчислюємо n-те число та зберігаємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci


# Отримуємо екземпляр функції fibonacci з власним кешем
fib = caching_fibonacci()

# Використовуємо для обчислення пріклад
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
