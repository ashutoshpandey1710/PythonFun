from tree import readTreeFromFile

def getNumbers(tree, numbers=''):
	if not tree:
		return []
	elif (not tree[1]) and (not tree[2]):
		return [numbers + tree[0]]
	else:
		return getNumbers(tree[1], numbers + tree[0]) + getNumbers(tree[2], numbers + tree[0])

if __name__ == '__main__':
	tree = readTreeFromFile('unbalanced.txt')
	# print get_path_from_root(tree, 'x', [])
	print getNumbers(tree)