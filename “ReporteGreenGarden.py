import csv 
import subprocess

agregar_cliente1=True
agregar_compra1=True
lista_productos1=[]
data=[]
lista_productos_c=[]
valor=0
valor_de_venta=0
valor_de_compra=0

def no_valido():
    print("***NO VALIDO***\nintentar nuevamente\n")

def no_disponible():
    print("***No disponible***\nintentar nuevamente\n")

def validar_entrada(mensaje, condicion):
 while True:
  entrada=input(mensaje)
  if condicion(entrada):
     return entrada
  print("***Entrada NO valida. Intente nuevamente***")


def menu_productos():
    print(
        """

        PRODUCTOS
    Producto:     Cantidad   Valor:
    1. Abono         0        1.200
    2. Tierra        0        1.000
    3. Lirio         0        1.100
    4. Rosas Rojas   0        1.700
    5. Margaritas    0        1.100

    0. Salir
    """
    )

print("Empresa GreenJarden")

def gestionar_pedido():
    agregar_cliente1={}
    lista_productos1=[]
    total_venta=0



while agregar_cliente1:

    lista_productos_c.clear()
    print("Bienvenid@")
    print("\nIngrese sus datos")

    nombre=input("Nombre: ")
    while not nombre.isalpha():
        no_valido()
        nombre=input("Nombre: ")

    telefono=input("Telefono: ")
    while not telefono.isdigit() or len(telefono)<9 or len(telefono)>9:
        if len(telefono)<9 or len(telefono)>9:
            print("***Debe ingresar 9 digitos***\nintente nuevamente\n")
        else:
            no_valido()
        telefono=input("Telefono: ")

    direccion=input("Direccion: ")

    agregar_compra=True
    lista_productos_c.clear()
    valor_de_venta=0
    while agregar_compra:
        menu_productos()
        
        producto=input("Ingrese numero de producto: ")
        if int(producto)==0:
            agregar_cliente=False
            break
    while not producto.isdigit()or int(producto)<0 or int(producto)>5:
        if producto.isdigit():
            if int (producto)<0 or int(producto)>5:
                no_disponible()
            elif producto.lower()=="m":
                menu_productos()
            else:
                no_valido()
                producto=input("Ingrese cantidad del producto:")
                unidades_pro=input("Ingrese cuantas unidades desea:")
                while not unidades_pro.isdigit()or int (producto)<0:
                    if unidades_pro.isdigit():
                        if int(producto)<0:
                            no_disponible
                        else:
                            no_valido()
                            unidades_pro=input("Unidades:")
            if int(producto)==1:
                valor=1200
            if int(producto)==2:
                valor=1000
            if int(producto)==3:
                valor=1100
            if int(producto)==4:
                valor=1700
            if int(producto)==5:
                valor=1100

            valor_de_venta+=valor*int(unidades_pro)
            valor_de_compra=valor*int(unidades_pro)

            compra=input("Agregar Compra:\n1. Si \n2. No\n")
            while not compra.isdigit() or int (compra)!=1 and int (compra)!=2:
                if not compra.isdigit():
                    no_valido()
                elif int (compra)!=1 or int (compra)!=2:
                    no_disponible()

                compra=input("Desea agregar compra: \n1. Si \n2. No\n")
                if int(compra)==2:
                    agregar_compra=False

            data.append([nombre,telefono,direccion,lista_productos_c])

        print(f"""****DATOS DE SU COMPRA***** 
              ****PRODUCTOS:****
              """)
        for i in lista_productos1:
            print (i)
            print(f"PRECIO FINAL:
                  {valor_de_venta}$\n*****")
            
            nuevo_cliente=input("Desea agregar cliente?:")
        if int (nuevo_cliente)==2:
            agregar_cliente=False
            print("saliendo...")




with open("data.csv", "w")as archivo_csv:
    escritor_csv= csv.writer(archivo_csv)
    escritor_csv.writerow([nombre, telefono, producto])
    escritor_csv.writerows(data)