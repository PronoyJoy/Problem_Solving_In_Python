

string ='ABCDCDC'
sub_string = 'CDC'
counter = 0
for i in range(len(string)):
    if (string[i:]).startswith(sub_string):
        counter +=1


print(counter)

            

        


    


