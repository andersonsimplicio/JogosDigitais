def particionamento_lomuto(v):
    i = j = 0
    pivot = len(v)-1
    for j in range(len(v)-1):
        if v[j] <= v[pivot]: 
            v[i],v[j] = v[j],v[i]
            i+=1
    v[pivot],v[i] = v[i],v[pivot]
    return i


if __name__=="__main__":
    v = [3,8,10,0,23,2,1,77,7]
    print(v)
    posicao = particionamento_lomuto(v)
    print(f"Pivo {posicao}  posição v[{posicao}] = {v[posicao]}")
    print(v)
    v =  [3, 8, 6, 1, 7, 2, 5]
    posicao = particionamento_lomuto(v)
    print(f"Pivo {posicao}  posição v[{posicao}] = {v[posicao]}")
    print(v)
    
