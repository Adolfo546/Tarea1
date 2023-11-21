valor1=int(input("Ingrese el primer valor: "));
valor2=int(input("Ingrese el segundo valor: "));

if valor1 > valor2:
    print("El primer valor es mayor que el segundo valor.")
    print("El segundo valor es menor que el primer valor.")
elif valor1 < valor2:
    print("El segundo valor es mayor que el primer valor.")
    print("El primer valor es menor que el segundo valor.")
else:
    print("Ambos valores son iguales.")