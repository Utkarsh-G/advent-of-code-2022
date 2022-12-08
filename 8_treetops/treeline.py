import sys

num_col = 0
num_row = 0
trees = []

class Tree:
	def __init__(self, height):
		self.height = height
		self.visible = False

	def setVisible(self):
		self.visible = True

with open(sys.argv[1], 'r') as f:
	line = f.readline().strip()
	#num_row = 1
	num_col = len(line)
	print(num_col)
	row_index = 0
	while line:
		num_row +=1
		tallest_in_row = -1
		col_index = 0
	

		trees.append([])
		for char in line:
			height = int(char)
			trees[row_index].append(Tree(height))
			if height > tallest_in_row:
				trees[row_index][col_index].setVisible()
				tallest_in_row = height
			col_index += 1

		#another pass, going backwards this time
		tallest_in_row = -1
		for i in range(num_col - 1, 0, -1):
			this_tree = trees[row_index][i]
			if this_tree.height > tallest_in_row:
				this_tree.setVisible()
				tallest_in_row = this_tree.height

		line = f.readline().strip()
		row_index += 1
		
tallest_in_column = -1

for j in range(num_col):
	for i in range(num_row):
		if trees[i][j].height > tallest_in_column:
			trees[i][j].setVisible()
			tallest_in_column = trees[i][j].height
	tallest_in_column = -1

	for i in range(num_row-1, 0, -1):
		if trees[i][j].height > tallest_in_column:
			trees[i][j].setVisible()
			tallest_in_column = trees[i][j].height
	tallest_in_column = -1

num_visible_trees = 0
for i in range(num_row):
	for j in range(num_col):
		if trees[i][j].visible:
			num_visible_trees += 1
		print(f"{trees[i][j].height}{trees[i][j].visible}", end=" ")
	print("\n")

print(num_visible_trees)
