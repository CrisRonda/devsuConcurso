def track(array_milisegundos):
    tiempo_fin=0
    respuesta=[]
    dias=''
    horas=''
    minutos=''
    segundos=''
    milisegundos=''

    if(array_milisegundos):
        array_milisegundos=array_milisegundos
    else:
        array_milisegundos=[0]

    for tiempo in array_milisegundos:

        if tiempo <0 :
            tiempo=0
        tiempo_fin+=tiempo


    dias=tiempo_fin//(86400000)

    horas_aux=dias*24
    horas=(tiempo_fin//(3600000))-horas_aux

    minutos_aux=(dias*24*60)+(horas*60)
    minutos=(tiempo_fin//(60000))- minutos_aux

    segundos_aux=(dias*24*60*60)+(horas*60*60)+(minutos*60)
    segundos=(tiempo_fin//(1000))-segundos_aux

    milisegundos_aux=(dias*24*60*60*1000)+(horas*60*60*1000)+(minutos*60*1000)+(segundos*1000)
    milisegundos=tiempo_fin-milisegundos_aux

    respuesta=[dias, horas, minutos, segundos, milisegundos]
    return respuesta
