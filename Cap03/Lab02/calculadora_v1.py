# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

def calculatorFunc():
    
    print('Operações disponíveis: \n1- soma \n2- subtração \n3- multiplĩcação \n4- divisão')

    inpt = int(input('Selecione o número da operação que deseja realizar: 1/2/3/4 => '))
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    def calc(x, y): 
        if (inpt == 1):
            result = x + y
            print('%s + %s = %s' %(x, y, result))
        elif (inpt == 2):
            result = x - y
            print('%s - %s = %s' %(x, y, result))
        elif (inpt == 3):
            result = x * y
            print('%s x %s = %s' %(x, y, result))
        elif (inpt == 4):
            result = x / y
            print('%s / %s = %s' %(x, y, result))
        elif (input > 4):
            print('número de operação inválido. Try again')

    calc(num1, num2)
    
    again = input('Deseja fazer outra operação? y/n: ')
    if again == 'y':
        calculatorFunc()
    elif again == 'n':
        exit()
        
        
calculatorFunc()


