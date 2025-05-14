#1 Definindo um array
frutas = []
frutas = ["laranja", "maça", "uva"]
letras = list("python")
numeros = list(range(10))

#2 Aninhamento
matriz = [
      [1, 2, "a"],
      [3, 4, "b"],
      [5, 6, "c"]
]
print(matriz[0][2])

#3 Iterar um array
for fruta in frutas:
      print(fruta)

#3.1 Iterar um array pegando o index
for index, fruta in enumerate(frutas):
      print(f"{index}: {fruta}")
      
#4 List Comprehensions
first_letra_l = [ i for i in frutas if i[0]=="l"]
print(first_letra_l)

#4.1 Sem comprehension List
# first_letra_l = []
# for fruta in frutas:
#       if fruta[0] == "l":
#             first_letra_l.append(fruta)
# print(first_letra_l)

#5 Métodos da Classe List (Array)
frutas.append("maça") #Adiciona um item a lista.
#frutas.clear() #Limpa a lista
frutas.copy() #Faz uma copia da lista, criando uma nova instancia com os mesmos valores.
contador = frutas.count("maça") #Retorna quantas vezes o argumento passado aparece na lista
frutas.extend(first_letra_l) #Adiciona itens a lista.
index = frutas.index("laranja") #Retorna o indice do item na lista. Na sua PRIMEIRA ocorrencia.
frutas.pop() #Remove itens. Seu padrão é remover sempre o ultimo (pilha), mas pode passar o index
remove = frutas.remove("maça") #Remove itens passando o nome do item, na sua primeira ocorrencia
frutas.reverse()
frutas.sort() #Ordena por padrao em ordem alfabetica, mas passando argumentos pode mudar a ordenação
ordenar = sorted(frutas) #Retorna a lista ordenada. Função Built-in
tamanho = len(frutas) #Retorna o tamanho da lista. Função Built-in
print(frutas)


