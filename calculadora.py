# -*- coding: utf-8 -*-

# Calculadora
# Autor: Jorge Zaldívar
# Fecha: 17/feb/21

# Escribe tu programa a continuación

# Entradas
a = eval(raw_input("Dame un número: "))
b = eval(raw_input("Dame otro número: "))
op = raw_input("¿Que operación? ")

# Proceso
if op.lower() == "sumar":
  resultado = a + b
  salida = "La suma de " + str(a) + " y " + str(b) + " es " + str(resultado)
elif op.lower() == "restar":
  resultado = a - b
  salida = "La resta de " + str(a) + " menos " + str(b) + " es " + str(resultado)
elif op.lower() == "multiplicar":
  resultado = a * b
  salida = "La multiplicación de " + str(a) + " y " + str(b) + " es " + str(resultado)
elif op.lower() == "dividir":
  resultado = a / b
  salida = str(a) + " entre " + str(b) + " da " + str(resultado)

# Salidas
print(salida)