#lautaro sucur
#tema:c
#division:105



#UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva franquicia que se insertará en el mercado argentino y en la cual invertirán. Las posibles franquicias son las siguientes: Apple, Dunkin o Ikea.
#Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles son los gustos de los encuestados (no se sabe cuántos):
#Se ingresa de cada encuestado:
#nombre
#edad (no menor a 18)
#está empleado (si-no)
#género (Masculino - Femenino - Otro)
#voto (APPLE, DUNKIN, IKEA)
#Se necesita saber:
#1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.
#4. Edad promedio de los encuestados que están o no empleados (de cada uno).
#5. Determinar cuál fue la franquicia más votada.
contador_votos_masculinos=0
bandera_masculino=0
edad_masculino=0
contador_votos_apple=0
contador_votos_ikea=0
contador_votos_dunkin=0
franquicia_mas_votada=""
primer_voto_apple=0
voto_ikea_femenino_mayor_25=0
porcentaje_femenino=0
total_votos=0
seguir="si"

while seguir=="si":
    nombre_del_encuestado=input("ingrese su nombre: ")

    edad_ingresada=int(input("ingrese su edad: "))
    while edad_ingresada<18:
        edad_ingresada= int(input("ingrese su edad: "))

    sitaucion_laboral=input("tiene empleo si-no: ")
    while sitaucion_laboral!="si" and sitaucion_laboral!="no":
        
        genero_ingresado=input("ingrese su genero(masculino-femenino-otro: )")
    while genero_ingresado!="masculino" and genero_ingresado!="femenino" and genero_ingresado !="otro":
        genero_ingresado=input("reingrese su genero(masculino-femenino-otro: )")

    voto_ingresado=input("ingrese su voto (apple-dunkin-ikea): ")
    while voto_ingresado!="apple" and voto_ingresado!="dunkin" and voto_ingresado!="ikea":
        voto_ingresado=input("reingrese su voto (apple-dunkin-ikea): ")
#1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.

    
    match genero_ingresado:
        case "masculino":
        
            if edad_ingresada >18 and edad_ingresada <25:
                contador_votos_masculinos+=1
            elif edad_ingresada >36 and edad_ingresada <49:
                contador_votos_masculinos+=1
            elif voto_ingresado=="ikea":
                contador_votos_masculinos+=1
        
        case "femenino":
            if voto_ingresado=="ikea":
                if edad_ingresada>25:
                    voto_ikea_femenino_mayor_25+=1

            porcentaje_femenino=(voto_ikea_femenino_mayor_25/total_votos)*100



    match sitaucion_laboral:
        case "si":
            if genero_ingresado=="masculino":
                


    #seguir=input("quiere seguir si-no: ")



#5. Determinar cuál fue la franquicia más votada.

#if contador_votos_apple>contador_votos_dunkin and contador_votos_apple>contador_votos_ikea:
    #franquicia_mas_votada="apple"
#elif contador_votos_dunkin>contador_votos_apple and contador_votos_dunkin>contador_votos_ikea:
        #franquicia_mas_votada="dunkin"
#else:
    #franquicia_mas_votada="ikea"