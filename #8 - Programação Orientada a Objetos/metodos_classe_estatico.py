class Pessoa:
      def __init__(self,nome,idade):
            self.nome = nome
            self.idade = idade

      @classmethod
      def criar_de_data_nascimento(cls, ano, mes, dia, nome):
            idade = 2025 - ano
            return cls(nome,idade)
      
      @staticmethod
      def e_maior_idade(idade):
            return idade >= 18

p = Pessoa("Nilton", 26)
print(p.nome,p.idade)

p1 = Pessoa.criar_de_data_nascimento(1999, 2, 8,"Nilton")
print (p1.nome, p1.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))