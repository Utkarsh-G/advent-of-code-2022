import pdb
def add_to_list(list2, newsum):
	if len(list2) < 3:
		list2.append(newsum)
		list2.sort()
	else:
		if newsum > list2[0]:
			list2[0]=newsum
			list2.sort()
	return list2

with open("input_2") as input_file:
	list = input_file.readlines()
	highest_sum = 0
	current_sum = 0
	top_three_list = []
	for item in list:
		#pdb.set_trace()
		if item == "\n":
			highest_sum = current_sum if current_sum > highest_sum else highest_sum
			
			top_three_list = add_to_list(top_three_list, current_sum)
			print(top_three_list)
			current_sum = 0
		else:
			current_sum = current_sum + int(item)
	highest_sum = current_sum if current_sum > highest_sum else highest_sum
	print(highest_sum)

	top_three_list = add_to_list(top_three_list, current_sum)
	print(top_three_list)
	print(top_three_list[0] + top_three_list[1] + top_three_list[2])


		
