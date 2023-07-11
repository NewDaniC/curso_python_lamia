nota = float(input("Digite a nota do aluno: "))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9.5 and comportado:
    print("O aluno passou com honras!")
elif nota >= 7.0:
    print("O aluno passou!")
else:
    print("O aluno foi reprovado.")
    
print(nota)
