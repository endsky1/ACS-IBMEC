# Exercício 1

def determina_tipo_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "Não é um triângulo"
    
    elif lado1 == lado2 == lado3 :
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isócseles"
    else:
        return "Escaleno"
   
      
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo   






# Exercício 2

def dia_da_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "Número de dia inválido"

def testa_dia_semana():
    print(dia_da_semana(2)) # segunda-feira
    print(dia_da_semana(6)) # sexta-feira
    print(dia_da_semana(7)) # sábado
    print(dia_da_semana(9)) # string vazia



#  Exercício 3

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não está definida.")
    return a / b

def cli():

    while True:

        try:

            num1 = float(input("Insira o primeiro número: "))

            num2 = float(input("Insira o segundo número: "))

            operacao = input("Insira a operação (+, -, *, /): ")


            if operacao == "+":

                print(f"{num1} + {num2} = {soma(num1, num2)}")

            elif operacao == "-":

                print(f"{num1} - {num2} = {subtracao(num1, num2)}")

            elif operacao == "*":

                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

            elif operacao == "/":

                print(f"{num1} / {num2} = {divisao(num1, num2)}")

            else:

                print("Operação inválida.")

            break

        except ValueError as e:

            print(e)


if __name__ == "__main__":

    cli()


def main():
    testa_triangulo()
    testa_dia_semana()
    cli()


main()
    

