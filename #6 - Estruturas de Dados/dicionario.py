#Definindo um Dict
pessoa = {
     "Pai":{"nome":"Nilton", "idade":26},
      "Filha":{"nome":"Cecilia", "idade":1},
      }
pessoa_2= dict(nome="Cesar", idade=26)
pessoa["Pai"]["telefone"]= "(98) 9 8910-3793"
print(pessoa["Pai"])

#Métodos do Dict
#pessoa_2.clear()
#pessoa_2.copy()
new_key = pessoa_2.fromkeys(["telefone", "endereco"], "valor") #Add novas chaves ao dicionario
get_value = pessoa_2.get("endereco", "Nao achei")# Busca a chave que passamos, se nao existir, retorna none ou o 2 args
return_itens = pessoa_2.items() #Retorna uma Lista com os itens do dicionario. Usado para iterar dict com for
pessoa_2.keys()#Retorna uma lista contendo somente as chaves do dict
pessoa_2.pop("telefone", "nao achei") #Remove a chave que voce passar, caso nao encontre, o 2 args será retornado.
pessoa_2.popitem() #Remove item a item, porém dá KeyError quando tiver vazio o dict
pessoa_2.setdefault("telefone","(98 9 8910-3793)") #Add uma nova chave somente se ela nao existir ainda.
pessoa_2.update({"primeiro_nome":"Nilton"}) #Atualiza a chave que foi passada, mas se nao existir, ele adiciona.
values = pessoa_2.values()# Retorna somente os valores do dict
has_value = "Cesar" in pessoa_2["nome"]
del pessoa_2["primeiro_nome"]
print(pessoa_2)