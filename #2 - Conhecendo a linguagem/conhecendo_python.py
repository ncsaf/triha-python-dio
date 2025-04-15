'''
1 Tipos de dados
 int - inteiro
bool - boleano
str - string
float - racionais

print("Este é um número Inteiro: 10")
print("Este é um número float: +10.5")
print("Este é um número Bool: True")
print("Isto é uma String"+" Ola")


2 Modo Interativo
Digitar python no console abre o modo interativo
python -i nome_do_arquivo.py -> roda o arquivo no terminal
help ou help() -> Ajuda sobre algum objeto
dir() ou dir -> lista os diretorios do projeto ou de um objeto

3 Variaveis e Constantes
age = 26
name = "Nilton"

age, name = 27 , "Cesar"
VARIAVEL_CONSTANTE = "Não nativa do python, convensão usada: Maiuscula e snake_case"

print(VARIAVEL_CONSTANTE,age,name) 

4 Conversão de Tipos de dados
'''
preco = 10.40
idade = 21
texto = "20"

print(float(21))
print(int(preco))
print(type(float(texto))) #type() retorna o tipo de dado daquela variável
print(100/2) #Retorna a divisão com ponto flutuante
print(100//2) #Retorna a divisão somente com parte inteira
