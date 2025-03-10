import time
def conjunción (*var):
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
        return p != q  
    else:
        return (p + q + r) % 2 != 0

def tabla(conector,nombre,c):
    print(f"///Tabla de verdad para {nombre}:///")
    if c==1:
        print(f"| p |    {nombre}")
        print("--+--------------")
        time.sleep(0.5)
    elif c==2:
        print(f"| p | q |     {nombre}")
        print("--+---+--------------")
        time.sleep(0.5)
    elif c==3:
        print(f"| p | q | r |   {nombre}")
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
                    for r in [False, True]:
                        resultado = conector(p, q, r)
                        print(f"{int(p)} | {int(q)} | {int(r)} | {int(resultado)}")
                        print("--+---+---+----------")
                        time.sleep(1)


def menu ():
    print("///Tablas de Verdad///")
    time.sleep(0.5)
    print("""***Menu de Opciones*** 
    1. Generar Tablas de Verdad
    2. Ingresar variables
    3. Salir""")

def menu2 ():
    print("""**Expresiones Logicas**
    1. Conjuncion
    2. Disyuncion
    3. Condicional
    4. Bicondicional
    5. Disyuncion Excluyente
    6. Regresar a Menu Principal""")
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
                while op==1:
                    menu2()
                    op=int(input("Expresion a Ingresar: "))
                    match op:
                        case 1:
                            if c==1:
                                nombre="p^p"
                                tabla(conjunción,nombre,1)
                            elif c==2:
                                nombre="p^q"
                                tabla(conjunción,nombre,2)
                            else:
                                nombre="(p^q)^r"
                                tabla(conjunción,nombre,3)
                        case 2:
                            op=1
                            if c==1:
                                nombre="pvp"
                                tabla(disyuncion,nombre,1)
                            elif c==2:
                                nombre="pvq"
                                tabla(disyuncion,nombre,2)
                            else:
                                nombre="(pvq)vr"
                                tabla(disyuncion,nombre,3)
                        case 3:
                            op=1
                            if c==1:
                                nombre="p→p"
                                tabla(condicional,nombre,1)
                            elif c==2:
                                nombre="p→q"
                                tabla(condicional,nombre,2)
                            else:
                                nombre="(p→q)→r"
                                tabla(condicional,nombre,3)
                        case 4:
                            op=1
                            if c==1:
                                nombre="p↔p"
                                tabla(bicondicional,nombre,1)
                            elif c==2:
                                nombre="p↔q"
                                tabla(bicondicional,nombre,2)
                            else:
                                nombre="(p↔q)↔r"
                                tabla(bicondicional,nombre,3)
                        case 5:
                            op=1
                            if c==1:
                                nombre="p⊻p"
                                tabla(disyuncion_excluyente,nombre,1)
                            elif c==2:
                                nombre="p⊻q"
                                tabla(disyuncion_excluyente,nombre,2)
                            else:
                                nombre="(p⊻q)⊻r"
                                tabla(disyuncion_excluyente,nombre,3)
                        case 6:
                            op=0
                        case _:
                            print("!NO VALIDO!")
                            op=1
        case 2:
            if c < 3:
                variable=input("Ingrese la Variable: ")
                c=c+1
            else:
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