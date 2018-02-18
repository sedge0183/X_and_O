import sys

def start():
	print('Please enter the name of player 1:')
	player_x = (sys.stdin.readline()).strip()
	print("{} is X's and will go first\n".format(player_x))
	print('Please enter the name of player 2:')
	player_o = (sys.stdin.readline()).strip()
	print("{} is O's and will go second\n".format(player_o))

	return[player_x, player_o]


def printboard(board):
	print('{}|{}|{}'.format(board[0], board[1], board[2]))
	print('-|-|-')
	print('{}|{}|{}'.format(board[3], board[4], board[5]))
	print('-|-|-')
	print('{}|{}|{}'.format(board[6], board[7], board[8]))
	print()


def playermove(board, sign):
	while 1 != 0:
		number = (sys.stdin.readline()).strip()
		print()
		try:
			number = int(number)
			position = number - 1
			try:
				if str(board[position]).isnumeric():
					board[position] = sign
					return(board)
					
				else:
					print('That position has already been taken. Please select another.')
				
			except IndexError:
				print("{} is not a vaild position. Please select another".format(number))
		except ValueError:
			print("'{}' is not a number. Please select a valid position".format(number))


def check(b):
	# vertical line checks
	i = 0
	while i < 3:
		if b[i] == b[i + 3] == b[i + 6]:
			return(True)
		i += 1

	# horizontal line check
	i = 0
	while i < 8:
		if b[i] == b[i + 1] == b[i + 2]:
			return(True)
		i += 3

	# diagnol line check
	if b[0] == b[4] == b[8]:
		return(True)
	
	elif b[2] == b[4] == b[6]:
		return(True)

def checkdraw(b):
	i = 0
	while i < len(b) and str(b[i]).isalpha():
		i += 1

	if i == len(b):
		return(True)

def main():
	players = start()
	sign = ['X', 'O']
	board = [number for number in range(1, 10)]
	turn = 1
	result = None
	draw = None

	while result == None and draw == None:
		printboard(board)
		
		turn = 1 - turn
		print("{}'s turn. Please choose an availible position.".format(players[turn]))
		playermove(board, sign[turn])		

		result = check(board)
		draw = checkdraw(board)

	printboard(board)

	if result != None:
		print("{} has won!! Conglaturation!".format(players[turn]))

	else:
		print("The game is a draw.")


if __name__ == '__main__':
	main()


# names
# while the game is not over:
#	print board
#	player move
#	check for win, draw

# print result, boardm