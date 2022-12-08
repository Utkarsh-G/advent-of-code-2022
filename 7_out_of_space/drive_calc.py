import sys

dir = [] #

class Node:
	def __init__(self, name):
		self.name = name
		self.size = 0
		self.children = []
		self.parent = None

root_node = Node("/")
temp_parent_node = root_node

with open(sys.argv[1], 'r') as f:
	line = f.readline()
	line = f.readline()
	while line:
		parsed_line = line.strip().split(" ")
		if parsed_line[0]=="$" and parsed_line[1] == "cd" and parsed_line[2] != "..":
			temp_parent_node = [x for x in temp_parent_node.children if x.name == parsed_line[2]][0]
		if parsed_line[0]=="$" and parsed_line[1] == "cd" and parsed_line[2] == "..":
			temp_parent_node = temp_parent_node.parent
			sizes = [x.size for x in temp_parent_node.children]
			sum = 0
			for num in sizes:
				sum += num
			temp_parent_node.size += sum
			print(f"Node: {temp_parent_node.name} size: {temp_parent_node.size}")
		elif parsed_line[0]=="$" and parsed_line[1] == "ls":
			print(f"Showing ls of {temp_parent_node.name}")
		elif parsed_line[0] != "$":
			if parsed_line[0] == "dir":
				node = Node(parsed_line[1])
				node.parent = temp_parent_node
				temp_parent_node.children.append(node)
				print(f"Directory name: {node.name}")
			else:
				node = Node(parsed_line[1])
				node.size = int(parsed_line[0])
				node.parent = temp_parent_node
				temp_parent_node.children.append(node)
				print(f"Leaf name: {node.name} size: {node.size}")
		line = f.readline()

while temp_parent_node.name != "/":
	temp_parent_node = temp_parent_node.parent
	sizes = [x.size for x in temp_parent_node.children]
	sum = 0
	for num in sizes:
		sum += num
	temp_parent_node.size += sum
	print(f"Node: {temp_parent_node.name} size: {temp_parent_node.size}")

