def calculation(a, b):
    """
    Принимает два целых числа и возвращает их сумму и разность.
    """
    addition = a + b
    subtraction = a - b
    return addition, subtraction

def calculator(a, b):
    """
    Вызывает функцию calculation() и выводит её результаты.
    """
    res = calculation(a, b)
    print(res)

# Пример использования
calculator(40, 10)  # Вывод: (50, 30)
