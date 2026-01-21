import os
current_dir = os.path.dirname(os.path.abspath(__file__))
poem = os.path.join(current_dir, "poem.txt")
newHash = {}

with open(poem, "r") as f:
    for line in f:
        tokens = line.split(" ")
        for token in tokens:
            token=token.replace('\n','')
            if token not in newHash:
                newHash[token] = 1
            else:
                count = newHash[token] 
                newHash[token] = count + 1

print(newHash)
#ver se ta certo
# dictnary = {}
# dictnary["n"] = 1
# print(dictnary["n"])