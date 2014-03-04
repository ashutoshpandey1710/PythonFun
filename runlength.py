def runLength(st):
	final = st[0]
	prev = st[0]
	current_runlength = 1
	for char in st[1:]:
		if char == prev:
			current_runlength += 1
		else:
			if current_runlength > 1:
				final += str(current_runlength) + char 
			else:
				final += char
			current_runlength = 1
		prev = char
	#final += st[-1]
	if current_runlength > 1:
		final += str(current_runlength)
	return final



if __name__ == '__main__':
	print runLength("fuuuuuuuuckaaaaaaa")