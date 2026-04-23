# Calculadora simples

# Pedindo os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pedindo a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Verificando qual operação foi escolhida
if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"

else:
    resultado = "Operação inválida"

# Mostrando o resultado
print("Resultado:", resultado)