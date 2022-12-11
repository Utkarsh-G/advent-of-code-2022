import sys

turn = 0
signal = 1

def print_20s(turn, signal, render):
	is_draw = True if (turn%40) >= signal and (turn%40) <= (signal+2) else False
	render += "#" if is_draw else "." #if turn == 20 or turn == 60 or turn == 100 or turn == 140 or turn == 180 or turn == 220:
		#print(signal)
	
		#print(render)
	if turn > 1 and (turn%40)==0:
		print(render)
		render = ""
	return render

with open(sys.argv[1], 'r') as f:
	line = f.readline()
	render = ""
	while line:
		instruction = line.strip().split(" ")
		
		if instruction[0]=="noop":
			turn += 1
			render = print_20s(turn, signal, render)
		
		if instruction[0]=="addx":
			for i in range(2):
				turn += 1
				render = print_20s(turn, signal, render)
			signal += int(instruction[1])

		line = f.readline()
		
