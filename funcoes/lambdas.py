from functools import reduce

alunos = [
    {"nome": "Joao", "nota": 7.5},
    {"nome": "Maria", "nota": 8.2},
    {"nome": "Pedro", "nota": 6.9},
    {"nome": "Ana", "nota": 9.1},
    {"nome": "Carlos", "nota": 6.8}
]

aluno_situacao = lambda aluno: aluno['nota'] >= 7

alunos_aprovados = list(filter(aluno_situacao, alunos))

print(alunos_aprovados)