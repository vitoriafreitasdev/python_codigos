
musicas = [
    {"id": 1, "titulo": "Bohemian Rhapsody", "artista": "Queen", 
     "duracao": 354, "genero": "rock", "plays": 1500000},
    {"id": 2, "titulo": "Blinding Lights", "artista": "The Weeknd", 
     "duracao": 200, "genero": "pop", "plays": 2800000},
    {"id": 3, "titulo": "Smooth Criminal", "artista": "Michael Jackson", 
     "duracao": 258, "genero": "pop", "plays": 1900000},
    {"id": 4, "titulo": "Stairway to Heaven", "artista": "Led Zeppelin", 
     "duracao": 482, "genero": "rock", "plays": 1200000},
    {"id": 5, "titulo": "HUMBLE.", "artista": "Kendrick Lamar", 
     "duracao": 177, "genero": "hip-hop", "plays": 2100000},
    {"id": 6, "titulo": "Billie Jean", "artista": "Michael Jackson", 
     "duracao": 294, "genero": "pop", "plays": 2500000},
    {"id": 7, "titulo": "Smells Like Teen Spirit", "artista": "Nirvana", 
     "duracao": 301, "genero": "rock", "plays": 1800000}
]

"""
1
Mapeamento simples:
Crie um dicionário onde as chaves são os ids das músicas e os valores são os titulos.
"""
dict1 = {value["id"]:value["titulo"] for key, value in enumerate(musicas)}
print(dict1)

"""
2
Filtro por gênero:
Crie um dicionário com músicas do gênero "rock", onde a chave é o id e o valor é um dicionário com titulo e artista.
"""
dict2 = {value["id"]:{"titulo": value["titulo"], "artista": value["artista"]} for key, value in enumerate(musicas) if value["genero"] == "rock"}
print(dict2)

"""
3
Transformação de valores:
Crie um dicionário onde a chave é o titulo e o valor é a duração em minutos (duração original está em segundos, converta para minutos com 2 casas decimais).
"""
dict3 = {value["titulo"]:round(value["plays"]/60, 2) for key, value in enumerate(musicas)}
print(dict3)
#continuar

"""
4
Condicional complexo:
Crie um dicionário onde a chave é o artista e o valor é uma lista de títulos daquele artista. Dica: você pode precisar de um dicionário regular como passo intermediário.
"""
dict4 = {value['artista']:[m["titulo"] for i, m in enumerate(musicas) if m["artista"] == value["artista"]] for key, value in enumerate(musicas)}
print(dict4)
"""
5
Agregação com condição:
Crie um dicionário onde a chave é o genero e o valor é a média de plays das músicas daquele gênero (arredonde para inteiro).
"""
dict5 = {value["genero"]:[v["plays"] for k, v in enumerate(musicas) if v["genero"] == value["genero"]] for key, value in enumerate(musicas)}

for v in dict5:
    total = 0
    for i in dict5[v]:
        total += i 
    dict5[v] = round(total / len(dict5[v]))

print(dict5)

"""
6
Chave composta:
Crie um dicionário onde a chave é uma tupla (artista, genero) e o valor é a quantidade de músicas que aquele artista tem naquele gênero.
"""
newDict = {}
for v in musicas:
    if v["artista"] not in newDict:
        newDict[v["artista"]] = 0
    newDict[v["artista"]] += 1

total_mus = {}
for v in musicas:
    if v["artista"] not in total_mus:
        total_mus[(v["artista"], v["genero"])] = newDict[v["artista"]]

#print(total_mus)

# Primeiro: criar um dicionário para contar
contagem = {}
for musica in musicas:
    chave = (musica["artista"], musica["genero"])
    contagem[chave] = contagem.get(chave, 0) + 1
#print(contagem)

# Se quiser em formato de comprehension:
resultado = {chave: valor for chave, valor in contagem.items()}
print(resultado)

"""
7
Transformação aninhada:
Crie um dicionário onde a chave é o id e o valor é um dicionário com:
classificacao: "hit" se plays > 2.000.000, "popular" se plays > 1.500.000, "regular" caso contrário
duracao_min: duração em minutos (1 casa decimal)
"""

dictFinal = {value["id"]:{"hit" if value["plays"] > 2000000 else "popular" if value["plays"] == "entregue" else "regular" for k, v in enumerate(musicas)} for key, value in enumerate(musicas)}

print(dictFinal)