s="1 box has 3 blue 4 red 6 green and 12 yellow marbles"
temp = 0
value = ''
for i in s:

    if i.isnumeric():   

        if int(i) > temp:
            temp = int(i)
            value = 'true'
        else:
            value = 'false'
print(value)

