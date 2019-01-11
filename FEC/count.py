def count(imB,imA):
    ile = 0
    for i in range(len(imA)):
        if(imB[i]!=imA[i]):
            ile = ile + 1

    return ile