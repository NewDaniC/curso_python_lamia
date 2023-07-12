
class Produto:
    def __init__(self, nome, preco=1.99, desconto=0):
        self.__nome = nome #"privado"
        self.preco = preco
        self.desconto = desconto

    @property # get
    def nome(self):
        return self.__nome

    @property  # n precisa usar o () quando chamar
    def calcular_desconto(self):
        return self.preco - (self.desconto * self.preco)


p1 = Produto('Caneta', 5.99, 0.1)
p2 = Produto('Caderno', 12.99, 0.2)

print(p1.nome, p1.preco)
print("Preço com desconto:", p1.calcular_desconto)

print(p2.nome, p2.preco)
print("Preço com desconto:", p2.calcular_desconto)


'''
class Produto:
    def __init__(self, nome, preco=1.99):
        self.nome = nome
        self.preco = preco

p1 = Produto('Caneta')
p2 = Produto('Caderno')

print(p1.nome, p1.preco)
print(p2.nome, p2.preco)
'''
