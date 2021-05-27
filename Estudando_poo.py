class pessoa ():
    def __init__(self,nome,sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados(self):
        print(self.nome)
        print(self.sobrenome)
        print(self.idade)

gente = pessoa("Emily", "Alessandra", 18)        
print(vars(gente))        