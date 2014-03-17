def kthsmallest(arr1, arr2, k):
	ksm = []
	kcount = 0
	while (len(ksm) < k) and (len(arr1) > 0) and (len(arr2) > 0):
		top1 = arr1[0]
		arr1 = arr1[1:]
		
		top2 = arr2[0]
		arr2 = arr2[1:]
		
		if top1 < top2:
			ksm.append(top1)
			arr2 = [top2] + arr2
		elif top1 == top2:
			ksm.append(top1)
		else:
			ksm.append(top2)
			arr1 = [top1] + arr1
		
		if len(arr1) == 0:
			while (len(ksm) < k) and (len(arr2) > 0):
				ksm.append(arr2[0])
				arr2 = arr2[1:]
		elif len(arr2) == 0:
			while (len(ksm) < k) and (len(arr1) > 0):
				ksm.append(arr1[0])
				arr1 = arr1[1:]
		else:
			pass
				
	return ksm

if __name__ == '__main__':
	print kthsmallest([1, 8, 10, 12], [2, 4, 9, 10], 12)