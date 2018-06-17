class Tic_tac_toe:

    def draw_board(board):
        print("\033[35m---------------------------------------------------------------------")
        for i in range(10):     
            if i == 0:
                print ("| ", board[0+i*10], "  | ", board[1+i*10], "  | ", board[2+i*10], " |", board[3+i*10], "  | ", board[4+i*10], "  | ", board[5+i*10], "  | ", board[6+i*10], "  | ", board[7+i*10], "  | ", board[8+i*10], "  | ", board[9+i*10], " | ")
            elif i == 9:
                print ("| ", board[0+i*10], " | ", board[1+i*10], " | ", board[2+i*10], "|", board[3+i*10], " | ", board[4+i*10], " | ", board[5+i*10], " | ", board[6+i*10], " | ", board[7+i*10], " | ", board[8+i*10], " | ", board[9+i*10], "| ")
            else:
                print ("| ", board[0+i*10], " | ", board[1+i*10], " | ", board[2+i*10], "|", board[3+i*10], " | ", board[4+i*10], " | ", board[5+i*10], " | ", board[6+i*10], " | ", board[7+i*10], " | ", board[8+i*10], " | ", board[9+i*10], " | ")
            print ("---------------------------------------------------------------------")


    def history(player_token, player_answer):
        with open('history.txt', 'a') as f:
                    line = player_token + ' ' + str(player_answer) + '\n'
                    f.write(line)


    def take_input(player_token, board):
        global escape
        valid = False
        while not valid:
            player_answer = input("\033[37mWhere to put " + player_token+"? ")
            try:
                player_answer = int(player_answer)
            except:
                if player_answer == 'exit':
                    escape = True
                    break
                if player_answer == 'history':
                    print('\n')
                    with open('history.txt', 'r') as f:
                        for line in f.readlines():
                            print(line)
                    continue 
                print("Invalid input. Are you sure that you entered a number?")
                continue
            if player_answer >= 1 and player_answer <= 100:
                val = str(board[player_answer-1]).strip()
                if (val != '\033[32mO\033[35m' and val != '\033[32mX\033[35m'):
                    if player_answer < 10:
                        board[player_answer-1] = '\033[32m' + player_token +  '\033[35m'
                    else:
                        board[player_answer-1] = '\033[32m' + player_token + '\033[35m' + ' '
                    valid = True
                    Tic_tac_toe.history(player_token, player_answer)
                else:
                    print("This cell is already taken")
            else:
                print("Invalid input. Enter a number from 1 to 9.")


    def check_win(a):
        for i in range(10):
            for j in range(6):
                if str(a[j+i*10]).strip() == str(a[j+1+i*10]).strip() == str(a[j+2+i*10]).strip() == str(a[j+3+i*10]).strip() == str(a[j+4+i*10]).strip():
                    return a[j+i*10]
                elif str(a[i+j*10]).strip() == str(a[i+(j+1)*10]).strip() == str(a[i+(j+2)*10]).strip() == str(a[i+(j+3)*10]).strip() == str(a[i+(j+4)*10]).strip():
                    return a[i+j*10]
                elif str(a[i+j*10]).strip() == str(a[i+1+(j+1)*10]).strip() == str(a[i+2+(j+2)*10]).strip() == str(a[i+3+(j+3)*10]).strip() == str(a[i+4+(j+4)*10]).strip():
                    return a[i+j*10]
        for i in range(6):
            for j in list(reversed(range(5, 10))):
                if str(a[j+i*10]).strip() == str(a[(j-1)+(i+1)*10]).strip() == str(a[(j-2)+(i+2)*10]).strip() == str(a[(j-3)+(i+3)*10]).strip() == str(a[(j-4)+(4+i)*10]).strip():
                    return a[j+i*10]
        return False
