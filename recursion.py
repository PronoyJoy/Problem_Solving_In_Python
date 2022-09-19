#1

""" result = 0

def sum(n):
    n = n
    print(n)
    global result
    result = result + n
    print(result)
    if (n < 9) :
        print(f'for {n+1}- {result} okay')
        sum(n+1)
    else:
        print('Bigger than 10')

    return result

sum(0) """

#2 0 1=[ result + secondnumber- 1 ] 2 3 5 8

""" result = 0
def fibonacci(number_one,number_two):
    global result
    result = number_one + number_two
    print(result)
    if (result < 20):
        fibonacci(number_two,result)
    else:
        print('stop')
  

fibonacci(0,1) """
    
""" 
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

for i in range(0,10):
    print(fibo(i)) """


#3. reverse a string

def reverse_string(string,n):

    l =len(string)
    print(string[-n],end='')

    if n < l:
        reverse_string(string,n+1)

reverse_string('hello',1)
