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

      def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
      
      def __del__(self):
            print("Removendo a instancia da memoria")

bike1 = Bicicleta("Preta","Monark",1999, 100)
# bike1.buzinar()
# bike1.correr()
# bike1.parar()
print(bike1)

#Bicicleta.buzinar(bike1)

