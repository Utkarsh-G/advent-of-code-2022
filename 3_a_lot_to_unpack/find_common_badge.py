import sys

with open(sys.argv[1], 'r') as f:
	rucksacks = f.readlines()

sum = 0

for index in range(0, len(rucksacks), 3):
	first_sack = set(rucksacks[index].strip())
	second_sack = set(rucksacks[index+1].strip())
	third_sack = set(rucksacks[index+2].strip())
	
	common_element = (first_sack & second_sack & third_sack).pop()	

	value_of_element = ord(common_element) - 38 if ord(common_element) < 91 else ord(common_element) - 96
	sum = sum + value_of_element

print(sum)
