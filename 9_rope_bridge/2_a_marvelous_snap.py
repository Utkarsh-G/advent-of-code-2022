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
	
	map_of_snap = {(0,2):(0,1), (1,2):(1,1), (2,2):(1,1), (2,1):(1,1),
		(2,0):(1,0), (2,-1):(1,-1), (2,-2):(1,-1), (1,-2):(1,-1),
		(0,-2):(0,-1), (-1,-2):(-1,-1), (-2,-2):(-1,-1), (-2,-1):(-1,-1),
		(-2,0):(-1,0), (-2,1):(-1,1), (-2,2):(-1,1), (-1,2):(-1,1)}
	
	move = (0,0)
	if (diff_x, diff_y) in map_of_snap:
		move = map_of_snap[(diff_x, diff_y)]	
		
	return (tailp[0]+move[0], tailp[1]+move[1])
	
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
