a = input('enter elements: ').split(' ')

print(a)
temp=0
for j in range(len(a)):
    for i in range(len(a)):
        if i == 0 :
            if a[i] < a[i+1]:
                a[i] = a[i]
        else:
            while (a[i] < a[i-1]):
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                temp = 0
print(a)
