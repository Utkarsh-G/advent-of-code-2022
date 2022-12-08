import sys
import copy

dir = [] #

class Node:
	def __init__(self, name):
		self.name = name
		self.size = 0
		self.children = []
		self.parent = None

root_node = Node("/")
temp_parent_node = root_node

def propagate_sizes(node, prop_size):
	is_root = node.name == "/"
	if not is_root:
		parent_node = node.parent
		parent_node.size += prop_size
		print(f"prop parent {parent_node.name} : {parent_node.size}")
		propagate_sizes(parent_node, prop_size)
	else:
		print(f"prop / : {node.size}")
		return


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
			#temp_parent_node.size += sum
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
				propagate_sizes(node, node.size)
		line = f.readline()

is_not_root = True

while is_not_root: 
	temp_parent_node = temp_parent_node.parent
	print(f"Node: {temp_parent_node.name} size: {temp_parent_node.size}")
	is_not_root = temp_parent_node.name != "/"

sum_of_dirs = 0

def traverse_tree(node, dir_array):
	if len(node.children) > 0:
		print(f"dir size: {node.size} cur sum:{dir_array}")
		this_array = copy.deepcopy(dir_array)
		for n in node.children:
			print(f"before for {dir_array}")
			dir_array += traverse_tree(n, this_array)
			print(f"after for {dir_array}")
		dir_array += [node.size] if node.size >= (30000000-(70000000-root_node.size)) else []
		print(f"{node.name} : {node.size} sum: {dir_array}")
		return dir_array
	else:
		return []

def t_tree2(node, dir_array):
	if len(node.children) > 0:
		for n in node.children:
			t_tree2(n, dir_array)
		dir_array += [node.size] if node.size >= (30000000-(70000000-root_node.size)) else []
		return
	else:
		return

my_arr = []
t_tree2(root_node, my_arr)
print("final dirs:")
print (my_arr)
print(f"min spaces needed: {30000000 - root_node.size}")
print(f"dir takes up: {root_node.size}")
#my_arr.sort()
#print(my_arr[0])
print(min(my_arr))
