# verificar si se tiene acceso 
#a la libreria io de python (Anaconda lo trae)

# para crear en otro directorio libreria os

#1. Instalar libreria
#2. Hacer el import

documento = open("prueba.txt","a")  # crea y abre para escribir
documento.writelines(["\nuno","\ndos","\ntres"])
documento.close()


document= open("prueba.txt","r")
texto=document.read()
document.close()
print(texto)