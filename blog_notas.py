import json
from datetime import datetime

def escribir_nota():
    nota = input("Escribe una nota: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    edit = False
    try:
        with open("notas.json", "r") as n:
            try:
                notas = json.load(n)
            except json.JSONDecodeError:
                notas = []   
    except FileNotFoundError:
        notas = [] 
        
    notas.append({"fecha":fecha, "contenido":nota, "editada":edit})
    with open("notas.json", "w") as n:
        json.dump(notas, n, indent=4)
        print("\nNota Agregada!!\n")
    menu()

def eliminar_todo():
    try:
        with open("notas.json", "r") as n:
            notas = json.load(n)
    except FileNotFoundError:
        print("Sin Notas")
        return
    if not notas:
        print("Sin Notas")
        return
    notas = []
    with open("notas.json", "w") as n:
        json.dump(notas, n ,indent=4)
        print("Notas Vaciadas!!")
    menu()
    
def eliminar_nota():
    try:
        with open("notas.json", "r") as n:
            notas = json.load(n)
    except FileNotFoundError:
        print("Sin Notas")
        return
    if not notas:
        print("Sin Notas")
        return
        
    for i, nota in enumerate(notas , start=1):
        if nota["editada"] == True:
            print(f"{i}. {nota['fecha']} - [EDIT] {nota['contenido']}")
        else:
            print(f"{i}. {nota['fecha']} - {nota['contenido']}")
    
    try:
        num = int(input("Selecciona nota a eliminar: "))
        if 1 <= num <= len(notas):
            del notas[num-1]
            with open("notas.json", "w") as n:
                json.dump(notas, n, indent=4)
            print("Nota Eliminada!!")
        else:
            print("Numero Invalido")
    except ValueError:
        print("Entrada Invalida")
    menu()
        
def actualizar_nota():
    try:
        with open("notas.json", "r") as n:
            notas = json.load(n)
    except FileNotFoundError:
        print("Sin Notas")
        return
    if not notas:
        print("Sin Notas")
        return
    
    for i, nota in enumerate(notas , start=1):
        if nota["editada"] == True:
            print(f"{i}. {nota['fecha']} - [EDIT] {nota['contenido']}")
        else:
            print(f"{i}. {nota['fecha']} - {nota['contenido']}")
        
    try:
        num = int(input("Selecciona nota a Editar: "))
        if 1 <= num <= len(notas):
            nuevo = input("Escribe la nueva nota: ")
            notas[num-1]["contenido"] = nuevo
            notas[num-1]["editada"] = True
            with open("notas.json", "w") as n:
                json.dump(notas, n, indent=4)
            print("Nota Cambiada!!")
        else:
            print("Numero Invalido")
    except ValueError:
        print("Entrada Invalida")
    menu()
        
def ver_notas():
    try:
        with open("notas.json", "r") as n:
            notas = json.load(n)
    except FileNotFoundError:
        print("Sin Notas")
        return
    if not notas:
        print("Sin Notas")
        return
    for i, nota in enumerate(notas , start=1):
        if nota["editada"] == True:
            print(f"{i}. {nota['fecha']} - [EDIT] {nota['contenido']}")
        else:
            print(f"{i}. {nota['fecha']} - {nota['contenido']}")

    menu()
        
def menu():
    print('''
    1 - Agregar Nota
    2 - Editar Nota
    3 - Eliminar Nota
    4 - Vaciar Notas
    5 - Mostrar Notas
    0 - Salir..''')
    try:
        opc = int(input("-> "))
        match opc:
            case 1: escribir_nota()
            case 2: actualizar_nota()
            case 3: eliminar_nota()
            case 4: eliminar_todo()
            case 5: ver_notas()
            case 0: 
                global salir 
                salir = False
            case _: 
                print("Opcion no Disponible")
                menu()
    except ValueError:
        print("Escoja Algo")
        

print('''________________
...BIENVENIDO...
________________''')

salir = True
while salir:
    menu()
    
print('''______________
SALIENDO......
______________''')
