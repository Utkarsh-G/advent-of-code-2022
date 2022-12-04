import sys

with open(sys.argv[1], 'r') as f:
	pairs = f.readlines()

overlap_count = 0

for pair in pairs:
	lots = pair.replace('-',',').split(',')
	start1 = int(lots[0])
	end1 = int(lots[1])	
	start2 = int(lots[2])
	end2 = int(lots[3])
	
	#sets would be easier to write, but I think this performs better.
	is_start1_in_lot2 = start1 >= start2 and start1 <= end2
	is_end1_in_lot2 = end1 >= start2 and end1 <= end2
	is_start2_in_lot1 = start2 >= start1 and start2 <= end1
	is_end2_in_lot1 = end2 >= start1 and end2 <= end1

	is_overlap = is_start1_in_lot2 or is_end1_in_lot2 or is_start2_in_lot1 or is_end2_in_lot1

	if is_overlap:
		overlap_count += 1

print overlap_count 

