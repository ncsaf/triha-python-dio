class Bicicleta:
      def __init__(self, cor, marca, ano, valor):
            self.cor = cor
            self.marca = marca
            self.ano = ano
            self.valor = valor

      def buzinar(self):
            print("Plim Plim")

      def parar(self):
            print("Bicicleta parando")

      def correr(self):
            print("Bicicleta andando")

bike1 = Bicicleta("Preta","Monark",1999, 100)
bike1.buzinar()
bike1.correr()
bike1.parar()
print(bike1.ano, bike1.cor, bike1.marca)

Bicicleta.buzinar(bike1)

