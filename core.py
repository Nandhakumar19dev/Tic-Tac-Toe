class TicTacToe:
    PLAYER_X = "X"
    PLAYER_O = "O"

    board = [
        ["", "", "", ],
        ["", "", "", ],
        ["", "", "", ]
    ]

    def __init__(self, board=None):

        if board is not None:
            self.board = board

    def set_val(self, position, value):
        row, col = position
        self.board[row][col] = value

    def is_click_position_valid(self, position):
        row, col = position
        return self.board[row][col] == ""

    def win_by_if_game_over(self, ):
        diagonal_1 = []
        diagonal_2 = []

        for idx in range(3):  # row and col iteration
            row_vals = set(self.board[idx])
            col_vals = set([self.board[row][idx] for row in range(3)])
            diagonal_1.append(self.board[idx][idx])
            diagonal_2.append(self.board[idx][-(idx + 1)])

            if len(row_vals) == 1 and (self.PLAYER_X in row_vals or (self.PLAYER_O in row_vals)):
                return True, row_vals.pop()

            if len(col_vals) == 1 and (self.PLAYER_X in col_vals or (self.PLAYER_O in col_vals)):
                return True, col_vals.pop()

        else:
            set_diagonal_1 = set(diagonal_1)
            set_diagonal_2 = set(diagonal_2)

            if len(set_diagonal_1) == 1 and (self.PLAYER_X in set_diagonal_1 or (self.PLAYER_O in set_diagonal_1)):
                return True, set_diagonal_1.pop()

            if len(set_diagonal_2) == 1 and (self.PLAYER_X in set_diagonal_2 or (self.PLAYER_O in set_diagonal_2)):
                return True, set_diagonal_2.pop()

        return False, None


if __name__ == "__main__":
    board = [
        ["X", "X", "X", ],
        ["", "", "", ],
        ["", "", "", ]
    ]

    print(TicTacToe(board=board).win_by_if_game_over())

    board = [
        ["X", "", "X", ],
        ["", "X", "", ],
        ["", "", "X", ]
    ]

    print(TicTacToe(board=board).win_by_if_game_over())

    board = [
        ["X", "X", "O", ],
        ["", "O", "", ],
        ["O", "", "", ]
    ]

    print(TicTacToe(board=board).win_by_if_game_over())
    print(TicTacToe(board=None).win_by_if_game_over())


