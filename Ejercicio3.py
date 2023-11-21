num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
num3=int(input("Ingrese otro numero: "));

suma = num1 + num2 + num3;

if suma%7==0:
    mensaje=suma,"La suma de los valores es multiplo de 7."
else:
    mensaje=suma,"La suma de los valores no es multiplo de 7."
print(mensaje)
