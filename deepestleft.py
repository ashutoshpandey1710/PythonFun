from tree import readTreeFromFile
def deepestLeft(tree, level=1, isleft=False):
	if (not tree[1]) and (not tree[2]):
		if isleft:
			return level, tree[0]
		else:
			return -1, None

	leftmax, leftnode = -1, None
	if tree[1]:
		leftmax, leftnode = deepestLeft(tree[1], level + 1, True)

	rightmax, rightnode = -1, None
	if tree[2]:
		rightmax, rightnode = deepestLeft(tree[2], level + 1, False)
		
	if leftmax >= rightmax:
		return leftmax, leftnode
	else:
		return rightmax, rightnode
	
	
		

if __name__ == '__main__':
	tree = readTreeFromFile('unbalanced.txt')
	print deepestLeft(tree)	