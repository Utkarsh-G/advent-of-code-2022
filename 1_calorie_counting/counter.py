import pdb
with open("input_2") as input_file:
	list = input_file.readlines()
	highest_sum = 0
	current_sum = 0
	for item in list:
		#pdb.set_trace()
		if item == "\n":
			highest_sum = current_sum if current_sum > highest_sum else highest_sum
			current_sum = 0
		else:
			current_sum = current_sum + int(item)
	highest_sum = current_sum if current_sum > highest_sum else highest_sum
	print(highest_sum)
