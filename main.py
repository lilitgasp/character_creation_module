"""
Сейчас в модуле character_creation_module можно выделить три класса персонажей — Warrior, Mage и Healer.
Персонажи этих классов должны уметь атаковать,
защищаться и применять специальный навык, который доступен только им. Умения у всех персонажей одинаковые,
 но работают они по-разному,
именно поэтому в функциях, которые отвечают за способности персонажей, есть сложные if-блоки.
Эту логику нужно перенести в классы. То есть для каждого класса нужно определить методы атаки,
защиты и специального умения.
Избежать дублирования кода и упростить конструкции поможет базовый класс.
 Назовём его Character и объявим в этом классе общие методы и свойства.
Классы Warrior, Mage и Healer будут наследниками класса Character.
Откройте файл main.py модуля character_creation_module в редакторе кода и определите в нём структуру с учётом парадигмы ООП —
объявите родительский класс Character и дочерние классы Warrior, Mage и Healer. Вместо тела классов используйте эллипсис.
Далее перенесите код в поле сниппета, чтобы проверить себя.
"""


from random import randint

from graphic_arts.start_game_banner import run_screensaver

class Character:
    def __init__(self, name):
        self.name = name

    def attack(self, damage):
        """Наносит урон."""
        return (f'{self.name} нанёс урон противнику равный {damage}')


    def defence(self, block):
        """Блокирует урон."""
        return (f'{self.name} блокировал {block} урона')

    def special(self, skill, total):
        """Применяет специальное умение."""
        return (f'{self.name} применил специальное умение «{skill} {total}»')


class Warrior(Character):
    def attack(self):
        super().attack(5 + randint(3,5))

    def defence(self):
        super().defence(10 + randint(5, 10))

    def special(self):
        super().special("Выносливость", (80+25))


class Mage(Character):
    def attack(self):
        super().attack(5+ randint(5,10))

    def defence(self):
        super().defence(10 + randint(-2, 2))

    def special(self):
        super().special("Атака", (5 + 40))



class Healer(Character):
    def attack(self):
        super().attack(5+randint(-3,-1))

    def defence(self):
        super().defence(10 + randint(2, 5))

    def special(self):
        super().special("Защита" (10 + 30))









def attack(char_name: str, char_class: str) -> str:
    """Наносит урон."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {5 + randint(3,5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {5+ randint(5,10)}')

    return (f'{char_name} нанёс урон противнику равный {5+randint(-3,-1)}')


def defence(char_name: str, char_class: str) -> str:
    """Блокирует урон."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    """Применяет специальное умение."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость {80+25}»')

    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')

    return (f'{char_name} применил специальное умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Выводит сообщения."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        ('Введи одну из команд: attack — чтобы атаковать противника, '),
        ('defence — чтобы блокировать атаку противника или special '),
        ('- чтобы использовать свою суперсилу.'),
    )
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ""
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Да будет с вами сила сто сорока четырех."""
    approve_choice: str = ""
    char_class: str = ""
    while approve_choice != 'y':
        char_class = input(
            (('Введи название персонажа, за которого хочешь играть:'),
            ('Воитель — warrior, Маг — mage, Лекарь — healer: '))
        )
        if char_class == 'warrior':
            print(
                ('Воитель — дерзкий воин ближнего боя.'),
                ('Сильный, выносливый и отважный.'),
            )
        if char_class == 'mage':
            print(
                ('Маг — находчивый воин дальнего боя.'),
                ('Обладает высоким интеллектом.'),
            )
        if char_class == 'healer':
            print(
                ('Лекарь — могущественный заклинатель.'),
                ('Черпает силы из природы, веры и духов.'),
            )
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, чтобы выбрать другого персонажа ').lower()

    return char_class


def main() -> None:
    """Приветсвие заблудшего джедая."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

main()

if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))