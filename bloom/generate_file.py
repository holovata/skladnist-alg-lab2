import random
import string


def generate_random_string(length=15):
    # Генерує випадковий рядок з малих латинських літер довжиною до 15 символів
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, length)))


def generate_input_file(filename, num_lines):
    operations = ['+', '?', '-']  # Операції: додавання, перевірка, видалення
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            operation = random.choice(operations)  # Випадкова операція
            random_string = generate_random_string()  # Випадковий рядок
            file.write(f"{operation} {random_string}\n")
        file.write('#')  # Додаємо символ завершення операцій


if __name__ == "__main__":
    num_lines = int(input("Введіть бажану кількість рядків для генерації: "))
    generate_input_file('input.txt', num_lines)
    print(f"Згенеровано файл 'input.txt' з {num_lines} рядками.")
