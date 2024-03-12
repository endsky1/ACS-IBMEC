"""
AC5

"""
import random

def main():
    # statius  iniciais do aventureiro e do monstro
    vida_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    # exibição dos status do herói
    print("Atributos do aventureiro:")
    print("Vida: " + str(vida_aventureiro))
    print("Ataque: " + str(ataque_aventureiro))
    print("Defesa: " + str(defesa_aventureiro))

    # exibição dos status iniciais do monstro
    print("Atributos do monstro:")
    print("Vida: " + str(vida_monstro))
    print("Ataque: " + str(ataque_monstro))

    # Loop do combate
    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("Rodada " + str(rodada) + ":")

        # Ataque do aventureiro
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano_aventureiro
        print("O aventureiro ataca o monstro, causando " + str(dano_aventureiro) + " de dano.")

        # Verificar se o monstro morreu
        if vida_monstro <= 0:
            print("O monstro morreu.")
            break

        # Ataque do monstro
        dano_monstro = random.randint(1, ataque_monstro - defesa_aventureiro)
        vida_aventureiro -= dano_monstro
        print("O monstro ataca o aventureiro, causando " + str(dano_monstro) + " de dano.")

        # Verificar se o aventureiro morreu
        if vida_aventureiro <= 0:
            print("O aventureiro morreu.")
            break

        rodada += 1


if __name__ == "_main_":
    main()
import random

def main():

    vida_aventureiro = 100
     ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)


    print("Atributos do aventureiro:")
    print("Vida: " + str(vida_aventureiro))
    print("Ataque: " + str(ataque_aventureiro))
    print("Defesa: " + str(defesa_aventureiro))


    print("Atributos do monstro:")
    print("Vida: " + str(vida_monstro))
    print("Ataque: " + str(ataque_monstro))


    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print("Rodada " + str(rodada) + ":")
        dano_aventureiro = random.randint(1, ataque_aventureiro)
        vida_monstro -= dano_aventureiro
        print("O aventureiro ataca o monstro, causando " + str(dano_aventureiro) + " de dano.")


        if vida_monstro <= 0:
            print("O monstro morreu.")
            break


        dano_monstro = random.randint(1, ataque_monstro - defesa_aventureiro)
        vida_aventureiro -= dano_monstro
        print("O monstro ataca o aventureiro, causando " + str(dano_monstro) + " de dano.")


        if vida_aventureiro <= 0:
            print("O aventureiro morreu.")
            break

        rodada += 1

main()