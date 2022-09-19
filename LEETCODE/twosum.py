nums =list(map(int, input('Enter List:').split()))

target = int(input('Enter Target:'))

new_list=[]

for i,value in enumerate(nums):
    for j in range(i+1,len(nums)):
       if (value + nums[j]) == target :
           new_list.extend((i,j))
           break
print(new_list)