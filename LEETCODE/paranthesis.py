list_1  = [4,1,1,1,1]

for i in range(len(list_1)):
    num = 0
    if (list_1[i]) > 1:
        num = list_1[i]
        for j in range(i,i+list_1[i]):
            if list_1[j] < 1:
               print('false')
    if i == (i + num +1) and list_1[i] == '1':
        print('false')
        

    
               

    
    
    
    
    

