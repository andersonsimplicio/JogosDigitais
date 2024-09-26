
def particionamento_lomuto(array, inicio, fim):
    # Escolhe o pivô como o último elemento
    pivô = array[fim]
    
    # i começa uma posição antes do início do array
    i = inicio - 1
    
    # Percorre o array do início até o penúltimo elemento
    for j in range(inicio, fim):
        # Se o elemento atual for menor ou igual ao pivô
        if array[j] <= pivô:
            # Incrementa o índice i
            i += 1
            # Troca o elemento em i com o elemento em j
            # Armazena temporariamente o valor de array[i]
            temp = array[i]
            # Coloca o valor de array[j] na posição array[i]
            array[i] = array[j]
            # Coloca o valor temporário (que era de array[i]) na posição array[j]
            array[j] = temp
    
    # No final, coloca o pivô na posição correta
    # Armazena temporariamente o valor de array[i + 1]
    aux = array[i + 1]
    # Coloca o valor de array[fim] na posição array[i + 1]
    array[i + 1] = array[fim]
    # Coloca o valor temporário (que era de array[i + 1]) na posição array[fim]
    array[fim] = aux
    
    # Retorna a posição do pivô
    return i + 1

if __name__=="__main__":
    array = [3, 8, 6, 1, 7, 2, 5]
    inicio = 0
    fim = len(array)-1
    print(array)
    print(particionamento_lomuto(array,inicio,fim))
    print(array)
    