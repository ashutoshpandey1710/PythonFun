from tree import readTreeFromFile

def leafHeight(tree, height=1):
	if (not tree[1]) and (not tree[2]):
		return set([height])
	leftset = set()
	if tree[1]:
		leftset= leafHeight(tree[1], height + 1)

	rightset = set()
	if tree[2]:
		rightset = leafHeight(tree[2], height + 1)
	return leftset.union(rightset)
	
if __name__ == '__main__':
	tree = readTreeFromFile('unbalanced.txt')
	print leafHeight(tree)	