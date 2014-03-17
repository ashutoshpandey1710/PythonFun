from tree import readTreeFromFile

def getLevelK(tree, k):
	if (not tree) or (k < 1):
		return []
	if k == 1:
		return [tree[0]]
	else:
		return getLevelK(tree[1], k - 1) + getLevelK(tree[2], k - 1)
	
		

if __name__ == '__main__':
	tree = readTreeFromFile('datafile.txt')
	print getLevelK(tree, 2)