

def DecimalToBinary(num):
    return bin(num).replace('0b','')

n = int(input('Enter the number of elements:'))

array = list( map( int, input('enter numbers:').strip().split()))


new_array =[]
for i in array:
   new_array.append(DecimalToBinary(i).zfill(8))

print(new_array)
list_1 =[]
count =0
for i in new_array:
    
    for j in i:
        
        if j == '1':
            count = count + 1
        else:
            break
    list_1.append(count)
    count = 0
print(list_1)
value = 1
#check pattern
if len(list_1) > 1:
            
    for i in range(len(list_1)):
        if (list_1[i]) > 1:
            for j in range(i,i+list_1[i]):
                if list_1[j] < 1 :
                    value = 0
                    break
elif len(list_1) == 1:
    if list_1[0] == 0:
        value = 1
    else:
        value = 0

else: 
    value = 0

if value == 1:
    print('true')
elif value == 0:
    print('false')



    