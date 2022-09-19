import string #for alphabet list

file1 = open("input.txt","r")
readfile1= file1.read()
file1.close()

print(readfile1)

alphabet_string = string.ascii_uppercase
print(alphabet_string)
for i in range(len(readfile1)):
    print(readfile1[i])
  






# file2 = open("output.txt","a")
# file2.write(readfile1)
# file2.close()


