from bloom_filter import BloomFilterUniversal  # Імпортуємо реалізацію фільтра Блума


def process_file(filename, bloom_filter):
    """Обробляє вхідний файл з операціями додавання, перевірки та видалення"""
    operations = {
        "add": 0,
        "check": 0,
        "found": 0,  # Кількість успішних перевірок
        "removed": 0,  # Кількість успішних видалень
        "checked_items": [],
    }

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                break
            operation, item = line[0], line[2:].strip()
            if operation == '+':
                bloom_filter.add(item)
                operations["add"] += 1
            elif operation == '?':
                operations["check"] += 1
                operations["checked_items"].append(item)
                result = "Y" if bloom_filter.check(item) else "N"
                if result == "Y":
                    operations["found"] += 1  # Підраховуємо успішні перевірки
                print(result)
            elif operation == '-':
                removed = bloom_filter.remove(item)
                if removed:
                    operations["removed"] += 1
                    # print(f"Елемент '{item}' успішно видалений.")

    return operations


def print_statistics(operations):
    """Виводить статистику після обробки файлу"""
    print("\n=== Статистика ===")
    print(f"Додано елементів: {operations['add']}")
    print(f"Перевірено елементів: {operations['check']}")
    print(f"Знайдено елементів: {operations['found']}")
    print(f"Видалено елементів: {operations['removed']}")
    if operations['check'] > 0:
        found_percentage = (operations['found'] / operations['check']) * 100
        print(f"Відсоток знайдених елементів: {found_percentage:.2f}%")
    else:
        print("Перевірки не виконувались.")


def main():
    n = 10 ** 6  # максимальна кількість елементів
    p = 0.01  # ймовірність хибнопозитивних спрацювань
    # bloom_filter = BloomFilterMurMur3(n, p)
    # bloom_filter = BloomFilter(n, p)
    bloom_filter = BloomFilterUniversal(n, p)



    # Обробка файлу з операціями
    operations = process_file('input.txt', bloom_filter)

    # Виведення статистики
    print_statistics(operations)
    print("l = " + format(bloom_filter.l))
    print("m = " + format(bloom_filter.m))


if __name__ == "__main__":
    main()
