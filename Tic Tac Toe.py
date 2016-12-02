
def main():
    board = drawBoard()

#Draw the 3x3 Tic Tac Toe board    
def drawBoard():
    a = '---'.join('    ')
    b = '   '.join('||||')
    print('\n'.join((a,b,a,b,a,b,a)))

main()
