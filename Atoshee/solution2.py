
Key = 'the quick brown fox jumps over the lazy dog'
KeyEx = Key.replace(" ", "")
msgEx ='vkbs bs t suepuv'
dict_store = {} #dictionary


j=0
for i in range(0,len(KeyEx)):
    if KeyEx[i] not in dict_store:
        dict_store[KeyEx[i]] = chr(97 + j) #ascii key add
        j +=1

print(dict_store)

decoded_msg = ''

for i in msgEx:
    if i.isalpha():
        decoded_msg = decoded_msg + dict_store[i]
    if i == ' ': #add space in the result
        decoded_msg = decoded_msg + ' '
print(decoded_msg)
    