# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

# Processamento
if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado da soma:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado da subtração:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado da multiplicação:", resultado)

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Operação inválida. Use apenas +, -, * ou /.")