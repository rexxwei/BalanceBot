"""
This model is to find the solution for Sudoku game according to the rules.
"""


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
	param board: the 2D list contain the game info
	"""
	# evaluate whether the game has solution and has been solved already
	if solution(boa) is True and find_empty(boa) is None:
		print("The solution is:")
		return 1
	else:
		print("-No solution for puzzle-")
		return 1


def test_sol(boa):
	"""
	test this model is working properly
	param board: the 2D list contain the game info
	"""
	# evaluate whether the game has solution and has been solved already
	if len(find_empty(boa)) == 2 or find_empty(boa) is None:
		return True
