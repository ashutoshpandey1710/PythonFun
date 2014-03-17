from tree import readTreeFromFile


def get_path_from_root(tree, key, current_path=[]):
	if not tree:
		return None
	if tree[0] == key:
		return (current_path + [tree[0]])
	else:
		return (get_path_from_root(tree[1], key, current_path + [tree[0]]) or get_path_from_root(tree[2], key, current_path + [tree[0]]))

def shortest_path(tree, key1, key2):
	path1 = get_path_from_root(tree, key1)
	path2 = get_path_from_root(tree, key2)

	if (not path1) or (not path2):
		return None
	
	lca = 0
	for i in range(len(path2)):
		if path2[i] in path1:
			lca = i
	return path1[lca + 1:], path2[lca:]
	
	
if __name__ == '__main__':
	tree = readTreeFromFile('datafile.txt')
	# print get_path_from_root(tree, 'x', [])
	print shortest_path(tree, 'e', 'd')
	