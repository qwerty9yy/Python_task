import random
from traceback import print_tb

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def quantity_pass():
    while True:
        n = input().lower()
        if n.isdigit():
            break
        else:
            print("Не могу разбрать! Введите число")
    return int(n)

def length_pass():
    while True:
        n = input().lower()
        if n.isdigit():
            break
        else:
            print("Не могу разбрать! Введите число")
    return int(n)

def Num_letter():
    while True:
        n = input().lower()
        if 'да' in n or 'нет' in n:
            break
        else:
            print('Простите не могу разобрать! Напишите "да" или "нет"')
    return n

def Caps_letter():
    while True:
        n = input().lower()
        if 'да' in n or 'нет' in n:
            break
        else:
            print('Простите не могу разобрать! Напишите "да" или "нет"')
    return n

def Lowercase_letters():
    while True:
        n = input().lower()
        if 'да' in n or 'нет' in n:
            break
        else:
            print('Простите не могу разобрать! Напишите "да" или "нет"')
    return n

def Symbols_letters():
    while True:
        n = input().lower()
        if 'да' in n or 'нет' in n:
            break
        else:
            print('Простите не могу разобрать! Напишите "да" или "нет"')
    return n

def Obscure_letters():
    while True:
        n = input().lower()
        if 'да' in n or 'нет' in n:
            break
        else:
            print('Простите не могу разобрать! Напишите "да" или "нет"')
    return n

def Generation():
    chars = []

    print('Сколько вам нужно паролей для генерации? (Введите число)')

    while True:
        quantity = quantity_pass()
        if quantity > 0:
            break
        else:
            print('Может все таки введем число больше 0')

    print('Какую длинну пароля сгенерировать?')
    while True:
        length = length_pass()
        if length > 0:
            break
        else:
            print('Может все таки введем число больше 0')

    print('Включать ли цифры? (да / нет)')
    num = Num_letter()
    if 'да' in num:
        chars.extend(digits)

    print('Включать ли прописные буквы? (да / нет)')
    caps = Caps_letter()
    if 'да' in caps:
        chars.extend(uppercase_letters)

    print('Включать ли строчные буквы? (да / нет)')
    lowercase = Lowercase_letters()
    if 'да' in lowercase:
        chars.extend(lowercase_letters)

    print('Включать ли символы? (да / нет)')
    symbols = Symbols_letters()
    if 'да' in symbols:
        chars.extend(punctuation)

    print('Исключать ли неоднозначные символы (il1Lo0O)? (да / нет)')
    obscure = Obscure_letters()
    if 'да' in obscure:
        if 'да' in lowercase:
            chars.remove('i')
            chars.remove('l')
            chars.remove('o')
        if 'да' in num:
            chars.remove('1')
            chars.remove('0')
        if 'да' in caps:
            chars.remove('L')
            chars.remove('O')

    for i in range(quantity):
        p = random.sample(chars, length)
        print(''.join(p))

Generation()
