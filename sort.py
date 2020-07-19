
#insert sort

import numpy as np

arr1 = np.array([233,646,242,6,24,7,234,-323,66,-24,23,2,18,122,233,34,11])

print(arr1)

def switch(array_, x, y):
	if(x < (len(array_)) and y < (len(array_))):
		buffer1 = array_[x]
		array_[x] = array_[y]
		array_[y] = buffer1
	return array_

for i in range(len(arr1) -1):
	for j in range(i+1):
		if(arr1[i-j+1] < arr1[i-j]):
			arr1 = switch(arr1, i-j+1, i-j)
		else:
			break


print(arr1)

