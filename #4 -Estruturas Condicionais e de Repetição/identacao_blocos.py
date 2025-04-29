# A abertura e fechamento de blocos no python
# é feito pela identação.

# o simbolo : define o inicio do bloco
# Mas o fechamento é definido pelo "recuo de margem"
# Se tiver código recuado, significa que esta dentro do bloco
# Senão tiver, significa que acabou o bloco.

def sacar (valor): # Identação OK
      saldo = 500
      if saldo >= valor:
            print("Valor sacado")

sacar(100)

# def sacar (valor): # Erro de identação (NÃO RODA) 
# saldo = 500
# if saldo >= valor:
# print("Valor sacado")

# sacar(100)