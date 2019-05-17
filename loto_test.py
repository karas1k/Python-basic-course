import random

def card_loto():

    mas_list = []
    mas = [[] * 5 for i in range(1, 91)]
    per = []

    for i in range(3):
        while len(mas[i]) < 5:

            rand = random.sample(range(1, 91), 1)

            if rand not in per:
                mas[i].extend(rand)
                mas[i] = sorted(mas[i])
                per.append(rand)

        mas_list.extend(mas[i])

    print(mas_list)
    return(mas_list)

player = card_loto()
computer = card_loto()

mas_boch = []
while len(mas_boch) != 90:

    boch = random.randint(1,90)

    if boch not in mas_boch:
        mas_boch.append(boch)
        if boch in player:
            player.remove(boch)
            print(f'Игрок {player}')
            print(f'Компутер {computer}')
        if boch in computer:
            computer.remove(boch)
            print(f'Игрок {player}')
            print(f'Компутер {computer}')

        if len(player) == 0:
            print("Победил игрок!")
            break

        if len(computer) == 0:
            print("Победил компутер!")
            break