def conjunción (p,q):
    return p and q

def disyuncion (p,q):
    return p or q

def condicional (p,q):
    return (not p) or q

def bicondicional (p,q):
    return p == q

def disyuncion_excluyente (p,q):
    return not(p==q)

def tabla(conector,nombre):
    print(f"Tabla de verdad para {nombre}:")
    print("p | q | Resultado")
    print("--+---+------------")
    for p in [False, True]:
        for q in [False, True]:
            resultado = conector(p,q)
            print(f"{int(p)} | {int(q)} |     {int(resultado)}")
            print("--+---+------------")  # Espacio entre tablas


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
    op=int(input("Opcion: "))
    match op:
        case 1:
            nombre="Conjuncion"
            tabla(conjunción,nombre)
        case 2:
            nombre="Disyuncion"
            tabla(disyuncion,nombre)
        case 3:
            nombre="Condicional"
            tabla(condicional,nombre)
        case 4:
            nombre="Bicondicional"
            tabla(bicondicional,nombre)
        case 5:
            nombre="Distuncion Excluyente"
            tabla(disyuncion_excluyente,nombre)
        case 6:
            break
        case _:
            print("!NO VALIDO, VUELVA A INGRESAR LA OPCION! ")