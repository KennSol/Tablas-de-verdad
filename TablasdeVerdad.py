import time
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

def tabla(conector,nombre,c):
    print(f"Tabla de verdad para {nombre}:")
    if c==1:
        None
    elif c==2:
        print(f"| p | q | {nombre}")
        print("--+---+--------------")
        time.sleep(0.5)
    elif c==3:
        print(f"| p | q | r | {nombre}")
        print("--+---+---+----------")
    for p in [False, True]:
        if c==1:
            None
        else:
            for q in [False, True]:
                if c==2:
                    resultado = conector(p,q)
                    print(f"| {int(p)} | {int(q)} |     {int(resultado)}")
                    print("----+---+------------")  # Espacio entre tablas
                    time.sleep(1)
                else:
                    for c in [False, True]:
                        resultado = conector(p, q, r)
                        print(f"{int(p)} | {int(q)} | {int(r)} | {int(resultado)}")
                        time.sleep(1)


def menu ():
    print("*Tablas de Verdad*")
    time.sleep(0.5)
    print("""***Menu de Opciones*** 
    1. Generar Tablas de Verdad
    2. Ingresar variables
    3. Salir""")

op=0
nombre=""
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
            print("Saliendo en")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("Adios")
            break
        case _:
            print("!NO VALIDO, VUELVA A INGRESAR LA OPCION! ")