def ler_nome():
    """
    Pede para o usuário informar o nome e retorna uma string
    """
    return input("Informe o seu nome: ")

def ler_notas():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))
    return ap1, ap2, asub, ac

def validar_notas(ap1, ap2, ac, asub):
    if ap1 >= 0 and ap2 >= 0 and ac >= 0 and asub >= 0 and ap1 <= 10 and ap2 <= 10 and ac <= 10 and asub<= 10:
        print("Notas válidas! Prosseguindo..")
        return True
    else:
        print("Por favor insira notas válidas...")

def duas_maiores_notas(ap1, ap2, asub):
    if ap1 >= ap2 and ap1 >= asub:
        if ap2 >= asub:
            return ap1, ap2
        else:
            return ap1, asub
    elif ap2 >= ap1 and ap2 >= asub:
        if ap1 >= asub:
            return ap2, ap1
        else:
            return ap2, asub
    else:
        if ap1 >= ap2:
            return asub, ap1
        else:
            return asub, ap2

def calcular_media(n1,n2,ac):
    media = round((n1 + n2) * 0.4 + ac * 0.2, 2)
    return media




def informar_aprovacao(media):
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado")
    else:
        print("Você foi reprovado...")





def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

    # ler notas do usuário
        # se forem válidas :
        # definir as maiores notas, entre ap1, ap2 e AC
        # calcular a média
        # dizer se o aluno está aprovado ou não


main()