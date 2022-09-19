

import time
start_time = time.time()

import math

cocacola_numbers= int(input(''))
total_cans_you_can_drink = cocacola_numbers
empty_cans_offer = 3
if (cocacola_numbers % 3) == 0 :
    result = (cocacola_numbers / 3)

elif (cocacola_numbers % 3) != 0 :

    result = (cocacola_numbers / 3)
    #print('not three',result)

    floor_result = math.floor(result)
    
    ceil_result = math.ceil(result)
   
    print ('NOT DIVISIBLE BY THREE So You Have To Borrow','Result:',result,'Floor:',floor_result,'Ceil:',ceil_result)

    if (floor_result % 3) == 0 :
        floor_divide_result =  floor_result / 3
        total_cans_you_can_drink = total_cans_you_can_drink + int(floor_divide_result)
        #print(floor_divide_result)
        

    elif (ceil_result % 3) == 0:
        ceil_divide_result =  ceil_result / 3
        total_cans_you_can_drink = total_cans_you_can_drink + int(ceil_divide_result)
        #print(ceil_divide_result)

    else:
        print("error")
        
   

   

else:
    print("error")

total_cans_you_can_drink= total_cans_you_can_drink  + empty_cans_offer / 3 #empty bollte numbers
print((f'{int(total_cans_you_can_drink)}'))


print("Process finished --- %s seconds ---" % (time.time() - start_time))