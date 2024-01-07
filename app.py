from PyQt5 import QtWidgets, uic, QtGui

import sys
from typing import List
from functools import partial


class TButton:
    sansFont = QtGui.QFont("Helvetica [Cronyx]", 22)

    def __init__(self, button: QtWidgets.QPushButton, row, col,func):

        button.row = row
        button.col = col
        button.ovdSetText = self.setText
        self.button = button
        button.setText(" ")
        button.setFont(self.sansFont)
        button.clicked.connect(partial(func, button))

    def setText(self, board, value):
        board[self.button.row][self.button.col] = value
        self.button.setText(value)

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.change_player = None

    def set_change_player(self, player):
        self.change_player = player

    def get_change_player (self):
        return self.change_player

    def __str__(self):
        return self.name


class Ui(QtWidgets.QWidget):
    init_board = lambda : [
        ["", "", "", ],
        ["", "", "", ],
        ["", "", "", ]
    ]


    board = init_board()

    PLAYER_X = Player("X", color="background-color: blue;")
    PLAYER_O = Player("O", color="background-color: green;")

    PLAYER_X.set_change_player(PLAYER_O)
    PLAYER_O.set_change_player(PLAYER_X)

    current_player = PLAYER_X


    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('tic-tac-toe.ui', self)

        self.ttt_buttons = [TButton(self.pushButton,   0, 0, self.button_clicked),
        TButton(self.pushButton_2, 0, 1, self.button_clicked),
        TButton(self.pushButton_3, 0, 2, self.button_clicked),
        TButton(self.pushButton_4, 1, 0, self.button_clicked),
        TButton(self.pushButton_5, 1, 1, self.button_clicked),
        TButton(self.pushButton_6, 1, 2, self.button_clicked),
        TButton(self.pushButton_7, 2, 0, self.button_clicked),
        TButton(self.pushButton_8, 2, 1, self.button_clicked),
        TButton(self.pushButton_9, 2, 2, self.button_clicked)]


        self.show()

    def button_clicked(self, button: TButton):

        button.ovdSetText(self.board, str(self.current_player))
        button.setDisabled(True)
        button.setStyleSheet(self.current_player.color)
        # button
        is_game_over, win_by = self.win_by_if_game_over()
        if is_game_over:
            self.show_info_messagebox(win_by=win_by)
            self.current_player = self.PLAYER_X
            self.board = Ui.init_board()
            for ttt_button in self.ttt_buttons:
                ttt_button.button.setText(" ")
                ttt_button.button.setEnabled(True)
                ttt_button.button.setStyleSheet("background-color: rgb(255, 255, 255)")
            return
        self.current_player = self.current_player.change_player


    def win_by_if_game_over(self, ):
        diagonal_1 = []
        diagonal_2 = []

        for idx in range(3):  # row and col iteration
            row_vals = set(self.board[idx])
            col_vals = set([self.board[row][idx] for row in range(3)])
            diagonal_1.append(self.board[idx][idx])
            diagonal_2.append(self.board[idx][-(idx + 1)])

            if len(row_vals) == 1 and (str(self.PLAYER_X) in row_vals or (str(self.PLAYER_O) in row_vals)):
                return True, row_vals.pop()

            if len(col_vals) == 1 and (str(self.PLAYER_X) in col_vals or (str(self.PLAYER_O) in col_vals)):
                return True, col_vals.pop()

        else:
            set_diagonal_1 = set(diagonal_1)
            set_diagonal_2 = set(diagonal_2)

            if len(set_diagonal_1) == 1 and (str(self.PLAYER_X) in set_diagonal_1 or (str(self.PLAYER_O) in set_diagonal_1)):
                return True, set_diagonal_1.pop()

            if len(set_diagonal_2) == 1 and (str(self.PLAYER_X) in set_diagonal_2 or (str(self.PLAYER_O) in set_diagonal_2)):
                return True, set_diagonal_2.pop()

        return False, None

    def show_info_messagebox(self, win_by):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        # setting message for Message Box
        msg.setText(f"Game won by {win_by}")

        # setting Message box window title
        msg.setWindowTitle("Game Over")

        # declaring buttons on Message Box
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        # start the app
        retval = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()



