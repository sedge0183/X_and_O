import sys

def start():
	print('Please enter the name of player 1:')
	player_x = (sys.stdin.readline()).strip()
	print("{} is X's and will go first\n".format(player_x))
	print('Please enter the name of player 2:')
	player_o = (sys.stdin.readline()).strip()
	print("{} is O's and will go second\n".format(player_o))

	return(player_x, player_o)


def printboard(board):
	print('{}|{}|{}'.format(board[0], board[1], board[2]))
	print('-|-|-')
	print('{}|{}|{}'.format(board[3], board[4], board[5]))
	print('-|-|-')
	print('{}|{}|{}'.format(board[6], board[7], board[8]))


def main():
	players = start()
	board = [number for number in range(1, 10)]
	turn = 0
	result = None
	draw = False

	print(board)
	while result == None and draw == False:
		printboard(board)
		print()
		
		print("{}'s turn. Please choose an availible position.".format(players[turn]))
		

		turn = 1 - turn		


		result = True

if __name__ == '__main__':
	main()


# names
# while the game is not over:
#	print board
#	player move
#	check for win

# print result, board