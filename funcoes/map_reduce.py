from functools import reduce

def mais_um_meio(nota):
    return nota + 1.5

notas = [6.4, 7.2, 5.8, 8.4]

notas_finais = list(map(mais_um_meio, notas)) #cria uma nova lista e soma 1.5 em cada nota final
print(notas_finais)

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0)
print(total)

'''
for i, nota in enumerate(notas):
    #print(i, nota)
    notas[i] = nota + 1.5
    
print(notas)
'''
