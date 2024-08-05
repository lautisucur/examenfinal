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

contador_votos_masculinos = 0
bandera_masculino=0
bandera_votos_apple = 0
edad_encuestado_menor_edad_apple = 999
nombre_encuestado_menor_edad_apple = ""
genero_encuestado_menor_edad_apple = ""
contador_votos_apple= 0
contador_votos_ikea= 0
contador_votos_dunkin= 0
franquicia_mas_votada= ""
primer_voto_apple=0
contador_votos_femenino = 0
contador_votos_femeninos_mayor = 0
porcentaje_femenino=0
total_votos=0
total_edad_empleados = 0
total_empleados = 0
total_edad_no_empleados = 0
total_no_empleados = 0
seguir="si"

while seguir == "si":
    nombre_del_encuestado = input("ingrese su nombre: ")

    edad_ingresada = int(input("ingrese su edad: "))
    while edad_ingresada < 18:
        edad_ingresada= int(input("ingrese su edad: "))

    situacion_laboral=input("tiene empleo si-no: ")
    while situacion_laboral!="si" and situacion_laboral!="no":
        situacion_laboral = input("reingresar situacion laboral: ")
        
    genero_ingresado=input("ingrese su genero(masculino-femenino-otro: )")
    while genero_ingresado!="masculino" and genero_ingresado!="femenino" and genero_ingresado !="otro":
        genero_ingresado=input("reingrese su genero(masculino-femenino-otro): ")

    voto_ingresado=input("ingrese su voto (apple-dunkin-ikea): ")
    while voto_ingresado!="apple" and voto_ingresado!="dunkin" and voto_ingresado!="ikea":
        voto_ingresado=input("reingrese su voto (apple-dunkin-ikea): ")
    
    total_votos += 1 #cuenta los votos
        
#1. Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA.
#2. Nombre y género del encuestado de menor edad que votó por APPLE.
#3. Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años.

    
    match genero_ingresado:
        case "masculino":
        
            if edad_ingresada >=18 and edad_ingresada <=25:
                contador_votos_masculinos+=1
            elif edad_ingresada >=36 and edad_ingresada <=49:
                contador_votos_masculinos+=1
        
        case "femenino":
            if edad_ingresada > 18 and edad_ingresada <25:
                contador_votos_femenino +=1
            elif edad_ingresada >36 and edad_ingresada <49:
                contador_votos_femeninos_mayor +=1
    
    match voto_ingresado:
        case "apple":
            if bandera_votos_apple==0:
                nombre_encuestado_menor_edad_apple = nombre_del_encuestado
                genero_encuestado_menor_edad_apple = genero_ingresado
                edad_encuestado_menor_edad_apple = edad_ingresada
                bandera_votos_apple = 1
            elif edad_ingresada < edad_encuestado_menor_edad_apple:
                nombre_encuestado_menor_edad_apple=nombre_del_encuestado
                genero_encuestado_menor_edad_apple=genero_ingresado
                edad_encuestado_menor_edad_apple=edad_ingresada
            contador_votos_apple += 1
            
        case "DUNKIN":
            contador_votos_dunkin +=1

        case "ikea":
            if genero_ingresado == "femenino" and edad_ingresada > 25:
                contador_votos_femeninos_mayor += 1
                
        case "ikea":
            contador_votos_ikea +=1
                
    seguir=input("quiere seguir si-no: ")
    
    match situacion_laboral:
        case "si":
            total_edad_empleados += edad_ingresada
            total_empleados += 1
        case "no":
            total_edad_no_empleados += edad_ingresada
            total_no_empleados += 1
        
if total_votos > 0:
    porcentaje_femenino_ikea_mayor = (contador_votos_femeninos_mayor / total_votos)*100

if total_empleados > 0:
    promedio_edad_empleados = total_edad_empleados / total_empleados
else:
    promedio_edad_empleados = 0

if total_no_empleados > 0:
    promedio_edad_no_empleados = total_edad_no_empleados / total_empleados
else:
    promedio_edad_no_empleados = 0

if contador_votos_apple > contador_votos_dunkin and contador_votos_apple > contador_votos_ikea:
    franquicia_mas_votada = "APPLE"
    
elif contador_votos_dunkin > contador_votos_ikea:
        franquicia_mas_votada = "DUNKIN"
    
else:
    franquicia_mas_votada = "IKEA"
    

print(f"contador de votos masculino: {contador_votos_masculinos}")
print(f"El encuestado de menor edad que voto por APPLE es: {nombre_encuestado_menor_edad_apple} con genero: {genero_encuestado_menor_edad_apple} y edad: {edad_encuestado_menor_edad_apple}")
print(f"El porcentaje de encuestados de genero femenino que votaron por IKEA y tienen mas de 25 es: {porcentaje_femenino_ikea_mayor}%")
print(f"Edad promedio de los encuestados empleados: {promedio_edad_empleados}")
print(f"Edad promedio de los encuestados no empleados: {promedio_edad_no_empleados}")
print(f"La franquicia mas votada es: {franquicia_mas_votada}")