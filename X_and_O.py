import sys

def start():
	print('Please enter the name of player 1:')
	player_x = (sys.stdin.readline()).strip()
	print("{} is X's and will go first\n".format(player_x))
	print('Please enter the name of player 2:')
	player_o = (sys.stdin.readline()).strip()
	print("{} is O's and will go second\n".format(player_o))

	return(player_x, player_o)

def main():
	player_x, player_o = start()


	

if __name__ == '__main__':
	main()


# names
# while the game is not over:
#	player move
#	print board
#	check for win

# print result