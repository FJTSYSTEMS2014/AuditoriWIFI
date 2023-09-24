import os
import subprocess
import re
import signal
os.system(f"clear")
nversion="1v1"
print("#########################################################################\n")
print("                          @FranckTscherig                                  ")
print("-------------------       AUDITORIA WIFI      -----------------------------")
print(f"                                {nversion}                              \n")
print("#########################################################################\n")

print(f"------------------                                       ")
print(f"# Verificando si el modo monitor es compatible\n")

# Verificar si el modo monitor de paquetes son compatibles
try:
    iw_output = subprocess.check_output(["iw", "list"], stderr=subprocess.STDOUT, text=True)
    if "monitor" in iw_output.lower():
        print("La tarjeta Wi-Fi es compatible con el modo monitor.\n")
    else:
        print("La tarjeta Wi-Fi no es compatible con el modo monitor.")
        exit(1)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar 'iw list': {e}")
    exit(1)
print(f"------------------                                       ")
print(f"# Listando las interfaces Wi-Fi disponibles \n               ")

# Listar las interfaces Wi-Fi disponibles
iwconfig_output = subprocess.check_output("iwconfig", shell=True).decode("utf-8")
print("Interfaces Wi-Fi disponibles:\n")
print(iwconfig_output)
print(f"------------------                                       ")
print(f"# Solicitando una interfaz Wi-Fi \n            ")

# Solicitar al usuario que seleccione una interfaz Wi-Fi
wlan_interface = input("Ingresa el nombre de la interfaz Wi-Fi a utilizar (por ejemplo, wlan0): ")


# Matar procesos innecesarios
print(f"------------------                                       ")
print(f"# Deshabilitando procesos que pueden causar problemas para habilitar el Modo Monitor")
os.system(f"airmon-ng check kill")

print(f"------------------                                       ")
print(f"# Solicitando habilitación del modo monitor               \n")

# Solicitar al usuario confirmación para habilitar el modo monitor
enable_monitor = input(f"¿Deseas habilitar el modo monitor en {wlan_interface}? (y/n): ").lower()
if enable_monitor != "y":
    print("Modo monitor no habilitado. Saliendo del script.")
    exit(1)
    print(f"------------------                                       ")
    print(f"# Colocar la interfaz en modo monitor                    ")

# Colocar la interfaz en modo monitor
subprocess.run(f"sudo airmon-ng start {wlan_interface}", shell=True)
print(f"------------------                                       ")
print(f"# Solicitud de nombre de la interfaz en modo monitor          ")

# Solicitar al usuario que ingrese el nombre de la interfaz en modo monitor
monitor_interface = input("Ingresa el nombre de la interfaz en modo monitor (por ejemplo, wlan0mon): ")

#puedes hacer lo mismo pero ahora para verificacion de si la placa de wifi es compatible para la inyeccion de paquetes, la variable es monitor_interface . ejecutando sudo aireplay-ng --test monitor_interface
# Comando para probar la inyección de paquetes
command = ["sudo", "aireplay-ng", "--test", monitor_interface]

try:
    subprocess.run(command, check=True)
    print(f"La tarjeta Wi-Fi {monitor_interface} es compatible con la inyección de paquetes.\n")
except subprocess.CalledProcessError:
    print(f"La tarjeta Wi-Fi {monitor_interface} no es compatible con la inyección de paquetes.")
    exit(1)


# Cambiar la dirección MAC de la interfaz en modo monitor
print(f"------------------                                       ")
print(f"# Solicitud de Cambio de MAC de la interfaz en modo monitor")
mac_networks = input("¿Deseas Cambiar la dirección MAC de la interfaz en Modo Monitor? (y/n): ").lower()
if mac_networks != "y":
    print("No se realizará el Cambio de la dirección MAC de la interfaz en Modo Monitor. Saliendo del script.")
    exit(1)
print(f"Cambiando la dirección MAC de {monitor_interface}...\n")
subprocess.run(f"sudo ifconfig {monitor_interface} down", shell=True)
subprocess.run(f"sudo macchanger -r {monitor_interface}", shell=True)
subprocess.run(f"sudo ifconfig {monitor_interface} up", shell=True)

print(f"------------------                                       ")
# Mostrar la nueva dirección MAC 
ifconfig_output = subprocess.check_output(f"ifconfig {monitor_interface}", shell=True).decode("utf-8")
print(f" # Informacion de {monitor_interface} :")
print(ifconfig_output)
print(f"# Solicitar confirmación para escanear redes Wi-Fi       ")
print(f"------------------                                       ")
# Solicitar al usuario confirmación para escanear redes Wi-Fi
scan_networks = input("¿Deseas escanear las redes Wi-Fi disponibles? (y/n): ").lower()
if scan_networks != "y":
    print("No se realizará el escaneo de redes. Saliendo del script.")
    exit(1)
# Inicia el proceso de airodump-ng
print(f"------------------                                       ")
print(f"# guardando redes WIFI en Vivo en trafico/redesWifi-Area.log (Detener con ctrl+ c)")
os.system("sudo airodump-ng wlan0mon > trafico/redesWifi-Area.log")

print(f"------------------                                       ")
print(f"# Ver redes WIFI en Vivo (Detener con ctrl+ c)")
subprocess.run(f"sudo airodump-ng {monitor_interface}", shell=True)


print(f"------------------                                       ")
print(f"A continuación ......  Escaneamos una red en especifica  ")

# Solicitar al usuario que indique el BSSID Objetivo 
print(f"------------------                                       ")
print(f"# Solicitando una  BSSID  Objetivo (ejemplo:04:95:E6:22:64:78) \n")

user_bssid  = input("# Ingresar  BSSID  del Objetivo ")

print(f" La MAC del Objetivo ingresado es: {user_bssid}   \n")
# Solicitar al usuario que indique el BSSID Objetivo 
print(f"------------------                                       ")
print(f"# Solicitando  el CANAL  Objetivo     \n")

user_channel = input("Ingresar el Canal del Objetivo ( ejemplo: 1 ) :")
print(f" El canal del Objetivo ingresado es:  {user_channel}    \n")

print("#######################################################################################\n")
print(" ### Abrir otra consola (CTRL+Shift+R) Ejecutando el Script: sudo python DesAuntenticar.py ###")
print(" ###     o mediante el comando:                                                         ###")
print(" ###     sudo aireplay-ng -0 (repeticion) -a (BSSID) -c (STATION) wlan0mon              ###")
print(" ### ------------------------         EJEMPLO        ---------------------------------  ###")
print(" ###     sudo aireplay-ng -0 9 -a 04:95:E6:22:64:78 -c 28:35:45:74:6F:14  wlan0mon      ###")
print("#######################################################################################\n")
print(" \n")
scan_networks = input(f"¿Deseas Capturar trafico del WIfi con el BSSID:{user_bssid} y CHANNEL:{user_channel} indicados anteriormente? (y/n): \n").lower()
if scan_networks != "y":
    print("No se realizará el escaneo de la red previamente configurada. Saliendo del script.")
    exit(1)
print(f"Capturando trafico del WIfi  en - trafico/capturefile_{user_bssid}  - con el BSSID: {user_bssid} y CHANNEL:{user_channel} ")
print(f"---------------------------------------------------------------------------------------------- (Detener Captura ctrl+ c)\n")

mac_sin_dos_puntos = user_bssid.replace(":", "")

subprocess.run(f"sudo airodump-ng -c {user_channel} --bssid {user_bssid} -w trafico/capturefile_{mac_sin_dos_puntos} {monitor_interface}", shell=True)

# Solicitar al usuario confirmación para limpiar y detener el modo monitor
stop_monitor = input("¿Deseas detener el modo monitor? (y/n): ").lower()
if stop_monitor == "y":
    subprocess.run(f"sudo airmon-ng stop {monitor_interface}\n", shell=True)
    print(f"------------------                                       ")
    print("Modo monitor detenido.")
# Solicitar al usuario confirmación iniciar interfaz
    print(f"------------------                                       ")
    print("Modo para el restablecimiento del adaptador WIFI")
# Listar las interfaces Wi-Fi disponibles
iwconfig_output1 = subprocess.check_output("iwconfig", shell=True).decode("utf-8")
print(f"------------------                                       ")
print(" Listando las interfaces Wi-Fi disponibles:\n")
print(iwconfig_output1)

print(f"------------------                                       ")
print(f"# Soleccionar una interfaz Wi-Fi para restablecer (por ejemplo wlan0)\n            ")

# Solicitar al usuario que seleccione una interfaz Wi-Fi
wlan_interface1 = input("Restablece la conexión Wi-Fi a utilizar (por ejemplo, wlan0): \n")
print(f" la interfaz seleccionada es: {wlan_interface1}  \n")
up_red = input(f"¿Deseas iniciar el restablecimiento del servicio de {wlan_interface1} normalmente   (y/n): \n").lower()   
if up_red == "y":
    subprocess.run(f"sudo service NetworkManager restart && sudo ifconfig {wlan_interface1} down && sudo iwconfig {wlan_interface1} mode managed && sudo ifconfig {wlan_interface1} up", shell=True)
    
print(f"------------------                                       ")
print("Proceso de auditoría finalizado. Adios!")















