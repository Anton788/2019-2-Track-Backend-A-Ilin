class Game:
    def __init__(self):
        self.field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def is_win(self, symbol):
        '''Victory Check'''
        main_diag = 0
        sup_diag = 0
        line = [0, 0, 0]
        collum = [0, 0, 0]
        for index in range(len(self.field)):
            if self.field[index] == symbol:
                line[index % 3] += 1
                collum[int(index / 3)] += 1
                if (index % 3) == int(index / 3):
                    main_diag += 1
                if ((index % 3) + int(index / 3)) == 2:
                    sup_diag += 1
        if main_diag == 3 or sup_diag == 3:
            return True
        for index in line:
            if index == 3:
                return True
        for index in collum:
            if index == 3:
                return True
        return False

    def start_game(self):
        '''Process of game'''
        for index in range(len(self.field)):
            if index % 3 == 0 and index != 0:
                print()
            print(index, end=' ')
        print()
        used_square = set()
        pos_numbers = set()
        for index in range(len(self.field)):
            pos_numbers.add(str(index))
        player = 1
        while len(used_square) < len(self.field):
            print("Введите позицию:")
            position = input()
            if position in used_square:
                print("Поле занято")
                continue
            if position in pos_numbers:
                used_square.add(position)
                if player % 2 == 1:
                    self.field[int(position)] = 'X'
                    if self.is_win('X'):
                        print("Выиграли : X")
                        self.show_field()
                        return 1
                    player += 1
                else:
                    self.field[int(position)] = 'O'
                    if self.is_win('O'):
                        print("Выиграли : O")
                        self.show_field()
                        return 2
                    player += 1
            else:
                print("Некорретный ввод")
                continue
            self.show_field()
        print("Игра окончена")
        return 3

    def show_field(self):
        '''Shows current field'''
        for index in range(len(self.field)):
            if index % 3 == 0 and index != 0:
                print()
            print(self.field[index], end=' | ')
        print()


if __name__ == '__main__':
    our_game = Game()
    our_game.start_game()
