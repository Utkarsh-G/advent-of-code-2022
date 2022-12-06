import sys

nums_stacks = sys.argv[1]

with open(sys.argv[2], 'r') as f:
	lines = f.readlines()

stacks = []
stacks.append(["Z", "N"])
stacks.append(["M", "C", "D"])
stacks.append(["P"])
print stacks

for line in lines[5:]:
	words = line.split(" ")
	amount_to_be_moved = int(words[1])
	start_stack = int(words[3])
	target_stack = int(words[5])
	stacks[target_stack-1]=stacks[target_stack-1]+stacks[start_stack-1][-amount_to_be_moved:]
	stacks[start_stack-1]=stacks[start_stack-1][0:-amount_to_be_moved]
 #stacks[target_stack-1].append(stacks[start_stack-1].pop())
	print stacks	
	
