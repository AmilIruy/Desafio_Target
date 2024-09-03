# Resposta 1) Ao final do processamento, qual será o valor da variável SOMA? 91

n = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))
a = 0
p = 1

found = False

while a <= n:
    if a == n:
        found = True
        break
    s = p + a
    a = p
    p = s

if found:
    print(f"O número {n} está na sequência de Fibonacci.")
else:
    print(f"O número {n} não está na sequência de Fibonacci.")

