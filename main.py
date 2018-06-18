from gomoku.gomoku import Gomoku
board = list(range(1,101))
counter = 0
win = False
escape = False
with open('history.txt', 'w') as f:
        f.close()
while not win:
	Gomoku.draw_board(board, counter)
	if counter % 2 == 0:
                escape = Gomoku.take_input("X", board)
	else:
		escape = Gomoku.take_input("O", board)
	if escape == True:
		break
	counter += 1
	if counter > 8:
		tmp = Gomoku.check_win(board)
		if tmp:
			Gomoku.draw_board(board, counter)
			print(tmp, "Win!")
			win = True
			break
	if counter == 100:
		Gomoku.draw_board(board, counter)
		print("Draw!")
		break
   

