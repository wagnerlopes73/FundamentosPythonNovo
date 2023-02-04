# Testando uma string
a = "Wagner Lopes"
print(a)

# Testando uma string
a = "João Carlos \nAna Clara \nWagner Lopes"
print(a)

s = "Data Science Academy"
print(s)

# Indexação - Apenas o primeiro caractere da string
# Em Python a idenxação começa com 0
s1 = s[0]
print(s1)

# Indexação - Apenas o primeiro caractere da string
# Em Python a idenxação começa com 0
s2 = s[1]
print(s2)

# Tudo a partir do índice 1
s3 = s[1:]
print(s3)

# Entre os índices 6 e 9
# slicing
# valor depois do ":" é EXCLUSIVO, ou seja, não entra no retorno
s4 = s[6:9]
print(s4)

# também podemos indexar de trás para frente
s5 = s[-1]
print(s5)

# retorna tudo menos a última letra
s6 = s[:-1]
print(s6)

# fatiar usando indexação saltando de 2 em 2
s7 = s[::2]
print(s7)

# podemos ainda manipular de trás para frente
s8 = s[::-1]
print(s8)

# criar repetição
letra1 = "w"
letra2 = letra1 * 3
print(letra2)

# Funções BUILT-IN de Strings

# Upper Case
s9 = s.upper()
print(s9)

# Lower Case
s10 = s.lower()
print(s10)

# Primeira letra em Maiúsculo
s11 = s.capitalize()
print(s11)

# Primeira letra maiúscula de cada palavra
s12 = s.title()
print(s12)


# Orientado a objetos com métodos e atributos
# Dividir a string pelos espaços em branco, criando uma lista
s13 = s.split()
print(s13)

# Dividir a atring por um elemento específico, ou seja, retira esse valor da string
s14 = s.split("a")
print(s14)



