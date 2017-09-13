from random import shuffle

def printboard(board):
    for i in board:
        print i

def generatedirtwith(num):
    number=list(range(100))
    shuffle(number)
    board=[[0]*10 for i in range(10)]
    for i in range(num):
        j=number[i]
        board[j/10][j%10]=1    
    printboard(board)
    return board

def generatedirt(matrixsize):
    number=list(range(matrixsize**2))
    shuffle(number)
    board=[[0]*matrixsize for i in range(matrixsize)]
    p=float(raw_input("Enter percentage of dirt you want to generate : "))
    while p < 0 or p >100:
        p = float(raw_input("Renter percentage in range 0 to 100 : "))
    p=int(round((p*matrixsize*matrixsize)/100))
    for i in range(p):
        j=number[i]
        board[j/matrixsize][j%matrixsize]=1    
    printboard(board)
    return board
    

if __name__ == '__main__':
    num=int(raw_input("Enter Matrix Size : "))
    generatedirt(num)
