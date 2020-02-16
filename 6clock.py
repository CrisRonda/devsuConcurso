def angulo(hour, minute): 
    resp = hour*30 + minute*0.5 - minute*6
    if(hour*30 + minute*0.5 >  minute*6 ):
        return abs(360-resp)
    return abs(resp)
def angles(times):
    resultado= 0
    for time in times:
        separacion= time.split(":",2)
        if separacion[0].isdigit() and separacion[0].isdigit() :
            hora=int(separacion[0])
            minutos=int(separacion[1])
            if 12<=hora<=23:
                hora-=12
                resultado+=(angulo(hora,minutos))
            else:
                resultado-=100
        else:
            resultado-=100
    return resultado