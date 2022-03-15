"""
TicTacToe Class - Terminal game.
Fields numbered from 1 (top left corner)
to 9 (bottom right corner).
"""


class TicTacToe:
    """Tic Tac Toe Class.
    Parameters (str): mark_1 default is "O",
                      mark_2: default is "X".
    """
    def __init__(self, mark_1="O", mark_2="X"):
        self.marks = [" " + mark_1 + " ", " " + mark_2 + " "]
        self.board_line = " ---+---+--- "
        self.sign = ["   "]
        self.swich_p = 0
        self.position = 0
        self.fields = self.sign * 9
        self.mark = self.marks[self.swich_p]
        self.list_for_check_winner = []

    def drawing_board(self):
        """Drawing a board"""
        print(self.board_line)
        print("|" + self.fields[0] + "|" + self.fields[1] + "|" + self.fields[2] + "|")
        print(self.board_line)
        print("|" + self.fields[3] + "|" + self.fields[4] + "|" + self.fields[5] + "|")
        print(self.board_line)
        print("|" + self.fields[6] + "|" + self.fields[7] + "|" + self.fields[8] + "|")
        print(self.board_line)

    def is_empty(self, pos: int):
        """Check if chosen field is empty. pos: input player 1-9 int"""
        if self.fields[int(pos) - 1] == "   ":
            TicTacToe.change_player(self, pos)
        else:
            print("Field is not empty, chose correct position.")

    def change_player(self, position: int) -> int:
        """Change current player and his mark "O" <--> "X".
        Create list for check winners function.
        """
        self.position = position
        self.swich_p = 1 - self.swich_p
        self.mark = self.marks[self.swich_p]
        if self.swich_p == 1:
            self.fields[self.position - 1] = self.marks[0]
        elif self.swich_p == 0:
            self.fields[self.position - 1] = self.marks[1]
        self.list_for_check_winner = [self.fields[i::3] for i in range(3)]
        return self.swich_p

    @classmethod
    def is_full_board(cls, fields: list) -> False or True:
        """Check if board is full"""
        if "   " not in fields:
            return True
        return False

    @staticmethod
    def check_winner(full_board: bool, check: list, sign: str) -> False or True:
        """Check who win the game.
        full_board: bool, check: list from class Tic_Tac_Toe.
        sigh: str, to show who winn (X or O)"""
        if full_board:
            print("Game Over. No one win.")
            return True

        if check:
            for i in range(3):
                if sign != '   ' and check[i].count(sign) == 3:
                    # all verticals
                    print(f'Winner is Player {sign.strip()}')
                    return True

            if check[0][0] == check[1][1] == check[2][2] != '   ':
                # top-left to bottom-right
                print(f'Winner is Player{sign}')
                return True
            if check[0][2] == check[1][1] == check[2][0] != '   ':
                # top-right to bottom-left
                print(f'Winner is Player{sign}')
                return True
            if check[0][0] == check[1][0] == check[2][0] != '   ':
                # top horizontal
                print(f'Winner is Player{sign}')
                return True
            if check[0][1] == check[1][1] == check[2][1] != '   ':
                # middle horizontal
                print(f'Winner is Player{sign}')
                return True
            if check[0][2] == check[1][2] == check[2][2] != '   ':
                # bottom horizontal
                print(f'Winner is Player{sign}')
                return True
        return False


def valid_player_input(user_info: str, range_num: list) -> int or None:
    """Validation: user input should be integer in range 1-9
    If not return None, else return user_value = user_input
    """
    # Validation user input
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
    """Start Game"""
    tic_tac_toe = TicTacToe("A", "B")
    tic_tac_toe.drawing_board()
    while True:
        try:
            sign = tic_tac_toe.mark
            input_player = None
            while input_player is None:
                input_player = valid_player_input(f"Player_{sign.strip()} (as you read book 1-9):",
                                                  list(range(1, 10)))
            if input_player == "exit":
                break

            tic_tac_toe.is_empty(input_player)
            tic_tac_toe.drawing_board()
            if tic_tac_toe.check_winner(tic_tac_toe.is_full_board(tic_tac_toe.fields),
                                      tic_tac_toe.list_for_check_winner, sign):
                break
        except KeyboardInterrupt:
            print("Interrupt")
            break


if __name__ == "__main__":
    main()
