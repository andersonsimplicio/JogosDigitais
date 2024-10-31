def particionamento_lomuto(lista, inicio, fim):
    pivô = lista[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if lista[j] < pivô:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    # Complete a linha abaixo
    # Troque o pivô para a posição correta
    lista[i + 1], lista[___] = lista[___], lista[i + 1]
    
    return i + 1


