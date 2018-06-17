from tic_tac_toe.tic_tac_toe import Tic_tac_toe
global escape
board = list(range(1,101))
counter = 0
win = False
escape = False
with open('history.txt', 'a') as f:
        f.close()
while not win:
	Tic_tac_toe.draw_board(board)
	if counter % 2 == 0:
			Tic_tac_toe.take_input("X", board)
	else:
			Tic_tac_toe.take_input("O", board)
	if escape == True:
		break
	counter += 1
	if counter > 8:
		tmp = Tic_tac_toe.check_win(board)
		if tmp:
			Tic_tac_toe.draw_board(board)
			print(tmp, "Win!")
			win = True
			break
	if counter == 100:
		Tic_tac_toe.draw_board(board)
		print("Draw!")
		break
   

