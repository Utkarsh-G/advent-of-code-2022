import sys

with open(sys.argv[1], 'r') as f:
	pairs = f.readlines()

subset_count = 0

for pair in pairs:
	lots = pair.replace('-',',').split(',')
	
	# ugh. Uglier to write, but likely more efficient than making set()s
	is_subset = (int(lots[0]) <= int(lots[2]) and int(lots[1]) >= int(lots[3])) or (int(lots[0]) >= int(lots[2]) and int(lots [1]) <= int(lots[3]))
	if is_subset:
		subset_count += 1

print subset_count 

