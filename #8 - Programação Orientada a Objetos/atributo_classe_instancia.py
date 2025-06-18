class Estudante:
      escola = "Pthon"

      def __init__(self, nome, matricula):
            self.nome = nome
            self.matricula = matricula

      def __str__(self):
            return f"{self.nome} - {self.matricula} - {self.escola}"
      
aluno_1 = Estudante("Nilton", 1)
aluno_2 = Estudante("Cesar", 2)

Estudante.escola = "Dio"
aluno_1.escola = "NAda"

print(aluno_1)
print(aluno_2)