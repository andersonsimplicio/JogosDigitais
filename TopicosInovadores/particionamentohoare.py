def particionamento_hoare(array, inicio, fim):
    # Escolhe o pivô como o primeiro elemento
    pivô = array[inicio]
    
    # Inicializa os ponteiros
    i = inicio - 1
    j = fim + 1
    
    while True:
        # Move o ponteiro i para a direita até encontrar um valor maior ou igual ao pivô
        while True:
            i += 1
            if array[i] >= pivô:
                break
        
        # Move o ponteiro j para a esquerda até encontrar um valor menor ou igual ao pivô
        while True:
            j -= 1
            if array[j] <= pivô:
                break
        
        # Se os ponteiros se cruzarem, retorne j
        if i >= j:
            return j
        
        # Caso contrário, troque os elementos de array[i] e array[j]
        # Armazena temporariamente o valor de array[i]
        aux = array[i]
        # Coloca o valor de array[j] na posição array[i]
        array[i] = array[j]
        # Coloca o valor temporário (que era de array[i]) na posição array[j]
        array[j] = aux 
        
if __name__=="__main__":
    array = [8, 3, 6, 1, 7, 2, 5]
    inicio = 0
    fim = len(array)-1
    print(array)
    print(particionamento_hoare(array,inicio,fim))
    print(array)