idade = int(input("Digite sua idade: "))
aulas_assistidas = int(input("Digite quantas aulas foram assistidas: "))

if idade >= 18:
      if aulas_assistidas >= 10: #If dentro de If = IF aninhado.
            print("Você pode tirar a carteira de motorista")
      else:
            print("Você não atingiu o numero de aulas exigidas.")
elif idade == 17:
      print("Você finalizou as aulas teóricas, aguarde fazer as práticas.") if aulas_assistidas >= 10 else print("Você pode fazer as aulas teóricas, e não a prática.") #IF/ELSE Ternário (Em 1 linha somente)
else:
      print("Você não tem idade para tirar carteira.")