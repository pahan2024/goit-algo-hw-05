import sys
import os


def parse_log_line(line: str) -> dict:
    # Розбирає рядок логу. Очікуваний формат: 'YYYY-MM-DD HH:MM:SS LEVEL Message'.
    # Використовує split(maxsplit=3) для коректного виділення повідомлення.
    
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3].strip(),
    }


def load_logs(file_path: str) -> list:
        # Завантажує логи, використовуючи обробку винятків для перевірки файлу.
    
        logs = []
    if not os.path.exists(file_path):
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    parsed = parse_log_line(line)
                    if parsed:
                        logs.append(parsed)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    
    # Фільтрує логи. 
    
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    # Підраховує кількість записів для кожного рівня логування.
    
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    
    # Виводить статистику у вигляді форматованої таблиці.
    
    print(f"{'Рівень логування':<17} | {'Кількість'}")
    print("-" * 18 + "|" + "-" * 10)
    # Сортування для стабільного відображення (INFO, DEBUG, ERROR тощо)
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py [шлях_до_файлу] [рівень (опціонально)]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    # Виведення загальної статистики
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Обробка опціонального аргументу для деталізації
    if len(sys.argv) > 2:
        target_level = sys.argv[2].upper()
        filtered = filter_logs_by_level(logs, target_level)

        if filtered:
            print(f"\nДеталі логів для рівня '{target_level}':")
            for log in filtered:
                # Виведення згідно з вашим прикладом: дата час - повідомлення
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписи рівня '{target_level}' відсутні.")


if __name__ == "__main__":
    main()
