# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Entrada de dados
texto = input("Digite uma palavra ou frase: ")
quantidade = int(input("Digite um número inteiro: "))

# Criando uma lista com o texto repetido 'quantidade' vezes
resultado = (texto + " ") * quantidade

# Exibindo o resultado final
print("Resultado:", resultado)