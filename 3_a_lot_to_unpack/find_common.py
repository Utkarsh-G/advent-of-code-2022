import sys

with open(sys.argv[1], 'r') as f:
	rucksacks = f.readlines()

sum = 0

for rucksack in rucksacks:
	first_compartment = rucksack[0:len(rucksack)/2]
	second_compartment = rucksack[len(rucksack)/2:-1]
	unique_first = set(first_compartment)
	unique_second = set(second_compartment)
	common_element = (unique_first & unique_second).pop()	

	value_of_element = ord(common_element) - 38 if ord(common_element) < 91 else ord(common_element) - 96
	sum = sum + value_of_element

print(sum)
