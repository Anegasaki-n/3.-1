nums = list(map(int,input().strip('[]').split(',')))
target = int(input)

#   适用于无序列表
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
                return [i,j]

'''  适用于有序列表
for i in range(len(nums)):
	if nums[i] > target/2:
		temp1.append(nums[i])
	else:
		temp2.append(nums[i])

for i in range(len(temp1)):
	for j in range(len(temp2)):
		if temp1[i] + temp2[j] == target:
			print([j,i+j+1])
'''
