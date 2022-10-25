from tabnanny import check
from board import Board
from point import Point
from os import system

def show_introduction():
    with open('intro.txt') as file:
        intro = file.read()
        print(intro)

def check_victory(defending_player:Board):
    for line in defending_player.board:
        for column in line:
            if column == 'O':
                return False
    return True

def attack_possible(position:Point, board:Board):
    if 0 <= position.x < 10 and 0 <= position.y < 10 and board.board[position.x][position.y] == '_':
        return True
    return False

def print_boards(player1_name, board_p1, player2_name, board_p2):
    print(" "*20, player1_name, " "*48, player2_name)
    for i in range(10):
        print(board_p1.board[i], "  ", board_p2.board[i])

def attack(attacking_player:Board, defending_player:Board, blank_board: Board):
    while True:
        while True:
            attack_position = input(f"É a vez do {attacking_player.name}. Insira a posição que deseja atacar: ").split()
            if len(attack_position) == 2:
                break
            else:
                print("Valor inválido, tente novamente\n\n")
        attack_point = Point(int(attack_position[0]), int(attack_position[1]))
        if attack_possible(attack_point, blank_board):
            if defending_player.board[int(attack_position[0])][int(attack_position[1])] == 'O':
                defending_player.board[int(attack_position[0])][int(attack_position[1])] = 'X'
                blank_board.board[int(attack_position[0])][int(attack_position[1])] = "X"
                print("CABUM, ACERTOU")
                if check_victory(defending_player):
                    return True
            else:
                defending_player.board[int(attack_position[0])][int(attack_position[1])] = 'E'
                blank_board.board[int(attack_position[0])][int(attack_position[1])] = "E"
                print("SPLASH. ERROU")
                return blank_board
        else:
            print("Não foi possível atacar a posição selecionada, tente novamente")

def play_game(player1:Board, player2:Board):
    player1_blank_board = Board('Player1_blank_board')
    player2_blank_board = Board('Player2_blank_board')
    print_boards(player1_name=player1.name, player2_name=player2.name, board_p1=player1_blank_board, board_p2=player2_blank_board)
    while True:
        player2_blank_board = attack(player1, player2, player2_blank_board)
        if player2_blank_board == True:
            return player1.name
        print_boards(player1_name=player1.name, player2_name=player2.name, board_p1=player1_blank_board, board_p2=player2_blank_board)
        player1_blank_board = attack(player2, player1, player1_blank_board)
        if player1_blank_board == True:
            return player2.name
        print_boards(player1_name=player1.name, player2_name=player2.name, board_p1=player1_blank_board, board_p2=player2_blank_board)


def main():
    show_introduction()
    input('Press Enter to Start...')

    system('clear')
    player1 = Board(input('Insira o nome do jogador 1: '))
    print("Agora insira a posição de seus navios")
    player1.position_fleet()
    player1.print_board()
    print("Agora é a vez do player 2 inserir suas informações")
    input('Press enter para deixar o player 2 entrar')
    
    system('clear')
    player2 = Board(input('Insira o nome do jogador 2: '))
    print("Agora insira a posição de seus navios")
    player2.position_fleet()
    player2.print_board()

    print("Tropas posicionadas, é hora da batalha")
    input('Press enter para começar o jogo')

    system('clear')
    winner = play_game(player1, player2)
    system('cls')
    print_boards(player1_name=player1.name, player2_name=player2.name, board_p1=player1, board_p2=player2)
    print(f"{winner} Venceu!")
    

if __name__=='__main__':
    main()