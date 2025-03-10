import time
def conjunción_ (*var):
    return all(var)

def disyuncion (*var):
    return any(var)

def condicional(p,q,r=None):
    if r is None:
        return (not p) or q  
    else:
        return (not (p and not q)) or r

def bicondicional(p,q,r=None):
    if r is None:
        return p == q 
    else:
        return p == q == r  

def disyuncion_excluyente (p,q,r=None):
    if r is None:
        return not(p==q)
    else:
        return not(p == q == r)

def tabla(conector,nombre,c):
    print(f"Tabla de verdad para {nombre}:")
    if c==1:
        print(f"| p | {nombre}")
        print("--+--------------")
        time.sleep(0.5)
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
                    print("----+---+------------")
                    time.sleep(1)
                else:
                    for c in [False, True]:
                        resultado = conector(p, q, r)
                        print(f"{int(p)} | {int(q)} | {int(r)} | {int(resultado)}")
                        print("--+---+---+----------")
                        time.sleep(1)


def menu ():
    print("*Tablas de Verdad*")
    time.sleep(0.5)
    print("""***Menu de Opciones*** 
    1. Generar Tablas de Verdad
    2. Ingresar variables
    3. Salir""")

def menu2 ():
    print("*Tablas de Verdad*")
    time.sleep(0.5)
    print("""**Expresiones Logicas**
    1. Conjuncion
    2. Disyuncion
    3. Condicional
    4. Bicondicional
    5. Disyuncion Excluyente""")
op=0
variable=""
nombre=""
c=0
while True:
    menu()
    op=int(input("Opcion: "))
    match op:
        case 1:
            if c < 1:
                print("!NO HA INGRESADO VARIABLES!")
            else:
                menu2()
                op=int(input("Expresion a Ingresar: "))
                match op:
                    case 1:
                        if c==1:
                            nombre="p^p"
                            tabla(conjunción_,nombre,1)
                        elif c==2:
                            nombre="p^q"
                            tabla(conjunción_,nombre,2)
                        else:
                            nombre="(p^q)^r"
                            tabla(conjunción_,nombre,3)
        case 2:
            if c < 1:
                variable=input("Ingrese la Variable: ")
                c=c+1
            elif c > 3:
                print("!MAXIMO DE VARIABLES ALCANZADO!")
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