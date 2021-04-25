"""
This model is to display the board for a new game.
"""


def draw_borad(boa):
	"""
	Print out the board in console for new game according data in 2d list
	param boa: A 2D list contain all the data for the game
	"""
	for raw in range(len(boa)):
		if raw % 3 == 0 and raw != 0:
			print("----------------------")
		for col in range(len(boa[raw])):
			print(draw_number(boa, raw, col), end=" ")
			if (col + 1) % 3 == 0 and col != 8:
				print("| ", end="")
			elif col == 8:
				print("")


def draw_number(boa, raw, col):
	"""
	Evaluate whether the spot should be empty or not
	param raw, col: the raw and column number of the element
	return: space if the number is 0, else return original value as string
	"""
	if boa[raw][col] == 0:
		return " "
	else:
		return str(boa[raw][col])

