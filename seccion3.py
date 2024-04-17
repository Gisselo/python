#Pide el nombre, apellido y edad del usuario. Después muestra un saludo y su edad dentro de 10 años.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad_futura = edad + 10
print ("Hola", nombre, "en 10 años tendras: ", edad_futura ,"años") 

#Pide la base y altura con números decimales de un rectángulo. Calcula el área y muestrala
base = float(input("Ingresa la base del rectangulo: "))
altura = float(input("Ingresa la altura del rectangulo: "))
area = base * altura
print("El area del rectangulo es: ",area, " cm²")

#Utiliza el operador + para concatenar cadenas con el ejemplo que tu desees
nombre = input("Ingresa tu nombre: ")
mensaje = input('Exactamente ' + nombre + 'CeoVLogs tienes toda tu boca llena de razon y tus pensamientos claros y decisivos')
print(mensaje)

#Crea un array con numeros, sumalos y muestra el total
n = [1,2,3,4,5]
suma = n[0]+n[2]+n[4]
print("El resultado de la suma es: ", suma)

#Crea una matriz 2x2 y muéstrala por pantalla
m = [ [12,2],
      [2,12]]

print("Matriz")
print(m[0][0])
print(m[0][1])
print(m[1][0])
print(m[1][1])