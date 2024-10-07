
def particionar_Hoare(v:[]):
    j= len(v)-1
    pivot = 0
    i = 1
    while True:
      
        while v[j] <= v[pivot]:
            j-=1

        while v[i] >= v[pivot]:
            i+=1

        if i < j:
            print("troca")
            v[i], v[j] = v[j], v[i]
        else:
            v[pivot], v[j] = v[j], v[pivot]
            return j

if __name__=="__main__":
    #array = [3,8,7,10,0,23,2,1,77,7]
    array = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]
    print(array)
    print(particionar_Hoare(array))
    print(array)
