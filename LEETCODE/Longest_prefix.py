strs = ['flowne','flew','flower','flow','flower']

# if i == '':
#     print('Faka')
# else:
value = strs[0]

if len(strs)<2:
    print(value)
else:
    new = ''
    
    k=0

    for m in range(1,len(strs)):
        j=0
        for k in strs[m]:
            if value[j] == k:
                print('matched',value[j])
                new = new + value[j]
                j+=1
            else:
                print('False',k,'and',value[j],'so break')
                break
        value = new

        print('str : ',new)

        #value = new
        #print('assigining new to value: ',value)
        print('\n')


            
                    







