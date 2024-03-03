"""
AC1

Pedro Mynssen
02/03/2024


"""

# Exercício 1


import cmath


def funcao_quadratica(a, b, c):

    raiz = cmath.sqrt

    negative_number = -b

    delta = (b**2) - (4 * a *c) # optei por dividir tudo em etapas pra conseguir identificar erros mais facilmente
    

    sol1 = ((negative_number + raiz(delta))/(2*a))
    sol2 = ((negative_number - raiz(delta))/(2*a))
    return sol1, sol2
  
  
sol1, sol2 = funcao_quadratica(float(input("Informe o parâmetro a da equação:")),float(input("Informe o parâmetro b da equação:")),float(input("Informe o parâmetro c da equação:")) )
# Não consegui fazer o código rodar direito quando pedia o input dentro da função... desculpe pela linha desnecessariamente longa
sol1_str = str(sol1) .replace("+0j", "")
sol2_str = str(sol2) .replace("+0j", "")
print(f"As raízes são {sol1_str} e {sol2_str}")


# Exercício 2


def bi6to(ano):
    if ano % 4 == 0 :
        return True
    elif ano % 100 == 0 :
        return False
    elif ano % 400 == 0 :
        return True
    else:
        return False
    if True : 
        print ("o ano é bissexto")
    else :
        print ("o ano não é bissexto")


print(bi6to (int(input("Informe o ano: "))))
    

