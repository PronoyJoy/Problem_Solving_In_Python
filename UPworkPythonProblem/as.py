import os,string
alp = list(string.ascii_uppercase)
# alp2= list(string.ascii_uppercase)

# #for first character
# for i in range(len(alp)):
    
#     if ord(alp[i]) >= 65 and ord(alp[i]) < 65+7:
#         alp[i] = chr(ord(alp[i]) + 19)

#     elif ord(alp[i]) >= 65+7 and ord(alp[i]) < (65+(7*2)):
#         alp[i] = chr( ord(alp[i]) - 7)

#     elif ord(alp[i]) >= 65+(7*2) and ord(alp[i]) < (65+(7*3)):
#         alp[i] = chr( ord(alp[i]) - 7)

#     elif ord(alp[i]) >= 65+(7*3) and ord(alp[i]) <= (65+(7*4)-3)  :
#         alp[i] = chr( ord(alp[i]) - 7)

#     else:
#         print('special char not included')
# print('first char:',alp)


#for second character
# for i in range(len(alp)):
    
#     if ord(alp[i]) >= 65 and ord(alp[i]) < 65+7:
#         alp[i] = chr(ord(alp[i]) + 8)

#     elif ord(alp[i]) >= 65+7 and ord(alp[i]) < (65+(7*2)):
#         alp[i] = chr( ord(alp[i]) + 8)

#     elif ord(alp[i]) >= 65+(7*2) and ord(alp[i]) < (65+(7*3)-3):
#         alp[i] = chr( ord(alp[i]) + 8 )

#     elif ord(alp[i]) >= 65+(7*3)-3 and ord(alp[i]) <= (65+(7*4)-3)  :
#         alp[i] = chr( ord(alp[i]) -18 )

#     else:
#         print('special char not included')


# print('second char',alp)


#for third
for i in range(len(alp)):
    
    if ord(alp[i]) >= 65 and ord(alp[i]) < 65+7:
        alp[i] = chr(ord(alp[i]) + 6)

    elif ord(alp[i]) >= 65+7 and ord(alp[i]) < (65+(7*2)):
        alp[i] = chr( ord(alp[i]) + 6)

    elif ord(alp[i]) >= 65+(7*2) and ord(alp[i]) < (65+(7*3))-1:
        alp[i] = chr( ord(alp[i]) + 6 )

    elif ord(alp[i]) >= 65+(7*3)-1 and ord(alp[i]) <= (65+(7*4)-3)  :
        alp[i] = chr( ord(alp[i]) - 20 )

    else:
        print('special char not included')


print('third char',alp)




    