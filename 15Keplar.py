def recursiva(n,contador):
    constante= "6174"
    if constante==n:
        return contador
    else:
        array_numeros=[]
        respuesta=0
        for numero in n:
            array_numeros.append((numero))
        array_asc=sorted(array_numeros)
        menor= int("".join(array_asc))
        array_des=array_asc[::-1]
        mayor= int("".join(array_des))
        new_n= str(mayor-menor)
        contador+=1
        return recursiva((new_n),contador)
    
def kaprekar(n):
   return recursiva(n,0)