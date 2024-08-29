
def processa_lista(lista):
    resultado = 0  # 1 operação primitiva
    max_valor = -float('inf')  # 1 operação primitiva
    min_valor = float('inf')  # 1 operação primitiva

    for item in lista:
        # 2 operações primitivas (leitura e adição)
        resultado += item  
        # 1 operação primitiva (comparação)
        max_valor = item if item > max_valor else max_valor 

    # Empacotamento dos valores em uma tupla: 1  operação primitiva.
    # Retorno da tupla: 1 operação primitiva
    return resultado, max_valor, min_valor  # 2 operações primitivas