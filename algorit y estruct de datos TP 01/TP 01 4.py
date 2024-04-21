# Título: TP01-04 -  BILLETES SEGÚN VUELTO 
# Fecha: 31-2023
# Autor: Rocco Moresi (1185425)
# 
# Descripción:
# Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que 
# debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero 
# recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que 
# se minimice la cantidad de billetes. Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10. Emitir 
# un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $3170 y se abona con $5000, el 
# vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10. 

billetes = [5000,1000,500,200,100,50,10]

def billetesVuelto(montoAPagar, montoRecibido):


    vuelto = montoRecibido - montoAPagar

    vueltoTotal = vuelto 

    billetes5000 = vuelto // 5000
    vuelto = vuelto % 5000

    billetes1000 = vuelto // 1000
    vuelto = vuelto % 1000

    billetes500 = vuelto // 500
    vuelto = vuelto %  500

    billetes200 = vuelto// 200
    vuelto = vuelto %  200

    billetes100 = vuelto // 100
    vuelto = vuelto % 100

    billetes50 = vuelto // 50
    vuelto = vuelto % 50

    billetes10 = vuelto // 10
    vuelto = vuelto % 10

    if montoRecibido < montoAPagar:
        print("FALTA DINERO POR ABONAR...") 
    elif montoRecibido - montoAPagar == 0:
        print("PAGO JUSTO...")
    
    else:

        print("billetes de 5000:", billetes5000)
        print("billetes de 1000:", billetes1000)
        print("billetes de 500:", billetes500)
        print("billetes de 200:", billetes200)
        print("billetes de 100:", billetes100)
        print("billetes de 50:", billetes50)
        print("billetes de 10:", billetes10)
    
 
    
    return vueltoTotal


montoAPagar = int(input("Ingrese cuanto debe pagar el cliente: "))

montoRecibido = int(input("Ingrese cuanto abono el cliente: "))

vueltoTotal = billetesVuelto(montoAPagar, montoRecibido)

if vueltoTotal >= 0:

    print("El total del vuelto seria: ", vueltoTotal) 


    


    
