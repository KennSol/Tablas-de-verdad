def conjunción (p,q):
    return p and q

def disyuncion (p,q):
    return p or q

def condicional (a,b):
    None

def bicondicional (a,b):
    None

def disyuncion_excluyente (a,b):
    None

def tabla(conector,nombre):
    print(f"Tabla de verdad para :")
    print("A | B | Resultado")
    print("--+---+----------")





def menu ():
    print("*Tablas de Verdad*")
    print("Opciones: "
    "1. Conjuncion"
    "2. Disyuncion"
    "3. Condicional"
    "4. Bicondicional"
    "5. Distuncion Excluyente"
    "6. Salir")

op=0
nombre=None
while True:
    menu()
    match op:
        case 1:
            nombre="Conjuncion"
        case 2:
            nombre="Disyuncion"
        case 3:
            nombre="Condicional"
        case 4:
            nombre="Bicondicional"
        case 5:
            nombre="Distuncion Excluyente"
        case 6:
            break
        case _:
            print("!NO VALIDO, VUELVA A INGRESAR LA OPCION! ")