#Exibir para o usuário: Cenário: Você é Hércules, o famoso herói grego. 
# O seu navio naufragou em uma ilha que em seu centro possui a cidade de Lerna. 
# Para chegar até lá e obter suprimentos, você precisa passar pelo monstro de 9 cabeças, a Hidra. 
# Para derrota-la será necessário força, uma arma e uma poção de cura.
#Dica: Você naufragou junto com a sua bolsa que possui um meio frasco de cura.
#Cada ataque Da hydra lhe dará uma graça (benção) dos deuses que poderá ser usado ao longo do jogo!

#Cura = remédio/medicamento
#For = ambrosia

class Tempo:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while (self.minutos >=60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

class Hercules:
    def __init__(self):
        self.forca = True
        self.cura = False
        self.graca = 0
        self.benção = 100

    def __str__(self):
        return "Você está " + ("forte" if self.forca else "fraco")+", "+("com" if self.cura else "sem")+"Cura. Você tem"+str(self.graca)+ "Graças."

    def descanso(self):
        self.forca = True
        self.cura = True
        
class Barco: 
    def __init__(self):
        self.ambrosia = 1
        self.pocao = 1

if(__name__ == "__main__"):
    dia = 1
    tempo = Tempo()
    hercules = Hercules()
    barco = Barco()
    cafe_da_manha = False
    while True:
        print("---")
        print("São "+str(tempo)+" do dia "+str(dia)+". Você tem que sair pro Combate até às 07:00")
        print(hercules)
        print("")
        print("Tarefas")
        print(" 1- Achar a ambrosia nos destroços do navio")
        print(" 2 - Tomar a ambrosia para ter força")
        print(" 3 - Afiar uma pedra para fazer a arma")
        print(" 4 - Tomar a poção de cura ")
        print(" 5 - Atacar o mostro")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            hercules.forca = True
            tempo.avancaTempo(20)
        elif(opcao == "2"):
            if(barco.ambrosia > 0):
                barco.ambrosia -= 1
                cafe_da_manha = True
            else:
                print("Não há ambrosia encontrada no barco.")
            tempo.avancaTempo(15)
        elif(opcao == "3"):
            if(hercules)   #criar atributo relacinado a arma

        elif(opcao == "4"):
            if(barco.pocao > 0):
                barco.pocao -= 1
                hercules.cura = True
            else:
                print("Não há poção encontrada no barco")
            tempo.avancaTempo(5)
        elif(opcao == "5"):
            print("Opçoes de ataque: 1 - cabeça, 2 - peito, 3 - pé :")    
            ataques = input("Qual será seu ataque?: ")  
                  





         