board = [" "]*9                

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def player_move(board,player):
    while True:
        try:
            move=int(input(f"Player {player}, choose position(1-9): "))

            if move < 1 or move > 9:
                print("Choose a number between 1 and 9")
                continue

            if board[move - 1] == " ":
                board[move - 1] = player
                break
            
            else:
                print("Position taken already!")

        except ValueError as e:
            print("DEBUG:", e)
        
def check_winner(board):
    winning_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]

    for combo in winning_positions:
        a,b,c = combo

        if board[a]==board[b]==board[c] != " ":
            return board[a]
        
    return None
current_player="X"

while True:
    print_board(board)

    player_move(board,current_player)

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"Player {winner} wins!")
        break
    if " " not in board:
        print_board(board)
        print("It's a tie! 🤝")
        break

    current_player = "O" if current_player == "X" else "X"






