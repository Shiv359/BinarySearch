def BinarySearch(list1,n):
	low=0
	high=len(list1)-1
	mid=0
	while low<=high:
		mid=(high+low)//2
		if list1[mid]<n:
			low=mid+1
		elif list1[mid]>n:
			high=mid-1
		else:
			return mid
	return -1

list1=[23,8,90,43,98,342,1,0,78]
list1.sort()
n=342
result=BinarySearch(list1,n)
if result==-1:
	print("element not found")
else:
	print("element is present at index",result)