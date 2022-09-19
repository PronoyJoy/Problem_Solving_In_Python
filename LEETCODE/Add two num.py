l1 = [2,4,3]
l2 = [5,6,4]
l1.reverse()
l2.reverse()
sum=0
str1 =''
str2=''

listToStr1 = (''.join(map(str, l1))).strip()
listToStr2 = (''.join(map(str, l2))).strip()
print(listToStr1,listToStr2)
sum = int(listToStr1) + int(listToStr2)
sum = list(str(sum))
sum.reverse()
print(sum)

