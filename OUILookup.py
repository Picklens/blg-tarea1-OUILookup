import sys
import random
import os

def buscaMacEnRed():
    IP= sys.argv[2]
    i=0
    mensaje=""
    listaFab= []
    for linea in abrirArchivo2():
        i=i+1
        if i >= 2:
            linea = linea.strip()
            listaTotal = linea.split()
            for a in listaTotal[2:3:]: #con el 2 tira la ultimas partes "xerox corporation", con el 1 tira xerox xerox corporation
                for k in listaTotal[:1]:
                    if sys.argv[2] == k:
                        listaFab.append(a)
                        for z in listaFab:
                            mensaje = mensaje+" "+ z
                            return mensaje
                    else:
                        return imprimirNOHAYIPENHOST()
                        
def retornarMac():
    mensaje =""
    newLista=[]
    for y in buscaMacEnRed():
        
        listaTotalMac = y.split()
        y = y.strip(":")
        for u in listaTotalMac[0:3:]:#revisar 2
            newLista.append(u)
    for a in newLista[:8:]:
        mensaje = mensaje+a
    return mensaje

def abrirArchivo():
    archivo=open("manuf","r",encoding="utf-8")
    archivo=archivo.readlines()
    return archivo

def abrirArchivo2():
    os.system("arp -n > datosArp")
    archivoARP=open("datosArp","r")
    archivoARP=archivoARP.readlines()
    return archivoARP

def macOriginal(mac):
    mensajeFinal =""
    newLista=[mac]
    listaFinal=[]

    for y in newLista:
        listaTotalMac = y.strip()
        lista = y.split(":")
        u=lista[:3]
        listaFinal= ":".join(u)
        listaFinal= listaFinal.upper()

    return listaFinal

def fabricanteMac(mac):
    i=0
    mensaje=""
    listaFab= []
    for linea in abrirArchivo():
        i=i+1
        if i >= 67:
            linea = linea.strip()
            listaTotal = linea.split()
            for a in listaTotal[2::]:
                for k in listaTotal[:1]:
                    if mac == k:
                        listaFab.append(a)
    for z in listaFab:
        mensaje = mensaje+" "+ z
    return mensaje

def imprimirNOHAYIPENHOST():
    print("Error: ip is outside the host network")
    exit(1)


def help():
    print("Uso: " + sys.argv[0] + " --ip <ip> | --mac <mac> [--help] ")
    print("\nParametros:")
    print("     --ip: especifique la IP del host a consultar.")
    print("     --mac: especifique la direccion MAC a consultar. EJ= aa:bb:cc:00:00:00. Obligatorio")
    print("     --help: muestra esta pantalla y termina. Opcional")
    exit(1)

if __name__ == "__main__":
    if len(sys.argv)==1:
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1]=="--help":
            help()

        if sys.argv[1]=="--ip":

            IP= sys.argv[2]
            mac1=retornarMac()
            mac2=fabricanteMac(mac1)

            print("\nIP: "+ IP )
            print("MAC ADDRESS: "+ mac1)
            print("Vendor: "+ mac2)
            
        elif sys.argv[1]=="--mac":

            mac=sys.argv[2]
            mac2=macOriginal(mac)
            mac3=fabricanteMac(mac2)
            
            print("\nMAC ADDRESS: "+ mac)
            print("Vendor: "+mac3)
            
        else:
            print("No ha ingresado los parametros solicitados")