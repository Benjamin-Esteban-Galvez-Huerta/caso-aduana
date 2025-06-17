#los datos de los turistas junto al pais, fecha donde llegaron y sus nombres ademas de la enumeracion 
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}
#esto es la primera opcion 
def tur_de_pais(pais):
    en = [datos[0] for datos in turistas.values() if datos[1].lower() == pais.lower()]
    if en:
        print(en)
    else: 
        print("No hay turistas de ese pais")
#esta es la funcion opción 2 confie esto servira
def tur_por_mes(mes):
    total = len(turistas)
    cantidad_mes = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            cantidad_mes += 1
    porcentaje = round((cantidad_mes / total) * 100, 1)
    return porcentaje
#esto hara funcionar la opcion 3
def remover_turista():
    nombre = input("Ingrese el nombre del turista a eliminar: ").lower()
    encontrado = False
    for key in list(turistas.key()):
        if turistas[key][0].lower() == nombre:
            del turistas[key]
            encontrado = True
            print("Turista eliminado con éxito.")
            break
    if not encontrado:
        print("Turista no encontrado. No se pudo eliminar.")

#esta estructura principal no entendido bien del main con otro por lo que lo use en el mismo codigo

def main():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1.- Turistas por país.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")

        opcion = input("Ingrese opción: ")
    
        if opcion == "1":
            pais = input("Ingrese pais a buscar: ")
            tur_de_pais(pais)

        elif opcion == "2":
         while True:
            try:
                mes = int(input("Ingrese mes a buscar: "))
                if 1 <= mes <= 12:
                    porcentaje = tur_por_mes(mes)
                    print(f"El número de turistas equivale el {porcentaje} % del total.")
                    break
                else: 
                   print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
            except ValueError:
                print("Debe ingresar un número valido")
        elif opcion == "3":
            remover_turista()

        elif opcion == "4":
            print("Programa terminado...")
            break
        else: 
            print("Debe seleccionar una opción válida flaco.")

main()