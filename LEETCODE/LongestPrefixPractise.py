s = ['flower','flo','fle','flew','flown']

longest = s[0]

print(type(longest))
common =''
for i in range (1,len(s)):
    
    for j in range(0,len(s[0])):

        if s[0][j] == s[i][j] and j < len(s[i]):
            common = common + s[0][j]
        else:
            longest = common
            break
print(longest)



        
    
