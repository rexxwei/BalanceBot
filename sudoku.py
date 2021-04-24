"""
This program is to result the Sudoku puzzle game save in file "soduku.txt".
In soduku.py, there are 8 individual models to achieve respective purpose and the main function to call
these models. Run the sudoku.py file, the main function will result and display the game and result.
The result will print in Python console and automatically save in "sudoku_result.txt" at the same time.
"""


def start_game():
	"""
	read data from txt file to and save in 2D list
	return: 2d list contain the initial data
	"""
	b_list = []
	with open("sudoku.txt") as f: 	# import txt file data
		lines = f.readlines()
		for line in lines:
			line = line.replace("\n", "")
			ln = line.split(",")
			b_list.append(ln)
	boa = [list(map(int, i)) for i in b_list]
	return boa


def draw_borad(boa):
	"""
	Print out the board in console for new game according data in 2d list
	param boa: A 2D list contain all the data for the game
	"""
	for raw in range(len(boa)):
		if raw % 3 == 0 and raw != 0:
			print("----------------------")
		for col in range(len(boa[raw])):
			print(draw_number(raw, col), end=" ")
			if (col + 1) % 3 == 0 and col != 8:
				print("| ", end="")
			elif col == 8:
				print("")


def draw_number(raw, col):
	"""
	Evaluate whether the spot should be empty or not
	param raw, col: the raw and column number of the element
	return: space if the number is 0, else return original value as string
	"""
	if boa[raw][col] == 0:
		return " "
	else:
		return str(boa[raw][col])


def find_empty(boa):
	"""
	find the first empty spot on the board
	param board: the 2D list contain the game data
	return: A list containing the raw & col number, or None if board is full
	"""
	for raw in range(len(boa)):
		for col in range(len(boa[raw])):
			if boa[raw][col] == 0:
				return [raw, col]
	return None


def verify(boa, val, ind):
	"""
	verify potential value for an empty spot on the board according to Sudoku rule
	param board: the 2D list contain the game data
	param value: the potential value that might fit for the spot
	param ind: list contain index (row,col) of the spot
	return: True if the value is valid, or False if not
	"""
	# verify in the row
	for r in range(len(boa[0])):
		if boa[ind[0]][r] == val and r != ind[1]:
			return False
	# verify in the column
	for c in range(len(boa)):
		if boa[c][ind[1]] == val and c != ind[0]:
			return False
	# verify in the 3 x 3 block
	b_raw = ind[0] // 3		# get the row# of block
	b_col = ind[1] // 3		# get the col# of block
	for bi in range(b_raw*3, b_raw*3 + 3):
		for bj in range(b_col*3, b_col*3 + 3):
			if boa[bi][bj] == val and bi != ind[0] and bj != ind[1]:
				return False
	return True


def solution(boa):
	"""
	use backtrack algorithm to find solution for the whole game
	param board: 2d list contain data for the game
	"""
	free = find_empty(boa)		# find the first empty spot
	if free is None:			# if no empty spot
		return True
	else:						# else get the index of empty spot
		row, col = free
	for i in range(1, 10):		# try #1-9 for the spot
		if verify(boa, i, [row, col]):		# call model to verify
			boa[row][col] = i
			if solution(boa) is True:		# achieve backtrack algorithm through recursive calling
				return True
			boa[row][col] = 0
	return False


def result(boa):
	"""
	evaluate whether game has solution or not, print the conclusion
	param board: the 2D list contain the game
	"""
	# evaluate whether the game has solution and has been solved already
	if solution(boa) is True and find_empty(boa) is None:
		print("The solution is:")
	else:
		print("-No solution for puzzle-")


def output_game():
	"""
	save the result from 2d list to txt file
	"""
	output = open('sudoku_result.txt', 'w')
	for element in boa:
		output.write(str(element)[1:-1])
		output.write('\n')
	output.close()


if __name__ == "__main__":
	boa = start_game()					# obtain data to start game
	draw_borad(boa)						# display the board
	print("<===================>")		# separation line
	show_sol = "n"
	# accept input from user to decide show solution or not
	while str(show_sol).lower() != "y" and str(show_sol).lower() != "yes":
		show_sol = input("Want to see solution?[Y/N]: ")
	print("<===================>")
	result(boa)							# call model to solve the puzzle
	draw_borad(boa)						# display the board
	output_game()						# save data to txt file

