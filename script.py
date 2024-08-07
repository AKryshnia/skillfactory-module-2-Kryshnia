def greeting():
    print("-------------------------------------------",
        " Приветствуем Вас в игре 'Крестики-Нолики'",
        "-------------------------------------------",
        "     Формат ввода: x y (через пробел), ",
        " сначала номер строки, затем номер столбца",
        "-------------------------------------------",
        sep='\n')

def show_playfield():
    print(" ")
    print("   | 0 | 1 | 2 | ")
    print("-----------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("-----------------")
    print()
def ask_coords():
    while True:
        coords = input("    Ваш ход: ").split()

        if len(coords) != 2:
            print(" ")
            print(" Введите 2 координаты! ")
            print(" ")
            continue

        x, y = coords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" ")
            print(" Введите числа! ")
            print(" ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" ")
            print(" Координаты вне диапазона! ")
            print(" ")
            continue

        if field[x][y] != " ":
            print(" ")
            print(" Клетка занята! ")
            print(" ")
            continue

        return x, y

def check_win():
    win_coords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coords:
        symbols = []
        for n in coord:
            symbols.append(field[n[0]][n[1]])
        if symbols == ["X", "X", "X"]:
            show_playfield()
            print(" Выиграли крестики! ")
            return True
        if symbols == ["0", "0", "0"]:
            show_playfield()
            print(" Выиграли нолики! ")
            return True
    return False

greeting()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show_playfield()
    if count % 2 == 1:
        print(" Ходит крестик ")
        print(" ")
    else:
        print(" Ходит нолик ")
        print(" ")

    x, y = ask_coords()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья ")
        break
