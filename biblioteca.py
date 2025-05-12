biblioteca = {}


def agregar():
    print("<----creando libro---->")

    id = int(input("ingrese el id:"))
    if id in biblioteca:
        print("este id ya se encuentra")
    else:
        titulo = input("ingrse el titulo del libro: ")
        autor = input("ingrese el autor: ")
    try:
        year = int(input("ingrese el año de publicacion: "))
    except ValueError:
        print("año invalido vuelve a intentarlo")
        return
    biblioteca[id] = {'titulo': titulo, 'autor': autor, 'año': year}

    print("----libro creado con exito----")


def ver():
    print(biblioteca)


def buscar_libro():

    opcion = input("1) buscar por id--->2) buscar por el titulo--->")
    if opcion == "1":
        id = int(input("ingresa el id"))
        opcion = biblioteca.get(id)
        print(opcion)
    elif opcion == "2":
        titulo = input("ingresa el titulo")
        titulo = biblioteca.get(id,['titulo'])
        


        #titulo = input("ingrese el titulo").lower()
       # bucar_libro = [(id, datos)
                       #for id, datos in biblioteca.items()
                      ## if datos['titulo'].lower() == titulo]
        #if buscar_libro:
            #for id, datos in bucar_libro:
               # print(f"{id}{datos}")
        #else:
               # print("libro encontrado")
    else:
            print("opcion invalida")


while True:
    print("\n <-------MENU-----> \n 1) agregar libro\n 2) ver libro\n 3) buscar libro \n 4) modificar libro\n 5) eliminar libro")

    opcion = input("ingrese una opcion: ")
    if opcion == "1":
        agregar()
    elif opcion == "2":
        ver()
    elif opcion == "3":
        buscar_libro()
