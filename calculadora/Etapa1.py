# calculadora 


# Solicitar ao usuário que insira o números e a operação.



numero1 = float(input("Digite o primeiro número:"))
operador = input("digite o operador (+, -, *, /)")
numero2 = float(input("Digite o segundo número:"))

# Realizar a operação correspondente

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    resultado = numero1 / numero2
else:
    resultado = "Operador Inválido"

    # Exibir Resultado

print ("Resultado", resultado)    

#

 