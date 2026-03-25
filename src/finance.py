def calcular(dados):
    total_gasto = 0
    total_ganho = 0

    for d in dados:
        if d["tipo"] == "gasto":
            total_gasto += d["valor"]
        else:
            total_ganho += d["valor"]

    return total_gasto, total_ganho