import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_chars = {'i', 'l', '1', 'L', 'o', '0', 'O'}


def input_number(prompt, min_value=1):
    while True:
        n = input(prompt).strip()
        if n.isdigit():
            num = int(n)
            if num >= min_value:
                return num
            print(f'Число должно быть не меньше {min_value}')
        else:
            print("Пожалуйста, введите число")


def input_yes_no(prompt):
    while True:
        n = input(prompt).lower().strip()
        if n in ('да', 'нет'):
            return n == 'да'
        print('Пожалуйста, ответьте "да" или "нет"')


def generate_passwords():
    chars = []

    print('=== Генератор паролей ===')

    quantity = input_number('Сколько вам нужно паролей? (Введите число): ')
    length = input_number('Какую длину пароля сгенерировать? (Введите число): ')

    print('\nКакие символы включать в пароль?')
    include_digits = input_yes_no('Включать цифры? (да/нет): ')
    include_upper = input_yes_no('Включать прописные буквы? (да/нет): ')
    include_lower = input_yes_no('Включать строчные буквы? (да/нет): ')
    include_symbols = input_yes_no('Включать символы? (да/нет): ')
    exclude_ambiguous = input_yes_no('Исключать неоднозначные символы (il1Lo0O)? (да/нет): ')

    if include_digits:
        chars.extend(digits)
    if include_upper:
        chars.extend(uppercase_letters)
    if include_lower:
        chars.extend(lowercase_letters)
    if include_symbols:
        chars.extend(punctuation)

    if not chars:
        print('Ошибка: не выбрано ни одного набора символов')
        return

    if exclude_ambiguous:
        chars = [c for c in chars if c not in ambiguous_chars]

    if length > len(chars):
        print(f'Ошибка: максимальная длина для выбранных символов - {len(chars)}')
        return

    print('\nСгенерированные пароли:')
    for _ in range(quantity):
        password = ''.join(random.sample(chars, length))
        print(password)


if __name__ == '__main__':
    generate_passwords()