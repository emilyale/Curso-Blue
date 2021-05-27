# class aluno:
#     def __init__(self,nome,classe,media):
#         self.nome = nome
#         self.classe = classe
#         self.media = media
#         self.escola = "Blue"
#     # Criando os atributos fora do construtor (não uso self)
#     # nome = "" 
#     # classe = ""
#     # media = 0

# gustavo = aluno("Gustavo","3AM",7)
# print(gustavo.nome)
# pedro = aluno("Pedro","2AM",8)
# print(pedro.nome)
# print(pedro.classe)

# nome = input("Digite o nome do aluno: ")
# classe = input("Digite a classe do aluno: ")
# media = int(input("Digite a média do aluno: "))
# aluno_novo = aluno(nome,classe,media)
# print(vars(aluno_novo))


#2
class funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.salario = 0
        self.horas_trabalhadas = 0

    def registra_hora_trabalhada(self):
         self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada

a = funcionario("Emily","Analista",100)
print(f"Salario atual: {a.salario}")
print(f"Horas trabalhadas: {a.horas_trabalhadas}")
print()
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas:"))

a.registra_hora_trabalhada()
a.calcula_salario()
print(f"Salario atual: {a.salario}")
print(f"Horas trabalhadas: {a.horas_trabalhadas}")

       

