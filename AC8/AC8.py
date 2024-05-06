# AC 8

# bee 1555
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def rafael(x, y):
    return (3*x)**2 + y**2

def beto(x, y):
    return 2*(x**2) + (5*y)**2

def carlos(x, y):
    return -100*x + y**3

while True:
    try:
        N = int(input("quantos casos? ").strip())
        if N <= 0:
            print("insira um número válido.")
            continue
        break
    except ValueError:
        print("valor inválido.")

for _ in range(N):
    while True:
        try:
            x, y = map(int, input("insira os valores de x e y").strip().split())
            break
        except ValueError:
            print("valores inválidos.")

    r = rafael(x, y)
    b = beto(x, y)
    c = carlos(x, y)
    
    if r > b and r > c:
        print("Rafael ganhou")
    elif b > r and b > c:
        print("Beto ganhou")
    elif c > r and c > b:
        print("Carlos ganhou")

#bee 1329
while True:
    try:
        N = int(input())

        R = [int(x) for x in input().strip().split(' ')]
        maria, joao = 0, 0

        for jogo in R:
            if(jogo == 0):
                maria += 1
            else:
                joao += 1
        
        print(f"maria venceu {maria} vezes e joão venceu {joao} vezes!")
    except EOFError:
        break

# bee 1221
from math import sqrt
a=int(input())
p = 1
primos = [2]
for numero in range(3,a+1):
    ehprimo = 1
    for i in primos:
        if numero % i == 0:
            ehprimo = 0
            print("não é primo")
            break
        if i > sqrt(numero):
            break
    if (ehprimo):
        primos.append(numero)
        print ("é primo!")
        p += 1

#bee 1771
n = int(input())

frequencias = [0 for _ in range(2001)]

for _ in range(n):
    x = int(input())
    
    frequencias[x] += 1

for i in range(1, 2001):
    if(frequencias[i] > 0):
        print(f"{i} aparece {frequencias[i]} vez(es)")

#bee 1770
 vez = int(input())

for x in range(0,vez):
  dias = 0
  quilos = float(input())
  stop = 1

  while stop == 1:
    quilos= quilos/2
    dias+=1

    if quilos <=1:
      stop = 0

#bee 1161
m = int(input("What's the number? ")) n = int(input("What's the number? "))

if (n==0): n=1

elif (n>0 and n<=20):

  for j in range(1,n):
      n = n*j
      j = j+1

if (m==0): m=1

elif (m>0 and m<=20):

  for i in range(1,m):
      m = m*i
      i=i+1

print (m+n)

#bee 1087
while True:
    try:
        [X1, Y1, X2, Y2] = [int(x) for x in input().strip().split(' ')]

        if(X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0):
            break

        if(X1 == X2 and Y1 == Y2):
            print('0')
        elif(X1 == X2 or Y1 == Y2 or abs(X1 - X2) == abs(Y1 - Y2)):
            print('1')
        else:
            print('2')
    except EOFError:
        break

#bee 1028

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)


N = int(input())

for _ in range(N):
    F1, F2 = [int(x) for x in input().strip().split(' ')]
    print(MDC(F1, F2))