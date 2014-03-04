import re
def flattenList(l):
		flatlist = []
		for item in l:
			if type(item) is list:
				flatlist.extend(flattenList(item))
			else:
				flatlist.append(item)
		return flatlist

if __name__ == '__main__':
	print flattenList([1, 2, [3, 4, [7, 8]], 23, 2])
	l = eval('[' + re.sub(r'[\[\]]', '', str([1, 2, [3, 4, [7, 8]], 23, 2])) + ']')
	
	print l
	