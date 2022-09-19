
string=input('enter string:')
string_rev = string[::-1]

count =0
if len(string) == len(string_rev):

    for i in range(len(string)):
        if (string[i].lower() == string_rev[i].lower()) :
            count = count + 1
        else:
            print('Not same letter palindrome')
            break       
    if count == len(string):
        print('They are palindrome')
    

else:
    print('len not equal')
