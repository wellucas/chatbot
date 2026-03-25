import json

def salvar(dado):
    with open("data/dados.json", "a") as f:
        f.write(json.dumps(dado) + "\n")