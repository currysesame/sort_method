
import numpy as np

arr1 = np.array([22,-15,55,36,23,67,755,324,23,75,24,878,6,235,222, -23, -322])

#merge sort

print('The array length is ', len(arr1))
tree_height = np.int(np.ceil(np.log2(len(arr1))))
print('The tree height is 'tree_height)

print(arr1)
for j in range(tree_height):
	sublength = 2**(j+1)
	half_length = sublength // 2
	for i in range(len(arr1) // sublength +1):
		sorted1 = arr1[sublength*i: sublength*i+half_length]
		sorted2 = arr1[sublength*i+half_length:sublength*(i+1)]
		length1 = len(sorted1)
		length2 = len(sorted2)
		subresult = np.zeros((length1 + length2))
		count = 0
		while((length1 > 0 ) and (length2 > 0)):
			if((sorted1[0] > sorted2[0])):
				if(length2 > 1):
					subresult[count] = sorted2[0]
					sorted2 = sorted2[1:]
				else:
					subresult[count] = sorted2[0]
					subresult[count+1:] = sorted1
					arr1[sublength*i:sublength*(i+1)] = subresult
					break
			else:
				if(length1 > 1):
					subresult[count] = sorted1[0]
					sorted1 = sorted1[1:]
				else:
					subresult[count] = sorted1[0]
					subresult[count+1:] = sorted2
					arr1[sublength*i:sublength*(i+1)] = subresult
					break
			length1 = len(sorted1)
			length2 = len(sorted2)
			count += 1
	print(arr1)
