'''
for i in range(10):
    print(i)
    
print('-------------------')
    
for i in range(1, 11):
    print(i)

print('-------------------')

for i in range(1, 100, 7):
    print(i)

print('-------------------')

for i in range(20, 0, -2):
    print(i)
'''

'''
nums = [2,4,6,8]

for n in nums:
    print(n)
    
for n in nums:
    print(n, end=' ') # Imprime todos na mesma linha separado por um espaco em branco
'''

'''
texto = 'Python e top'

for letra in texto:
    print(letra, end=' ')
'''

produtos = {
    '001': {'nome': 'Camiseta', 'preco': 29.99, 'estoque': 10},
    '002': {'nome': 'Calça Jeans', 'preco': 79.99, 'estoque': 5},
    '003': {'nome': 'Tênis', 'preco': 129.99, 'estoque': 3}
}

for codigo, produto in produtos.items():
    print(f"Código: {codigo}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']} unidades")
    print()
    
