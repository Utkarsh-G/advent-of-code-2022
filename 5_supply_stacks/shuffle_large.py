import sys

nums_stacks = sys.argv[1]

with open(sys.argv[2], 'r') as f:
	lines = f.readlines()

stacks = []
stacks.append(["R", "N", "F", "V", "L", "J", "S", "M"])
stacks.append(["P", "N", "D", "Z", "F", "J", "W", "H"])
stacks.append(["W", "R", "C", "D", "G"])
stacks.append(["N", "B", "S"])
stacks.append(["M", "Z", "W", "P", "C", "B", "F", "N"])
stacks.append(["P", "R", "M", "W"])
stacks.append(["R", "T", "N", "G", "L", "S", "W"])
stacks.append(["Q", "T", "H", "F", "N", "B", "V"])
stacks.append(["L", "M", "H", "Z", "N", "F"])
print stacks

for line in lines[10:]:
	words = line.split(" ")
	amount_to_be_moved = int(words[1])
	start_stack = int(words[3])
	target_stack = int(words[5])
	for i in range(amount_to_be_moved):
		stacks[target_stack-1].append(stacks[start_stack-1].pop())
	print stacks	
	
for stack in stacks:
	print stack[-1]
