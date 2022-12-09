import sys

head_position = (0,0)
tail_position = (0,0)
tail_tracker = set()
tail_tracker.add(tail_position)

def new_tail_position(headp, tailp, tail_tracker):
	diff_x = headp[0] - tailp[0]
	diff_y = headp[1] - tailp[1]
	new_tailp = tailp
	if diff_x > 1:
		new_tailp = (headp[0]-1, headp[1])
	if diff_x < -1:
		new_tailp = (headp[0]+1, headp[1])
	if diff_y > 1:
		new_tailp = (headp[0], headp[1]-1)
	if diff_y < -1:
		new_tailp = (headp[0], headp[1]+1)
	tail_tracker.add(new_tailp)
	return new_tailp


with open(sys.argv[1], 'r') as f:
	line = f.readline()
	while line:
		instruction = line.strip().split(" ")
		direction = instruction[0]
		steps = int(instruction[1])
		for i in range(steps):
			if direction == "R":
				head_position = (head_position[0]+1, head_position[1])
			if direction == "L":
				head_position = (head_position[0]-1, head_position[1])
			if direction == "U":
				head_position = (head_position[0], head_position[1]+1)
			if direction == "D":
				head_position = (head_position[0], head_position[1]-1)
			tail_position = new_tail_position(head_position, tail_position, tail_tracker)
		line = f.readline()
print(len(tail_tracker))
