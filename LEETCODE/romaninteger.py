s = input('Enter:')

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
result = 0 


#SMALLER BEFORE
if s[0] == 'I' and s[1] == 'V':
    result = 5 - 1
  
if s[0] == 'I' and s[1] == 'X':
    result = 10 - 1
  
if s[0] == 'X' and s[1] == 'C':
    result = 100 - 10
  
if s[0] == 'X' and s[1] == 'L':
    result = 50 - 10
  
if s[0] == 'C' and s[1] == 'D':
    result = 500 - 100
  
if s[0] == 'C' and s[1] == 'M':
    result = 1000 - 100
  
#SMALLER BEFORE

#SUM

if s[0] == 'I' and s[1]== 'I':
    result = 1
    for i in range(1, len(s)):
        result = result + 1


if s[0] == 'V':
    result = 5
    for i in range(1, len(s)):
        result = result + 1


if s[0] == 'X':
    result = 10 
    for i in range(1, len(s)):
        if s[i] == 'V':
            result = result + 5
        else:
            result = result + 1




if s[0] == 'L':
    result = 50
    for i in range(1, len(s)):
        if s[i] == 'V':
            result = result + 5
        elif s[i] == 'X':
            result = result + 10
        else:
            result = result + 1



if s[0] == 'C':
    result = 100
    for i in range(1, len(s)):
        if s[i] == 'V':
            result = result + 5
        elif s[i] == 'X':
            result = result + 10
        elif s[i] == 'L':
            result = result + 50
        else:
            result = result + 1


if s[0] == 'D':
    result = 500
    for i in range(1, len(s)):
        if s[i] == 'V':
            result = result + 5
        elif s[i] == 'X':
            result = result + 10
        elif s[i] == 'L':
            result = result + 50
        elif s[i] == 'C':
            result = result + 100
        else:
            result = result + 1


if s[0] == 'M':
    result = 1000
    for i in range(1, len(s)):
        if s[i] == 'V':
            result = result + 5
        elif s[i] == 'X':
            result = result + 10
        elif s[i] == 'L':
            result = result + 50
        elif s[i] == 'C':
            result = result + 100
        elif s[i] == 'D':
            result = result + 500
        elif s[i] == 'M':
            result = result + 1000
        else:
            result = result + 1



print(result)