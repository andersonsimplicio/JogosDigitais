class Node:
    def __init__(self,data:int) -> None:
        self.data = data
        self.no_direito:Node = None
        self.no_esquerdo:Node = None

def Em_ordem(nodo:Node)->None:
    
    if nodo is None:
       return 
    else:
        Em_ordem(nodo.no_esquerdo)
        print(nodo.data)
        Em_ordem(nodo.no_direito)
    
class Tree: 

    def __init__(self):
        self.raiz:Node = None

    def insercao(self,valor:int)->None:
        nodo = Node(valor)
        if self.raiz is None:
            self.raiz = nodo
        
        nodo_corrente = self.raiz
        saida = True    
        while saida:
            print(nodo_corrente.data)
            print(nodo.data)
            if nodo.data < nodo_corrente.data:
                if nodo_corrente.no_esquerdo is None:
                    nodo_corrente.no_esquerdo = nodo
                    saida = False
                else:
                    nodo_corrente = nodo_corrente.no_esquerdo
            else:
               if nodo_corrente.no_direito is None:
                    nodo_corrente.no_direito = nodo
                    saida = False
               else:
                    nodo_corrente = nodo_corrente.no_direito
       
        nodo_corrente = nodo
    
    def search(self,value:int)->int | None:
        pointer = self.raiz
        while pointer is not None:
            if pointer.data == value:
                return pointer.data
            elif pointer.data > value:
                pointer = pointer.no_direito
            else:
                pointer = pointer.no_direito
        return None
    
if __name__ == "__main__":
   
    bst = Tree()
    bst.insercao(7)
    bst.insercao(3)
    bst.insercao(9)
    bst.insercao(1)
    bst.insercao(5)

    print(f"Em ordem: raiz {bst.raiz.data}",)
    Em_ordem(bst.raiz)
    print(f"Buscar 7: {bst.search(7)} {' encontrado!' if bst.search(7) is not None else ' não encotrado!'}" )
    print(f"Buscar 3: {bst.search(3)} {' encontrado!' if bst.search(3) is not None else ' não encotrado!'}" )
    print(f"Buscar 9: {bst.search(9)} {' encontrado!' if bst.search(9) is not None else ' não encotrado!'}" )
    print(f"Buscar 1: {bst.search(1)} {' encontrado!' if bst.search(1) is not None else ' não encotrado!'}" )
    print(f"Buscar 5: {bst.search(5)} {' encontrado!' if bst.search(5) is not None else ' não encotrado!'}" )
   