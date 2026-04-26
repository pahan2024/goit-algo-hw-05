import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст, знаходить усі дійсні числа, відокремлені пробілами,
    і повертає їх як об'єкт генератора.
    """
    # Регулярний вираз для пошуку дійсних чисел:
    # \d+ - одна або більше цифр
    # \. - крапка
    # \d+ - одна або більше цифр після крапки
    # Навколо числа мають бути пробіли (за умовою завдання)
    pattern = r"\d+\.\d+"
    
    # Використовуємо finditer для ефективного пошуку всіх збігів
    for match in re.finditer(pattern, text):
        # Перевіряємо, чи число оточене пробілами (або є на початку/в кінці рядка)
        # Це додаткова перевірка згідно з рекомендаціями
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел у тексті, використовуючи функцію-генератор.
    """
    total_income = 0.0
    
    # Викликаємо генератор і проходимо по кожному отриманому числу
    for number in func(text):
        total_income += number
        
    return total_income

# --- Приклад використання (з твого завдання) ---

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
