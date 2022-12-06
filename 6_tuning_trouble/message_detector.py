import sys

ds_buffer = sys.argv[1]
window = []
unique_set = set()
index = 0

for char in ds_buffer:
	index += 1
	if index < 15:
		window.append(char)
	else:
		window = window[1:]+[char]
		unique_set = set(window)
	if len(unique_set) == 14:
		print "Found solution"
		print unique_set
		print index
		break	

