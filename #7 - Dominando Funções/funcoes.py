#1 Definição
def nome_funcao():
      print("Ola mundo")

def com_parametros(nome):
      print(f'Olá {nome}')

def com_parametro_definido(nome='Nilton'):
      print(f'Olá {nome}')

# nome_funcao()
# com_parametros('nilton')
# com_parametro_definido('Junho')

#2 Retorno da função
def calcular_total(numeros):
      return sum(numeros)

# print(calcular_total([10,20,30]))

def retorna_antecessor_sucessor(numero):
      antecessor= numero -1
      sucessor = numero +1
      return antecessor, sucessor

# print(retorna_antecessor_sucessor(10))

def retorno_padrao(): #Sem return na função, ele retorna por padrao None
      print("Olá mundo!")

# print(retorno_padrao())

#3 Argumentos Nomeados/Posicionados
def salvar_carro(*,marca, modelo, ano, placa):
      print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

# salvar_carro("palio","fiat", 1999, "ABC-1234")
# salvar_carro(modelo="palio",marca="fiat", ano=1999, placa="ABC-1234")
salvar_carro("Fiat","palio") #Passando o parametro como dicionario, evitando que aconteça erros na troca de ordens dos parametros ou mudança de nome dos mesmos.