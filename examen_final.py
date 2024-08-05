voto_masculino = 0
voto_masculino_edad18 = 0
voto_masculino_edad36 = 0
voto_masculino_ikea = 0
menor_edad_apple = None
nombre_menor_edad_apple = None
genero_menor_edad_apple = None
femenino_ikea_mayor_25 = 0
total_femenino = 0
total_encuestados = 0
edad_empleados = 0
edad_no_empleados = 0
empleados_contador = 0
no_empleados_contador = 0
votos_apple = 0
votos_dunkin = 0
votos_ikea = 0

while True:
    nombre = input("Ingrese su nombre (o 'FIN' para terminar): ")
    if nombre == 'FIN':
        break

    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("La edad no puede ser menor a 18.")
        continue

    empleado = input("Está empleado? (si-no): ")
    genero = input("Ingrese su género (Masculino - Femenino - Otro): ")
    voto = input("Ingrese su voto (APPLE, DUNKIN, IKEA): ")

    total_encuestados += 1

    if genero == "Masculino":
        voto_masculino += 1
        if 18 <= edad < 25:
            voto_masculino_edad18 += 1
        if 36 <= edad < 49:
            voto_masculino_edad36 +=1
        if voto == "IKEA":
            voto_masculino_ikea +=1
    

    # if voto == "APPLE":
    #     if menor_edad_apple is None or edad < menor_edad_apple:
    #         menor_edad_apple = edad
    #         nombre_menor_edad_apple = nombre
    #         genero_menor_edad_apple = genero

    # if genero == "Femenino":
    #     total_femenino += 1
    #     if voto == "IKEA" and edad > 25:
    #         femenino_ikea_mayor_25 += 1

    # if empleado == "si":
    #     empleados_contador += 1
    #     edad_empleados += edad
    # else:
    #     no_empleados_contador += 1
    #     edad_no_empleados += edad

    # if voto == "APPLE":
    #     votos_apple += 1
    # elif voto == "DUNKIN":
    #     votos_dunkin += 1
    # elif voto == "IKEA":
    #     votos_ikea += 1

# Resultados
# print(f"Cantidad de encuestados de género Masculino, cuya edad esté entre 18 y 25 o entre 36 y 49 o que votaron por IKEA: {masculino_edad_y_voto}")

# if nombre_menor_edad_apple:
#     print(f"Nombre y género del encuestado de menor edad que votó por APPLE: {nombre_menor_edad_apple}, {genero_menor_edad_apple}")
# else:
#     print("No hubo encuestados que votaron por APPLE.")

# if total_femenino > 0:
#     porcentaje_femenino_ikea_mayor_25 = (femenino_ikea_mayor_25 / total_femenino) * 100
#     print(f"Porcentaje de encuestados de género Femenino que votaron por IKEA con edad mayor a 25 años: {porcentaje_femenino_ikea_mayor_25:.2f}%")
# else:
#     print("No hubo encuestadas de género Femenino.")

# if empleados_contador > 0:
#     edad_promedio_empleados = edad_empleados / empleados_contador
#     print(f"Edad promedio de los encuestados que están empleados: {edad_promedio_empleados:.2f}")
# else:
#     print("No hubo encuestados empleados.")

# if no_empleados_contador > 0:
#     edad_promedio_no_empleados = edad_no_empleados / no_empleados_contador
#     print(f"Edad promedio de los encuestados que no están empleados: {edad_promedio_no_empleados:.2f}")
# else:
#     print("No hubo encuestados no empleados.")

# if votos_apple > votos_dunkin and votos_apple > votos_ikea:
#     franquicia_mas_votada = "APPLE"
# elif votos_dunkin > votos_apple and votos_dunkin > votos_ikea:
#     franquicia_mas_votada = "DUNKIN"
# else:
#     franquicia_mas_votada = "IKEA"

# print(f"La franquicia más votada fue: {franquicia_mas_votada}")

print(f"Total encuestados: {total_encuestados}")
print(f"Votos masculinos: {voto_masculino}")
print(f"Votos masculinos de 18 a 24 años: {voto_masculino_edad18}")
print(f"Votos masculinos de 36 a 48 años: {voto_masculino_edad36}")
print(f"Votos masculinos por IKEA: {voto_masculino_ikea}")