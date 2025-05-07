def adicionar (n1, n2):
    """Retorna a soma de dois números"""
    return n1 + n2

def subtrair (n1, n2):
    """Retorna a diferença entre dois números"""
    return n1 - n2

def multiplicar (n1, n2):
    """Retorna o produto de dois números"""
    return n1 * n2

def dividir (n1, n2):
    """Retornar o quociente da divisão de dois números"""
    return n1 / n2g

try:
     num1_str = input ("Digite o primeiro número:")
     operador = input ("Digite o operador (+, -, *, /)")
     num2_str = input("Digite o segundo número:")
    
    # Verificar se os números inseridos são válidos
     if not num1_str.replace('.', '',1).isdigit() or not num2_str.replace('.','',1).isdigit():
        raise ValueError("Por favor, Insira números válidos.")
     else:
        num1 = float(num1_str)
        num2 = float(num2_str)
    
      # Verificar se o operador inserido é válido  
     if operador in ['+', '-','*', '/']:
        # Chamar função correspondente
        if operador == '+':
            resultado = adicionar( num1, num2)
        elif operador == '-':
            resultado = subtrair (num1, num2)
        elif operador == '*':
            resultado = multiplicar (num1, num2)
        elif operador == '/':
        # considerar a divisão por zero aqui
            if num2 == 0:
                raise ZeroDivisionError ("Não é possivel dividir por zero")
            else:
                resultado = dividir(num1, num2)
    
                # Exibir Resultado
                print(f"O Resultado é:{resultado}")
    
        else:
            # Exibir mensagens de erro apropiadadas.
            raise ValueError("Operador Inválido. Use +, -, ou /.")
except ValueError as e:
        print (f"Erro:{e}")
except ZeroDivisionError as e:  
        print (f'Erro:{e}')
except Exception as e:
        print(f'Ocorreu um erro inesperado:{e}')



    

