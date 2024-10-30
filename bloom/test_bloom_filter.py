import random
import string
import time
from bloom_filter import BloomFilterUniversal


def generate_random_string(min_length=1, max_length=15):
    """ Генерує випадковий рядок із малих латинських літер довжиною від min_length до max_length """
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def test_false_positive_rate():
    N = 1_000_000  # Половина ключів буде додана до фільтра
    p = 0.01  # Теоретична ймовірність хибнопозитивних спрацювань
    # bloom_filter = BloomFilterMurMur3(N, p)
    # bloom_filter = BloomFilter(N, p)
    bloom_filter = BloomFilterUniversal(N, p)



    print(f"Тестування фільтра Блума з {N} елементами.")
    start_time = time.time()

    # Генерація 2 мільйонів унікальних випадкових рядків
    print("Генерація унікальних ключів...")
    keys = set()
    while len(keys) < 2 * N:
        keys.add(generate_random_string())
    print(f"Згенеровано {len(keys)} унікальних ключів.")

    keys = list(keys)
    inserted_keys = keys[:N]
    test_keys = keys[N:]

    # Додаємо першу половину рядків до фільтра Блума
    print("Додавання першої половини ключів до фільтра Блума...")
    for i, key in enumerate(inserted_keys, 1):
        bloom_filter.add(key)
        if i % 50000 == 0:
            print(f"Додано {i} ключів у фільтр Блума.")
    print("Додавання завершено.")

    # Перевіряємо другу половину рядків і підраховуємо хибнопозитивні спрацювання
    print("Початок перевірки на хибнопозитивні спрацювання...")
    false_positives = 0
    for i, key in enumerate(test_keys, 1):
        if bloom_filter.check(key):
            false_positives += 1
        if i % 50000 == 0:
            print(f"Перевірено {i} ключів, хибнопозитивні: {false_positives}")
    print("Перевірка завершена.")

    # Розраховуємо фактичну ймовірність хибнопозитивних спрацювань
    false_positive_rate = (false_positives / N) * 100
    print(f"Теоретична ймовірність хибнопозитивних спрацювань: {p * 100}%")
    print(f"Кількість хибнопозитивних спрацювань: {false_positives}")
    print(f"Фактична ймовірність хибнопозитивних спрацювань: {false_positive_rate:.2f}%")

    # Підсумковий час виконання тесту
    end_time = time.time()
    print(f"Тест завершено за {end_time - start_time:.2f} секунд.")


if __name__ == "__main__":
    test_false_positive_rate()
