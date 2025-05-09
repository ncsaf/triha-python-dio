nome = "Nilton"
idade = 26.34
dicionario = {"nome": "Nilton", "idade": 26 }

print("Olá, meu nome é %s e tenho %d anos." % (nome,idade))

print("Olá, meu nome é {} e tenho {} anos.".format(nome,idade))
print("Olá, meu nome é {0} e tenho {1} anos.".format(nome,idade))
print("Olá, meu nome é {name} e tenho {age} anos.".format(name=nome, age=idade))
print("Olá, meu nome é {nome} e tenho {idade} anos.".format(**dicionario))

print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
print(f"Olá, meu nome é {nome} e tenho {idade:.1f} anos.")

