#Definindo um Conjunto
#Semelhante a Listas e Tuplas, porém os itens repetidos são excluidos
# e não acessados por index ou fatiamento, somente passando-os para []
conjunto = {1, 2, 1, 2}
conjuntos = set((1,2,3,3,4,4))
conjuntos = set(("abacaxi"))
acessando_conjuntos = list(conjunto)
print(acessando_conjuntos[0])

#Métodos de conjuntos
unindo_conjuntos = conjunto.union(conjuntos)
interseçao_conjuntos = conjunto.intersection(conjuntos)
diferenca_conjuntos = conjunto.difference(conjuntos) #Oque tem no 1 que nao tem no 2.
conjunto.add(3) #Se ja existir o numero no conjunto, o add é ignorado
#conjunto.clear()
conjunto.copy() #Igual ao das Listas, cria uma nova instancia.
conjunto.discard(4) # Discarta um valor do conjunto
conjunto.pop() #Tira o primeiro valor da sequencia e assim por diante
conjunto.remove(2) #Remove um item, mas se passar um inexistente, retorna um erro, diferente do discard()
len(conjunto)
print(3 in conjunto)