def decrypt(key, message):
    if key == '':
        key = 'DJC'
    
    if not key:
        message = ''
        return(message)
    
    else :
        message = message.replace(key+'a','a')
        message = message.replace(key+'e','e')
        message = message.replace(key+'i','i')
        message = message.replace(key+'o','o')
        message = message.replace(key+'u','u')
        message = message.replace(key+'A','A')
        message = message.replace(key+'E','E')
        message = message.replace(key+'I','I')
        message = message.replace(key+'O','O')
        message = message.replace(key+'U','U')
        return message
