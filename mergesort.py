
def mergesort(a):
    left = []
    right = []
    n = len(a)
    if n > 1:
        mid = int(n/2)
        
        for i in range(mid):
            left.append(a[i])

        for i in range(mid,n):
            right.append(a[i])
        
        #recursion
        mergesort(left)
        mergesort(right)

        #merge
        i=0
        k=0
        j=0
        len_left = len(left)
        len_right = len(right)
        
        while ( i < len_left) and (j < len_right ):

            if left[i] <= right [j]:
                a[k] = left [i]
                i +=1
            elif left[i] > right[j]:
                a[k] = right[j]
                j +=1
            k+=1

        while(i < len_left):
            a[k] = left [i]
            k +=1
            i +=1


        while(j < len_right):
            a[k] = right[j]
            k +=1
            j +=1
        

a = (input('Enter elements: ').split(' '))

mergesort(a)

print(a)

#complexity o(nlogn)