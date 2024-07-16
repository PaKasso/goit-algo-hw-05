import sys
import re
from typing import Callable, List, Dict

def parse_log_line(line: str) -> dict:
    """
    Парсить рядок лог-файлу і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення.
    """
    parts = line.split(' ', 3)  # Розділяємо рядок на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:  # Перевіряємо, чи є всі необхідні частини
        return None  # Якщо частин менше 4, повертаємо None
    date, time, level, message = parts  # Розпаковуємо частини
    return {'date': date, 'time': time, 'level': level, 'message': message.strip()}  # Повертаємо словник

def load_logs(file_path: str) -> List[dict]:
    """
    Зчитує лог-файл і використовує parse_log_line для кожного рядка, зберігаючи результати в список.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Відкриваємо файл для читання
            for line in file:
                log_entry = parse_log_line(line)  # Парсимо кожен рядок
                if log_entry:  # Якщо рядок був успішно розпарсений
                    logs.append(log_entry)  # Додаємо розпарсений рядок до списку
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")  # Повідомляємо про відсутність файлу
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")  # Повідомляємо про інші помилки при читанні файлу
    return logs  # Повертаємо список логів

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Фільтрує логи за вказаним рівнем логування.
    """
    return [log for log in logs if log['level'].upper() == level.upper()]  # Повертаємо логи, що відповідають рівню

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = {}
    for log in logs:
        level = log['level'].upper()  # Отримуємо рівень логування у верхньому регістрі
        counts[level] = counts.get(level, 0) + 1  # Збільшуємо кількість для відповідного рівня
    return counts  # Повертаємо словник з підрахунком для кожного рівня

def display_log_counts(counts: Dict[str, int]):
    """
    Форматує та виводить результати підрахунку у вигляді таблиці.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")  # Виводимо рівень логування та кількість у форматованому вигляді

def display_logs(logs: List[dict]):
    """
    Виводить деталі логів для заданого рівня.
    """
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")  # Виводимо дату, час та повідомлення

def main():
    """
    Основна функція, яка обробляє аргументи командного рядка і виконує відповідні функції.
    """
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [log_level]")  # Пояснення використання
        return
    
    file_path = sys.argv[1]  # Отримуємо шлях до файлу з аргументів командного рядка
    log_level = sys.argv[2] if len(sys.argv) > 2 else None  # Отримуємо рівень логування, якщо він вказаний

    logs = load_logs(file_path)  # Завантажуємо логи з файлу
    if not logs:
        return
    
    counts = count_logs_by_level(logs)  # Підраховуємо кількість записів для кожного рівня логування
    display_log_counts(counts)  # Виводимо підрахунок

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)  # Фільтруємо логи за вказаним рівнем
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        display_logs(filtered_logs)  # Виводимо відфільтровані логи

if __name__ == "__main__":
    main()  # Викликаємо основну функцію, якщо скрипт запускається напряму