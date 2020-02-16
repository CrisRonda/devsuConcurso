def nthCase(n, message):
    contador_letra=1
    message_edit= ""
    if n<=0:
        return message
    if not message:
        return ""
    else:
        for letra in message:
            if contador_letra==n:
                if 'a'<=letra<='z':
                    message_edit+=letra.upper()
                else:
                    message_edit+=letra.lower()
                contador_letra=1
            else:
                message_edit+=letra
                contador_letra+=1
    return message_edit
  