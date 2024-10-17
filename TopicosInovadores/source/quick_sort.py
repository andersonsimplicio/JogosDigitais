
def quick_sort(arr,esq:int,dir:int):
    if esq < dir:
        p = particionar_lomuto(arr,esq,dir)    
        quick_sort(arr,esq,p-1)
        quick_sort(arr,p+1,dir)
        print(f"Pivot {arr[p-1]}")
