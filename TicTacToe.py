# Forst class and terminal game for learning
class Tictactoe:
    def __init__(self):
        self.marks = [" o ", " x "]
        self.s = " ---+---+--- "
        self.sign = ["   "]
        self.p = 0
        self.position = 0
        self.fields = self.sign * 9
        self.mark = self.marks[self.p]
        self.list_for_check_winner = []

    def drawing_board(self):
        print(self.s)
        print("|" + self.fields[0] + "|" + self.fields[1] + "|" + self.fields[2] + "|")
        print(self.s)
        print("|" + self.fields[3] + "|" + self.fields[4] + "|" + self.fields[5] + "|")
        print(self.s)
        print("|" + self.fields[6] + "|" + self.fields[7] + "|" + self.fields[8] + "|")
        print(self.s)

    def is_empty(self, pos: int):
        if self.fields[int(pos) - 1] == "   ":
            Tictactoe.change_player(self, pos)
        else:
            print("This position is not empty, write correct positon.")

    def change_player(self, position: int) -> int:
        self.position = position
        self.p = 1 - self.p
        self.mark = self.marks[self.p]
        if self.p == 1:
            self.fields[self.position - 1] = self.marks[0]
        elif self.p == 0:
            self.fields[self.position - 1] = self.marks[1]
        self.list_for_check_winner = [self.fields[i::3] for i in range(3)]
        return self.p

    @classmethod
    def is_full_board(cls, fields: list) -> False or True:
        if "   " not in fields:
            return True
        return False

    @staticmethod
    def check_winner(full_board: bool, check: list, sign: str) -> False or True:

        if full_board:
            print("Game Over. No one win.")
            return True

        if check:
            for i in range(3):
                if sign != '   ' and check[i].count(sign) == 3:  # all verticals
                    print(check[i])
                    print(f'Winner is Player_{sign.strip()}')
                    return True

            if check[0][0] == check[1][1] == check[2][2] != '   ':  # top-left to bottom-right
                print(f'Winner is Player{sign}')
                return True
            if check[0][2] == check[1][1] == check[2][0] != '   ':  # top-right to bottom-left
                print(f'Winner is Player{sign}')
                return True
            if check[0][0] == check[1][0] == check[2][0] != '   ':  # top horizontal
                print(f'Winner is Player{sign}')
                return True
            if check[0][1] == check[1][1] == check[2][1] != '   ':  # middle horizontal
                print(f'Winner is Player{sign}')
                return True
            if check[0][2] == check[1][2] == check[2][2] != '   ':  # bottom horizontal
                print(f'Winner is Player{sign}')
                return True
        return False


def valid_player_input(user_info: str, range_num: list) -> int or None:
    user_input = input(user_info)
    if user_input != "exit":
        if not user_input.replace(".", "").isdecimal():
            print("Input should be a number.")
            return None
        if user_input.count(".") > 0:
            print("Input should be integer number.")
            return None
        user_value = int(user_input)
        if user_value not in range_num:
            print(f"Value {user_value} not in range 1-9")
            return None
    else:
        user_value = "exit"
    return user_value


def main():
    tictactoe = Tictactoe()
    tictactoe.drawing_board()
    while True:
        try:
            sign = tictactoe.mark
            input_player = None
            while input_player is None:
                input_player = valid_player_input(f"Player_{sign.strip()} (as you read book 1-9):", list(range(1, 10)))
            if input_player == "exit":
                break
            tictactoe.is_empty(input_player)
            tictactoe.drawing_board()
            if Tictactoe.check_winner(Tictactoe.is_full_board(tictactoe.fields),
                                      tictactoe.list_for_check_winner, sign):
                break
        except KeyboardInterrupt:
            print("Interrupt")
            break


if __name__ == "__main__":
    main()
