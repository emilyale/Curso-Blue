class Ingresso:
    def __init__(self,valor):
      self.valor=valor

    def imprimirValor(self):
      print(f"O valor do ingresso é : \nR${self.valor}")  

class IngressoVip(Ingresso):
 def __init__(self, valor, adicional):
     super().__init__(valor)
     self.adicional= adicional    
 def valorVip(self):
     print(self.valor + self.adicional)
     return self.valor + self.adicional
ingresso=IngressoVip(19,10)
ingresso.imprimirValor()
print(ingresso.valorVip())
