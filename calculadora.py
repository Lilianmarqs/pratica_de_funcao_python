menu ="""
[a] Adição 
[s] Subtração
[m] Multiplicação
[d] Divisão
[b] Sair
 """
print("Escolha uma operação: ")

def soma(a, b): 
    return a + b 

def subtracao(a, b): 
    return a - b

def multiplicacao(a, b): 
    return a * b

def divisao(a, b):
    if b != 0: 
        return a / b 
    else:
        return "Operação inválida! Divisão por zero não é permitida."
        
while True:
    opcao = input(menu)

    if opcao == "a": 
        num1 = float(input("digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado_soma = soma(num1, num2)
        print(f"\nO resultado da operação é: ", resultado_soma)

    elif opcao == "s": 
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado_subtracao = subtracao(num1, num2)
        print(f"\nO resultado da operação é ", resultado_subtracao)

    elif opcao == "m": 
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado_multiplicacao = multiplicacao(num1, num2)
        print(f"\nO resultado da operação é ", resultado_multiplicacao)

    elif opcao == "d":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado_divisao = divisao(num1, num2)
        print(f"\nO resultado da operação é ", resultado_divisao)

    elif opcao == "b": 
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida! Por favor digite uma opção válida.")
  

        
