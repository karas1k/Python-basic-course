import random

class LotoValues():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def game(self):
        self.boch = random.sample(range(1, 91), 90)
        while range(len(self.boch)):
            print(self.player, self.computer)
            number = self.boch.pop()
            print(f'Новый бочонок {number}, осталось бочонков {len(self.boch)}')
            answer = input("Зачеркнуть цифру? y/n: \nВведите 'q' что бы выйти из игры!")
            if answer == 'q':
                print("Вы вышли из игры!")
                break
            if answer == 'y':
                if not self.player.chek_line_number(number):
                    print(f'\nВы проиграли! Цифры {number} нет на вашей карточке!')
                    break
            elif self.player.chek_line_number(number):
                print(f'\nВы проиграли! Вы пропустили цифру {number}')
                break
            if self.computer.chek_line_number(number):
                pass

class Card:
    def __init__(self, player):
        self.player = player
        self.mas_list = []
        self.mas = [[] for i in range(3)]
        self.per = []
        self.line_number = 0

    def generate_card(self):
        for i in range(3):
            while len(self.mas[i]) < 5:
                self.rand = random.randint(1, 90)
                if self.rand not in self.per:
                    self.per.append(self.rand)
                    self.mas[i].append(self.rand)
            self.mas_list.append(sorted(self.mas[i]))

        return self.mas_list

    def chek_line_number(self, number):
        for index, line in enumerate(self.mas_list):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self.mas_list[index][num_index] = '*'
                    self.line_number += 1
                    if self.line_number == 15:
                        print(f'\n=======================================\n{self.player} победила!'
                              f'\n=======================================\n')
                    return True
        return False

    def __str__(self):
        card = ' ' * 7
        for i in self.mas_list:
            for j in i:
                card += str(j) + ' '
                if len(str(j)) != 2:
                    card += ' '
            card += '\n' + ' ' * 7
        return f'{self.player}\n\n{card}\n--------------------------\n'


player = Card('------ Ваша карточка -----')
player.generate_card()
computer = Card('-- Карточка компьютера ---')
computer.generate_card()

game = LotoValues(player, computer)
game.game()
