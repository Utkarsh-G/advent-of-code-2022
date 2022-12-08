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
highest_scenic_score = 0
for i in range(num_row):
	for j in range(num_col):
		# edges
		if i==0 or j==0 or i==num_row-1 or j==num_col-1:
			score_left = 0
			score_right = 0
			score_up = 0
			score_down = 0
		else:
		# look left
			s_j = j
			while s_j > 0:
				s_j = s_j-1
				if trees[i][s_j].height >= trees[i][j].height:
					break
			score_left = j-s_j
			s_j = j # look right
			while s_j < num_col - 1:
				s_j = s_j+1
				if trees[i][s_j].height >= trees[i][j].height:
					break
			score_right = s_j - j
			s_i = i # look up
			while s_i > 0:
				s_i = s_i-1
				if trees[s_i][j].height >= trees[i][j].height:
					break
			score_up = i-s_i
			s_i = i # look down
			while s_i < num_row -1:
				s_i = s_i+1
				if trees[s_i][j].height >= trees[i][j].height:
					break
			score_down = s_i - i
		print(score_down, end=" ")
		score = score_left * score_right * score_down * score_up
		highest_scenic_score = score if score > highest_scenic_score else highest_scenic_score
		#
		#print(f"{trees[i][j].height}{trees[i][j].visible}", end=" ")
	print("\n")

print(num_visible_trees)
print(highest_scenic_score)
