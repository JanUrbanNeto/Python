import random
import os


class JogoDaVelha:
    def __init__(self):
        self.reset_board()

    def print_board(self):
        print("")
        print(
            " " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2]
        )
        print("------------")
        print(
            " " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2]
        )
        print("------------")
        print(
            " " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2]
        )

    def reset_board(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            # verificar se alguma linha venceu
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            # verificar se alguma coluna venceu
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            # verificar se alguma diagonal venceu
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "x"
            print("X venceu!")
            return
        elif dict_win["O"]:
            self.done = "o"
            print("O venceu!")
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c += 1
                    break

        if c == 0:
            print("Empate")

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("digite a linha para seu próximo lance:")
                x = int(input())

                print("Digite a coluna para seu próximo lance:")
                y = int(input())

                if x < 0 or x > 2 or y < 0 or y > 2:
                    print("Posição inválida no tabuleiro")
                    continue

                if self.board[x][y] != " ":
                    print("Posição já contém uma jogada!")
                    continue

            except Exception as error:
                print(error)
                continue

            invalid_move = False

        self.board[x][y] = "X"

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))

        if len(list_moves) > 0:
            x, y = random.choice(list_moves)
            self.board[x][y] = "0"


jogo_da_velha = JogoDaVelha()
jogo_da_velha.print_board()
next = 0

while next == 0:
    os.system("cls")
    jogo_da_velha.print_board()
    while jogo_da_velha.done == "":
        jogo_da_velha.get_player_move()
        jogo_da_velha.make_move()
        os.system("cls")
        jogo_da_velha.print_board()
        jogo_da_velha.check_win_or_draw()

    print("digite 1 para sair ou qualquer tecla para jogar novamente!")

    next == int(input())
    if next == 1:
        break
    else:
        jogo_da_velha.reset_board()
        next = 0
