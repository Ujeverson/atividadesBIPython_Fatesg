reverso = lambda s: s[::-1]
print(reverso("\n Ujeverson \n"))


nome = "Ujeverson"

print(len(nome))

cincoPrimeiros = lambda s: s[:5]
print(cincoPrimeiros(nome))

cincoPrimeiros_2 = lambda s: s[1:6]
print(cincoPrimeiros_2(nome))

cincoUltimos = lambda s: s[-5:]
print(cincoUltimos(nome))

cincoPrimeiros_3 = lambda s: s[0:6:2]
print(cincoPrimeiros_3(nome))


