def soma(a, b):
    return a + b

somar = soma
print(somar(3, 4))


def somar_e_imprimir(funcao, elemento1, elemento2):
    resultado = funcao(elemento1, elemento2)
    print(resultado)
    return resultado

resultado = somar_e_imprimir(soma, 2, 3)
