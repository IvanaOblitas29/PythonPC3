import modulo


while True:
    print("1.Dividir dos números")
    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(modulo.dividir(num1, num2))
    elif opcion == '2':
        break