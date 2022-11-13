
s = 'PALLAPLLPL'
count = []
for i in range(len(s)):
  if s[i] == 'L':
    count.append('1')
    if i+1 <  len(s) and s[i+1] == 'L':
      count.append('1')
     
      if i+2 <  len(s) and s[i+2] == 'L':
        count.append('1')
        print(True)
      else:
        print('no 3')
count =0
print(count)


    

    




   