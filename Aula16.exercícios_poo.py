#Exercício3
class pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def envelhecer(self, idade):
        self.idade += idade

    def crescer(self, altura):
        self.altura += altura                

a = pessoa("Emily",18,59,1.59)    
print(vars(a))    
a.crescer(0.5)
print(f"A nova altura da {a.nome} é {a.altura}")