"""
This model is to read the game from or write the result to external txt file.
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


def output_game(boa):
	"""
	save the result from 2d list to txt file
	"""
	output = open('sudoku_result.txt', 'w')
	for element in boa:
		output.write(str(element)[1:-1])
		output.write('\n')
	output.close()
