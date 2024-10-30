import time
import random
import string
from bloom_filter import BloomFilterUniversal


def generate_random_string(length=15):
    """Генерує випадковий рядок із малих латинських літер довжиною до 15 символів."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def evaluate_performance(bloom_filter, num_operations=100000):
    """Оцінює середній час виконання операцій додавання, перевірки та видалення."""
    add_times = []
    check_times = []
    remove_times = []

    # Генеруємо випадкові рядки для тестування
    test_strings = [generate_random_string() for _ in range(num_operations)]

    # Вимірюємо час додавання
    for item in test_strings:
        start_time = time.time()
        bloom_filter.add(item)
        end_time = time.time()
        add_times.append(end_time - start_time)

    # Вимірюємо час перевірки
    for item in test_strings:
        start_time = time.time()
        bloom_filter.check(item)
        end_time = time.time()
        check_times.append(end_time - start_time)

    # Вимірюємо час видалення
    for item in test_strings:
        start_time = time.time()
        bloom_filter.remove(item)
        end_time = time.time()
        remove_times.append(end_time - start_time)

    # Розрахунок середніх значень
    avg_add_time = sum(add_times) / num_operations
    avg_check_time = sum(check_times) / num_operations
    avg_remove_time = sum(remove_times) / num_operations

    print(f"Середній час додавання: {avg_add_time * 1000:.6f} мс")
    print(f"Середній час перевірки: {avg_check_time * 1000:.6f} мс")
    print(f"Середній час видалення: {avg_remove_time * 1000:.6f} мс")


if __name__ == "__main__":
    n = 10 ** 6  # Максимальна кількість елементів
    p = 0.01  # Ймовірність хибнопозитивних спрацювань
    # bloom_filter = BloomFilterMurMur3(n, p)
    # bloom_filter = BloomFilter(n, p)
    bloom_filter = BloomFilterUniversal(n, p)



    # Оцінка продуктивності на великій кількості операцій
    evaluate_performance(bloom_filter)
