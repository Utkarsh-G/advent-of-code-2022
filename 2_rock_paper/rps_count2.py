import sys

with open(sys.argv[1], 'r') as f:
	rps_lines = f.readlines()

# not proud of how much I had to think
# to make this matrix
matchup_scoring = {
	"A X": 3, "B Y": 5, "C Z": 7,
	"A Y": 4, "B Z": 9, "C X": 2,
	"A Z": 8, "B X": 1, "C Y": 6
}

sum = 0

for line in rps_lines:
	sum = sum + matchup_scoring[line.strip()]

print sum
