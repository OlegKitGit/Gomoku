class Tic_tac_toe:

    def draw_board(board, counter):
        for i in range(10):
            for j in range(10):
                if i > 0 and j > 0 and counter == 0:
                    board[j+i*10] = '  '
                elif j == 0:
                    board[j+i*10] = i
        print("\033[35m---------------------------------------------------------------------")
        for i in range(10):     
            if i == 0:
                print ("| ", board[0+i*10], "  | ", board[1+i*10], "  | ", board[2+i*10], " |", board[3+i*10], "  | ", board[4+i*10], "  | ", board[5+i*10], "  | ", board[6+i*10], "  | ", board[7+i*10], "  | ", board[8+i*10], "  | ", board[9+i*10], " | ")
            else:
                print ("| ", board[0+i*10], "  | ", board[1+i*10], " | ", board[2+i*10], "|", board[3+i*10], " | ", board[4+i*10], " | ", board[5+i*10], " | ", board[6+i*10], " | ", board[7+i*10], " | ", board[8+i*10], " | ", board[9+i*10], " | ")
            print ("---------------------------------------------------------------------")


    def history(player_token, player_answer):
        with open('history.txt', 'a') as f:
                    line = player_token + ' ' + str(player_answer) + '\n'
                    f.write(line)

    def helper():
        print('\nIn order to win you need to put in a row five tokens\n')
    
    def take_input(player_token, board):
        valid = False
        while not valid:
            player_answer = input("\033[37mWhere to put " + player_token+"? ")
            try:
                player_answer_list = player_answer.split(',')
                player_answer_list[0] = int(player_answer_list[0])
                player_answer_list[1] = int(player_answer_list[1])
            except:
                if player_answer == 'exit':
                    return True
                    break
                if player_answer == 'history':
                    print('\n')
                    with open('history.txt', 'r') as f:
                        for line in f.readlines():
                            print(line)
                    continue
                if player_answer == 'helper':
                    Tic_tac_toe.helper()
                    continue
                print("Invalid input. Are you sure that you entered X,X?")
                continue
            if player_answer_list[0] >= 1 and player_answer_list[0] < 11 and player_answer_list[1] >= 1 and player_answer_list[1] < 10:
                val = str(board[player_answer_list[0] + player_answer_list[1]*10 - 1]).strip()
                if (val != '\033[32mO\033[35m' and val != '\033[32mX\033[35m'):
                    board[player_answer_list[0] + player_answer_list[1]*10 - 1] = '\033[32m' + player_token + '\033[35m' + ' '
                    valid = True
                    Tic_tac_toe.history(player_token, player_answer)
                else:
                    print("This cell is already taken")
            else:
                print("Invalid input. Enter a number from (1 to 10, 1 to 10)")
        return False

    def check_win(a):
        for i in range(10):
            for j in range(6):
                if str(a[j+i*10]).strip() == str(a[j+1+i*10]).strip() == str(a[j+2+i*10]).strip() == str(a[j+3+i*10]).strip() == str(a[j+4+i*10]).strip() == ('\033[32mO\033[35m' or '\033[32mX\033[35m'):
                    return a[j+i*10]
                elif str(a[i+j*10]).strip() == str(a[i+(j+1)*10]).strip() == str(a[i+(j+2)*10]).strip() == str(a[i+(j+3)*10]).strip() == str(a[i+(j+4)*10]).strip() == ('\033[32mO\033[35m' or '\033[32mX\033[35m'):
                    return a[i+j*10]
        for j in range(6):
            for i in range(6):
                if str(a[i+j*10]).strip() == str(a[i+1+(j+1)*10]).strip() == str(a[i+2+(j+2)*10]).strip() == str(a[i+3+(j+3)*10]).strip() == str(a[i+4+(j+4)*10]).strip() == ('\033[32mO\033[35m' or '\033[32mX\033[35m'):
                    return a[i+j*10]
        for i in range(6):
            for j in list(reversed(range(4, 10))):
                if str(a[j+i*10]).strip() == str(a[(j-1)+(i+1)*10]).strip() == str(a[(j-2)+(i+2)*10]).strip() == str(a[(j-3)+(i+3)*10]).strip() == str(a[(j-4)+(4+i)*10]).strip() == ('\033[32mO\033[35m' or '\033[32mX\033[35m'):
                    return a[j+i*10]
        return False
