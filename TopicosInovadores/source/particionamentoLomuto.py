def particionar_lomuto(v,esq,dir):
    pivot = v[esq]
    i = esq
    for j in range(esq+1,dir):
        if v[j] <= pivot: 
            i+=1
            v[i],v[j] = v[j],v[i]
           
    v[esq], v[i] = v[i], v[esq]

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
    
