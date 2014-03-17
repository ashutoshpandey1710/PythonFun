class Queue:
	def __init__(self):
		self.q = []
	
	def enqueue(self, item):
		self.q = [item] + self.q
	def empty(self):
		return (len(self.q) <= 0)
	def dequeue(self):
		item = self.q[-1]
		self.q = self.q[:-1]
		return item

def getTree(inorder, preorder):
	if (inorder == []) or (preorder == []):
		return None
	root = preorder[0]
	# print inorder, preorder
	rootIndex = inorder.index(root)
	tree = [root, getTree(inorder[:rootIndex], preorder[1:rootIndex + 1]), getTree(inorder[rootIndex + 1:], preorder[rootIndex + 1:])]
	return tree

def bfs_order(tree):
	q = Queue()
	q.enqueue(tree)
	while not q.empty():
		print q.q
		raw_input()
		top = q.dequeue()
		print q.q
		print
		print "------------------------------"
		print
		if top:
			q.enqueue(tree[1])
			q.enqueue(tree[2])
			# print top
		
def readTreeFromFile(filename):
	desc = open(filename, 'r').read().split('\n')
	inorder, preorder = desc[0].split(), desc[1].split()
	return getTree(inorder, preorder)

if __name__ == '__main__':
	tree = readTreeFromFile('datafile.txt')
	bfs_order(tree)
	# for node in bfs_order(tree)
	