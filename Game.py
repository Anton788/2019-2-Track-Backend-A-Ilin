class Game:
    def __init__(self):
        self.field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_win(self, symbol):
        main_diag = 0
        sup_diag = 0
        line = [0, 0 ,0]
        collum = [0, 0, 0]
        for i in range(len(self.field)):
            if self.field[i] == symbol:
                line[i % 3] += 1
                collum[int(i / 3)] += 1
                if (i % 3) == int(i / 3):
                    main_diag += 1
                if ((i % 3) + int(i / 3)) == 2:
                    sup_diag += 1
        if main_diag == 3 or sup_diag == 3:
            return True
        for i in line:
            if i == 3:
                return True
        for i in collum:
            if i == 3:
                return True
        return False

    def start_game(self):
        for i in range(len(self.field)):
            if i % 3 == 0 and i != 0:
                print()
            print(i, end=' ')
        print()
        used_square = set()
        pos_numbers = set()
        for i in range(len(self.field)):
            pos_numbers.add(str(i))
        player = 1
        while len(used_square) < len(self.field):
            print("Введите позицию:")
            position = input()
            if position in used_square:
                print("Поле занято")
                continue
            elif not (position in pos_numbers):
                print("Некорретный ввод")
                continue
            else:
                used_square.add(position)
                if player % 2 == 1:
                    self.field[int(position)] = 'X'
                    if self.is_win('X'):
                        print("Выиграли : X")
                        game.show_field()
                        return 1
                    player += 1
                else:
                    self.field[int(position)] = 'O'
                    if self.is_win('O'):
                        print("Выиграли : O")
                        game.show_field()
                        return 2
                    player += 1
            game.show_field()
        print("Игра окончена")
        return 3

    def show_field(self):
        for i in range(len(self.field)):
            if i % 3 == 0 and i != 0:
                print()
            print(self.field[i], end=' | ')
        print()


if __name__ == '__main__':
    game = Game()
    game.start_game()
