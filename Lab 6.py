import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board




#Question 1.
# a)

def square_num(i):
    l=((i-1)//3, i-1-(3*int(i/3)))
    return l

#Question 1.
#b)
    #v1 (used in code)
def put_in_board(b, m, s):
    b[s[0]][s[1]]=m

    #v2
def put_in_board_2(board, mark, square_num):
    coord = square_num(square_num)
    board[coord[0]][coord[1]] = mark
    return board

#Question 2.
# a)

def get_free_squares(board):
    ans= []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if(board[r][c] == " "):
                ans.append([r,c])
    return ans

#Question 2.
#b)

def make_random_move(board, mark):
    f=get_free_squares(board)
    rand =int(len(f)*random.random())
    put_in_board(board, mark, f[rand])



#Question 3
# a)

def is_row_all_marks(board, row, mark):
    for c in board[row]:
        if(c!=mark):
            return False
    return True

#Question 3
# b)

def is_col_all_marks(board, col, mark):
    for r in board:
        if(r[col]!=mark):
            return False
    return True

#Question 3
# c)

def is_win(board, mark):
    for i in range(2):
        if(is_row_all_marks(board, i, mark)):
            return True
        if(is_col_all_marks(board, i, mark)):
            return True

    if(board[0][0]==board[1][1]==board[2][2]==mark):
        return True
    if(board[2][0]==board[1][1]==board[0][2]==mark):
        return True

    return False


#Question 4.
#a) +  b)

def computer_move(board, mark):
    if(mark=="O"):
        opponent="X"
    else:
        opponent="O"


    if(best_move(board, mark)!=[-1,-1]):
        print("\n")
        print_board_and_legend(board)
    elif(best_opponent_move(board, opponent)!=[-1,-1]):
        put_in_board(board, mark, best_opponent_move(board, opponent))
    else:make_random_move(board,mark)






def best_move(board, mark):
    f=get_free_squares(board)
    for m in f:
        put_in_board(board, mark, m)
        if(is_win(board, mark)):
            return m
        else:
            put_in_board(board, " ", m)
    return [-1,-1]



def best_opponent_move(board, mark):
    f=get_free_squares(board)
    for m in f:
        put_in_board(board, mark, m)
        if(is_win(board, mark)):
            put_in_board(board, " ", m)
            return m
        else:
            put_in_board(board, " ", m)
    return [-1,-1]

def is_full(board):
    for r in board:
        for c in r:
            if(c==" "):
                return False
    return True



if __name__ == '__main__':
    run = True
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    print_board_and_legend(board)

    print(square_num(8))
    put_in_board(board, "X", square_num(8))
    print_board_and_legend(board)
    print("----------------------------------------")
    print(get_free_squares(board))
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    print("\n\n\n")

    #Question 1.  c)  +  Question 2.  c)  +  Question 3.  d)

    while(run):
        print("\n")
        print_board_and_legend(board)
        print("\n")
        print("Player one's turn.")
        num=int(input("Enter move: "))
        put_in_board(board, "X", square_num(num))
        if(is_win(board, "X")):
            run = False
            print("\n\n\n")
            print("P l a y e r   1   W O N !!   ")
        if(get_free_squares(board)==[]):
            run= False
            print("\n\n")
            print_board_and_legend(board)
            print()
            print("Y 'A L L   T I E D ")
            break
        computer_move(board, "O")
        if(is_win(board, "O")):
            run = False
            print("\n\n\n")
            print("P l a y e r   2   W O N !!  " )


















