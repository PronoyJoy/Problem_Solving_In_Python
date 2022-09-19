a = input('enter elements: ').split(' ')

print(a)
temp = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)


#right minimum swap by current element o(n^2)

