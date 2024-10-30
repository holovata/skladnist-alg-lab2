import math
import random

class BloomFilterUniversal:
    def __init__(self, n, p):
        self.n = n  # Максимальна кількість елементів
        self.p = p  # Ймовірність хибнопозитивних спрацювань
        self.m = self.calculate_size()  # Розмір масиву лічильників
        self.l = self.calculate_hash_count()  # Кількість хеш-функцій
        self.counter_array = [0] * self.m  # Масив лічильників
        self.big_prime = 1000000007  # Велике просте число

        # Ініціалізація випадкових коефіцієнтів a та b для кожної хеш-функції
        self.a = [random.randint(1, self.big_prime - 1) for _ in range(self.l)]
        self.b = [random.randint(0, self.big_prime - 1) for _ in range(self.l)]

    def calculate_size(self):
        """Розраховує розмір масиву лічильників"""
        m = -(self.n * math.log(self.p)) / (math.log(2) ** 2)
        return int(m)

    def calculate_hash_count(self):
        """Розраховує кількість хеш-функцій для оптимальної роботи фільтра"""
        l = (self.m / self.n) * math.log(2)
        return int(l)

    def hash_item(self, item, i):
        """Обчислює універсальне хеш-значення для item з використанням i-ї хеш-функції"""
        x = self.string_to_int(item)  # Перетворюємо рядок у числове значення
        return ((self.a[i] * x + self.b[i]) % self.big_prime) % self.m

    def string_to_int(self, s):
        """Перетворює рядок у числове значення"""
        # Проста функція, яка конвертує рядок у ціле число
        result = 0
        for char in s:
            result = result * 31 + ord(char)  # Використовуємо базу 31 для уникнення колізій
        return result

    def get_hash_values(self, item):
        """Генерує кілька хеш-значень для рядка"""
        return [self.hash_item(item, i) for i in range(self.l)]

    def add(self, item):
        """Додає елемент до фільтра Блума"""
        hash_values = self.get_hash_values(item)
        for index in hash_values:
            self.counter_array[index] += 1  # Збільшуємо лічильник

    def remove(self, item):
        """Видаляє елемент з фільтра Блума, якщо він існує"""
        if not self.check(item):
            return False  # Елемент не знайдено

        hash_values = self.get_hash_values(item)
        for index in hash_values:
            self.counter_array[index] -= 1  # Зменшуємо лічильник
        return True

    def check(self, item):
        """Перевіряє наявність елемента у фільтрі"""
        hash_values = self.get_hash_values(item)
        return all(self.counter_array[index] > 0 for index in hash_values)
