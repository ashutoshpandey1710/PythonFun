from tree import readTreeFromFile


def deepestOdd(tree, level=1):
	if (not tree[1]) and (not tree[2]):
		if level % 2 == 1:
			return level, tree[0]
		else:
			return -1, None

	leftmax, leftnode = -1, None
	if tree[1]:
		leftmax, leftnode = deepestOdd(tree[1], level + 1)

	rightmax, rightnode = -1, None
	if tree[2]:
		rightmax, rightnode = deepestOdd(tree[2], level + 1)
		
	if leftmax >= rightmax:
		return leftmax, leftnode
	else:
		return rightmax, rightnode
		
if __name__ == '__main__':
	tree = readTreeFromFile('unbalanced.txt')
	print deepestOdd(tree)	