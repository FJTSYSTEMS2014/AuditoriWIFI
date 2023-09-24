import os

os.system(f"clear")
nversion="1v1"
print("#########################################################################\n")
print("                          @FranckTscherig                                  ")
print("Este script primero lista los archivos TXT en la carpeta 'diccionario'     ")
print("y los archivos CAP en la carpeta 'trafico'. Luego, permite seleccionar     ")
print("un archivo de cada carpeta y muestra las selecciones. Después, pregunta    ")
print("si se desea ejecutar el comando aircrack-ng  con los archivos seleccionados")
print(f"                                {nversion}                              \n")
print("#########################################################################\n")


def listar_archivos_en_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]
    return archivos_txt

def listar_archivos_cap():
    carpeta_trafico = 'trafico'
    archivos_cap = [archivo for archivo in os.listdir(carpeta_trafico) if archivo.endswith('.cap')]
    return archivos_cap

def seleccionar_archivo(lista_archivos, mensaje):
    print("Archivos disponibles:")
    for i, archivo in enumerate(lista_archivos, start=1):
        print(f"{i}. {archivo}")
    
    while True:
        try:
            seleccion = int(input(mensaje))
            if 1 <= seleccion <= len(lista_archivos):
                return lista_archivos[seleccion - 1]
            else:
                print("Selección inválida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

def main():
    while True:
        diccionarios = listar_archivos_en_carpeta('diccionario')
        cap_files = listar_archivos_cap()
        
        if not diccionarios:
            print("Problema Detectado:                             ")
            print("no hay archivos TXT en la carpeta 'diccionario'.")
            continuar = input("¿Desea realizar otra configuración? (si/no): ").lower()
            if continuar != 'si':
                break
            else:
                continue

        if not cap_files:
            print("Problema Detectado:                             ")
            print("no hay archivos CAP en la carpeta 'trafico'.")
            continuar = input("¿Desea realizar otra configuración? (si/no): ").lower()
            if continuar != 'si':
                break
            else:
                continue
        print("---------------------------------------                            \n")
        archivo_diccionario = seleccionar_archivo(diccionarios, "Seleccione un archivo TXT de diccionario: ")
        print("---------------------------------------                            \n")
        archivo_cap = seleccionar_archivo(cap_files, "Seleccione un archivo CAP de tráfico: ")
        print("---------------------------------------                            \n")
        print(f"Seleccionó el archivo '{archivo_diccionario}' como \n diccionario y '{archivo_cap}' como archivo de tráfico.")

        ejecutar = input("¿Desea ejecutar el comando aircrack-ng con los archivos seleccionados? (si/no): ").lower()
        if ejecutar == 'si':
            comando = f"aircrack-ng -w diccionario/{archivo_diccionario} trafico/{archivo_cap}"
            os.system(comando)
        
        reiniciar = input("¿Desea realizar otra configuración? (si/no): ").lower()
        os.system(f"clear")
        if reiniciar != 'si':
            break

if __name__ == "__main__":

    main()
