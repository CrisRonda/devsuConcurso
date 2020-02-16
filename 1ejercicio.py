def encrypt(key, message):
    if not message=="null":
        if key:
            pass
        else:
            key="DJC"
    else:
        return ""
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    codificado=""
    for caracter in message:
        if (caracter in vocales):
            codificado+=key+caracter
        else: 
            codificado+=caracter
    return codificado
