'''texto = input("Informe seu nome: ")
VOGAIS = "AEIOU"

for i in texto:
      if i.upper() in VOGAIS:
        print(i, end=" ")            
else: 
      print("\nAqui executa o Else")
      

for i in range(0,51,5):
     print(i, end=" ")'''

opcao = -1

while opcao != 0:
      opcao = int(input(" [1]Sacar \n [2]Extrato \n [0]Sair \n : "))

      if opcao == 1:
            continue
            print("Sacando...")
            
      elif opcao == 2:
            print("Exibindo extrato...")
            break