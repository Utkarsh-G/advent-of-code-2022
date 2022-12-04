import sys
import time

with open(sys.argv[1], 'r') as f:
	pairs = f.readlines()

overlap_count = 0

start = time.time()
for pair in pairs:
	lots = pair.replace('-',',').split(',')
	set1 = set(range(int(lots[0]), int(lots[1])+1))
	set2 = set(range(int(lots[2]), int(lots[3])+1))
	is_overlap = set1 & set2
	if is_overlap:
		overlap_count += 1

end = time.time()
print (end - start)
print overlap_count 

