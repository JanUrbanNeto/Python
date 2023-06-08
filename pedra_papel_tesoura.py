import random
import os

print("============================================")
print("Bem vindo ao jogo de Pedra, Papel ou Tesoura")
print("============================================\n")

move_list = ["pedra", "papel", "tesoura"]
player_score = 0
computer_score = 0

def increment(score):
    score +=1
    return score

def main_print():
    print("============================================")
    print("\nPlacar:")
    print(f"Você: {player_score}")
    print(f"Computador: {computer_score}")
    print("\nEscolha seu lance:\n0 - Pedra | 1 - Papel | 2 - Tesoura")


def select_computer_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise ValueError(f"{player_move} não é permitido")
            return move_list[player_move]

        except ValueError as input_error:
            print(input_error)

def select_winner(p_move, c_move):
    global player_score, computer_score

    if p_move == "pedra":
        if c_move == "tesoura":
            player_score += 1
            return "p"
        elif c_move == "papel":
            computer_score += 1
            return "c"
        else:
            return "d"

    if p_move == "papel":
        if c_move == "pedra":
            player_score += 1
            return "p"
        elif c_move == "tesoura":
            computer_score += 1
            return "c"
        else:
            return "d"

    if p_move == "tesoura":
        if c_move == "papel":
            player_score += 1
            return "p"
        elif c_move == "pedra":
            computer_score += 1
            return "c"
        else:
            return "d"

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_computer_move()
    winner = select_winner(player_move, computer_move)

    print("\n========================================")
    print(f"Sua jogada: {player_move.upper()}")
    print(f"Jogada do Computador: {computer_move.upper()}")
    
    if winner == "p":
        print("Você venceu essa rodada!")
    elif winner == "c":
        print("O computador venceu essa rodada")
    else:
        print("Empate")
    print("=========================================")
    
    while True:
        print("Jogar novamente? 0 - SIM | 1 NÃO")
        decisao = int(input())
        if decisao == 0:
            break
        elif decisao == 1:
            again = 0
            break

    os.system("cls")
