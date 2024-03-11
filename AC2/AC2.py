import cmath
def main():
    resultado_quadratica()
    confirm_bi6to()
    informar_salario()
def funcao_quadratica():
    a = float(input("Informe o parâmetro a: "))
    b = float(input("Informe o parâmetro b: "))
    c = float(input("Informe o parâmetro c: "))
    raiz = cmath.sqrt

    negative_number = -b
    delta = (b**2) - (4 * a * c)

    SOL1 = ((negative_number + raiz(delta))/(2*a))
    SOL2 = ((negative_number - raiz(delta))/(2*a))
    return SOL1, SOL2

def resultado_quadratica():
    SOL1, SOL2 = funcao_quadratica()
    sol1_str = str(SOL1) .replace("+0j", "")
    sol2_str = str(SOL2) .replace("+0j", "")
    print(f"As raízes são {sol1_str} e {sol2_str}")

# Exercício 2

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

def confirm_bi6to():
    ano = float(input("Informe um ano: "))
    if bissexto(ano):
        mensagem = f"{ano} é bissexto"
    else:
        mensagem = f"{ano} não é bissexto"
    print(mensagem)



#Exercício 2
def calcula_salario(irpf=0.275):
    valor_hora = float(input("Informe o valor por hora:"))
    qtd_horas = float(input("Informe a quantidade de horas que você trabalha: "))
    salario_bruto = valor_hora * qtd_horas
    salario_liquido = salario_bruto * (1 - irpf)
    return salario_liquido

def informar_salario():
    salario_liquido = calcula_salario()
    print(f"Seu salário líquido será de R$ {salario_liquido:.2f}")


main()
