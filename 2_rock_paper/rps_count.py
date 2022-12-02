import sys

with open(sys.argv[1], 'r') as f:
	rps_lines = f.readlines()

shape_scoring = {"X": 1, "Y": 2, "Z": 3}

matchup_scoring = {
	"A X": 3, "B Y": 3, "C Z": 3,
	"A Y": 6, "B Z": 6, "C X": 6,
	"A Z": 0, "B X": 0, "C Y": 0
}

sum = 0

for line in rps_lines:
	sum = sum + matchup_scoring[line.strip()] + shape_scoring[line[2]]

print sum
