__Author__ = "Panda-J"

# def bin_search(li,val):
# 	low=0
# 	high = len(li)-1
# 	while low<=high:
# 		print(1)
# 		mid =(low+high)//2
# 		if li[mid]==val:
# 			left=mid-1
# 			right=mid+1
# 			while left>=0 and li[left]==val:
# 				left -=1
# 			while right <=len(li)-1 and li[right]==val:
# 				right +=1
# 			return (left+1,right-1)
# 		elif li[mid]<val:
# 			low = mid +1
# 		else:
# 			high = mid-1
# 	return
#
# li=[1,2,2,2,3,3,5,6,7,9]
# print(bin_search(li,1))
#

def sum_down(li,num):
	for i in range(0,len(li)-1):
		for j in range(i+1,len(li)-1):
			if li[i]+li[j]==num:
				return (i,j)



list=[1,2,3,5,7,9]
print(sum_down(list,5))

def bin_search(li,target):
	low=0
	high=len(li)-1
	while low<=high:
		mid = (low+high)//2
		if li[mid] == target:
			return mid
		elif li[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
def func2(li,target):
	for i in li:
		target_bin = target - i
		b=bin_search(li,target_bin)
		if b:
			return (li.index(i), b)
	else:
		print('cannot found')
print(func2(list,5))
