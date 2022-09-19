array = (input('Enter elements: ').split(' '))
temp = 0
print(array)
for j in range(len(array)):
    for i in range(len(array)-1):
        if array[i] > array [i+1] :
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            temp = 0
            
print(array)


#complexity (n-1)*(n-1)*c = O(n^2)