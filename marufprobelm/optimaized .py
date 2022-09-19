

#import timeit

#start = timeit.default_timer()

#Your statements here



N = int(input())

totalempty__cans = 0

if ( N % 3 == 0 ):
    totalempty__cans  = N/(N/3) + N
    print(int(totalempty__cans))
    exit()

else:
    if ((N+1) % 3) == 0 :
        totalempty__cans = N + 1  + (N+1)/3   
    if ((N-1) % 3) == 0 :
        totalempty__cans = N + 1 + (N-1)/3
     
print(int(totalempty__cans))


#stop = timeit.default_timer()

#print('Time: ', stop - start)  
