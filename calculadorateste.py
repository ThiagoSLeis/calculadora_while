# Calculadora com while

while True:
    # Recolhendo dados do usuário.
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    # Validando os dados do usuário.
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    # Operadores
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    # Operações matemáticas
    
    # ADIÇÃO
    if operador == '+':
        print(num_1_float + num_2_float)
    # SUBTRAÇÃO    
    elif operador == '-':
        print(num_1_float - num_2_float) 
    # MULTIPLICAÇÃO      
    elif operador == '*':
        print(num_1_float * num_2_float) 
    # DIVISÃO       
    elif operador == '/':
        if numero_2 == '0':
            print('Não é possível a divisão por zero.')
        else:
            print(num_1_float / num_2_float)
        
    # Saindo da aplicação
    sair = input('Você quer sair ? (s/n): ').lower().startswith('s')
    if sair:
        print('Você saiu da calculadora')
        break
