


while(True):

    cola = int(input ('Enter the number of cola you have:'))
    extracola = 1
    result = 0
    d=0

    
    if (cola % 3 ) != 0 :
        
        top = cola + extracola #borrowed
        down = cola - extracola #remain
        if (down %3 ) == 0:
            result =  cola + (down/3) + extracola
        if (top %3 ) == 0:
            result =  cola + (top/3) + extracola
        

    elif(cola % 3 ) == 0 :
        
        divide = cola / 3
        top = divide + extracola #borrowed
        down = divide - extracola #remain

        if (down %3 ) == 0:
            result =  cola + divide + (down/3) + extracola
        if (top %3 ) == 0:
            result =  cola + divide +  (top/3) + extracola

        
        
    print(int(result))
