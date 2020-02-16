def subString(cadena):
    if not cadena:
        return 0
    longitud_cadena=len(cadena)//2
    index_cadena={}
    for index in range(longitud_cadena):
        caracter= cadena[index]
        if cadena.count(caracter)>1:
            menor= cadena.find(caracter)
            mayor= cadena.rindex(caracter)
            longitud= mayor -menor
            index_cadena[longitud]=[menor,mayor]
    ordenado = sorted(index_cadena.items())[::-1]
    index_bajo=ordenado[0][1][0]+1
    index_alto=ordenado[0][1][1]
    return cadena[index_bajo:index_alto]
   
    