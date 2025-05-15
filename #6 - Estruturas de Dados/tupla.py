#Definindo uma Tupla
#Irmã da Lista, mas com a principal diferença da lista
# ser mutável, enquanto a tupla é imutável, nao muda.

tupla = ("laranja", "uva", "pera",) #Usa-se ',' para diferenciar do uso tradicional dos parênteses.
letras = tuple("Python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)
l,u,p = tupla #Desempacotando cada item da tupla.
print(l)

#Métodos das Tuplas
tupla.count("laranja")
tupla.index("laranja")
len(tupla)