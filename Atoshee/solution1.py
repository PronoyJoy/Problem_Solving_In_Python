s = "Myself2 Me1 I4 and3"


# for i in space_removed:
#     for j in i:
#         if j.isnumeric():
#             index = int(j)
#             print(index)
#             store.insert(index-1, i)

space_removed = s.split()
storage_dictionary = {}

for i in space_removed:
   
    storage_dictionary[i[-1]] = i[:-1]

ret =''
storage_dictionary = dict(sorted(storage_dictionary.items()))

for i in storage_dictionary:
    ret = ret + storage_dictionary[i]
    ret = ret + ' '

print(ret)



            


