suma = 0

# primer número
num1 = int(input("Ingrese el primer número: "))
if num1 % 2 == 0:
    suma = suma + num1 

# segundo número
num2 = int(input("Ingrese el segundo número: "))
if num2 % 2 == 0:
    suma = suma + num2 

# tercer número
num3 = int(input("Ingrese el tercero número: "))
if num3 % 2 == 0:
    suma = suma + num3 

print(f"La suma de los números pares es: {suma}")
