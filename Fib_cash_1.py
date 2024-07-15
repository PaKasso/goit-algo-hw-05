def caching_fibonacci():
    # Створюємо порожній словник cache для зберігання обчислених значень чисел Фібоначчі
    cache = {}
    
    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0, як базовий випадок
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1, як базовий випадок
        if n == 1:
            return 1
        # Якщо n вже є у кеші, повертаємо значення з кешу
        if n in cache:
            return cache[n]
        
        # Рекурсивно обчислюємо n-те число Фібоначчі, використовуючи кешування
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Повертаємо обчислене значення
        return cache[n]
    
    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Приклад використання:
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610