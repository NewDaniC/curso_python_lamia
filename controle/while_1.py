limite = 5
contador = 0

while contador < limite:
    print(f"Contador: {contador}")
    contador += 1

print()

resposta = ""
contador = 0

while resposta != "1":
    resposta = input("Digite 1 para sair: ")
    contador += 1

print(f"Loop encerrado! O loop foi executado {contador} vezes.")

contador = 0
soma = 0
nota = 0

while nota != -1:
    nota = float(input("Digite a nota do aluno (-1 para sair): "))

    if nota != -1:
        soma += nota
        contador += 1

media = soma / contador

print(f"A média dos alunos é: {media:.2f}")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()

for numero in numeros:
    if numero % 2 == 0:
        continue #break - sai do laco
    print(numero)
