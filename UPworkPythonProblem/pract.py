import os,string
alp = list(string.ascii_uppercase)



def encrypt(alpchar,encodechar):
    alpchar = alpchar
    encodechar = encodechar
    difference = ord(alpchar) - ord(encodechar) 

    print(alpchar,encodechar,difference)


encode = input().upper()
encode = list(encode)
print(encode)

for i in range(len(encode)):
    alp[i] = encrypt(alp[i],encode[i])





