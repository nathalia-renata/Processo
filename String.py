vpalavra= [] 
palavra = str(input("Digite uma palavra : "))
vpalavra.append(palavra)
print(vpalavra) #mostra as palavras digitadas
contador = 0
for letra in palavra:
    if (letra == "a") or (letra == "A"):
        contador = contador +1
print(palavra, "possui", contador, "letra(s) a(A).")