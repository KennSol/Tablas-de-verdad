def conjunción (p,q):
    return p and q

def disyuncion (p,q):
    return p or q

def condicional (a,b):
    return (not a) or b

def bicondicional (a,b):
    return a == b

def disyuncion_excluyente (a,b):
    None

def tabla(conector,nombre):
    print(f"Tabla de verdad para {nombre}:")
    print("A | B | Resultado")
    print("--+---+----------")
    for p in [False, True]:
        for q in [False, True]:
            resultado = conector(p,q)
            print(f"{int(p)} | {int(q)} | {int(resultado)}")
            print("--+---+----------")  # Espacio entre tablas


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
    input(print("Opcion: "))
    match op:
        case 1:
            nombre="Conjuncion"
            tabla(conjunción,nombre)
        case 2:
            nombre="Disyuncion"
            tabla(disyuncion,nombre)
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