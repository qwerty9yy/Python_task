import random

def is_valid(n):
    return 0 <= n <= 100

print('Добро пожаловать в числовую угадайку\nХотите ссыграть в игру? (да/нет)')

cnt = 0

while True:
    otvet = input().split()
    if 'да' in otvet:
        print('Укажите правую границу для случайного выбора')
        border = int(input())
        guess_num = random.randint(0, border)

        print(f'Введите число от 0 до {border}')
        num = int(input())
        while True:
            if is_valid(num):
                cnt += 1
                if num < guess_num:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                elif num > guess_num:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                else:
                    print('Вы угадали, поздравляем!')
                    print(f'Колличество попыток {cnt}')
                    break
            else:
                print(f'А может быть все-таки введем целое число от 0 до {border}?')
            num = int(input())
        print('Спасибо, что играли в числовую угадайку. Хотите еще раз ссыграть? (да/нет)')
    elif 'нет' in otvet:
        print('Ждем вас в следущий раз!')
        break
    else:
        print('Простите я вас не понимаю! пожалуйта напишете (да/нет)')