import sys
import math

head_position = (0,0)
tail_position = (0,0)
tail_tracker = set()
tail_tracker.add(tail_position)

knots_position=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)] # 9

def new_tail_position(headp, tailp):
	diff_x = headp[0] - tailp[0]
	diff_y = headp[1] - tailp[1]
	new_tailp = tailp
		
	new_tailp_x = int((tailp[0]+headp[0])/2) if headp[0] > tailp[0] else int(math.ceil( (float(tailp[0])+float(headp[0]))/2  ))
	if headp==(-11,-4):
		print(f"h/t {headp}  {tailp}")
		print(int((tailp[1]+headp[1])/2))
	new_tailp_y = int((tailp[1]+headp[1])/2) if headp[1] > tailp[1] else int(math.ceil( (float(tailp[1])+float(headp[1]))/2  ))
	
	if headp==(-11,-5) or headp==(-11,-4) or tailp==(-10,-4):
		print(f"Head: {headp} tail:{tailp}")
		print(f"Special position, calculated x: {new_tailp_x}, y:{new_tailp_y}")
	#make it diagonal:
	if abs(diff_x) == 2 and abs(diff_y) == 1:
		new_tailp_y = headp[1]
	if abs(diff_y) == 2 and abs(diff_x) == 1:
		new_tailp_x = headp[0]	
	if headp==(-11,-4) or tailp==(-10,-4):
		print(f"Special position, post diag:  calculated x: {new_tailp_x}, y:{new_tailp_y}")
	return (new_tailp_x, new_tailp_y)
	
with open(sys.argv[1], 'r') as f:
	line = f.readline()
	while line:
		instruction = line.strip().split(" ")
		direction = instruction[0]
		steps = int(instruction[1])
		print(f"{direction} for {steps}")
		for i in range(steps):
			if direction == "R":
				head_position = (head_position[0]+1, head_position[1])
			if direction == "L":
				head_position = (head_position[0]-1, head_position[1])
			if direction == "U":
				head_position = (head_position[0], head_position[1]+1)
			if direction == "D":
				head_position = (head_position[0], head_position[1]-1)
			#tail_position = new_tail_position(head_position, tail_position)
			for j in range(9):
				if j == 0:
					knots_position[0] = new_tail_position(head_position, knots_position[0])
				else:
					knots_position[j] = new_tail_position(knots_position[j-1], knots_position[j])
				print(knots_position[j])
			tail_tracker.add(knots_position[8])
			#print(tail_tracker)
		line = f.readline()
print(len(tail_tracker))
print(tail_tracker)
