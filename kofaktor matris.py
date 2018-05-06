import random

def minorMatris(matris, i, j):
    return [row[:j] + row[j+1:] for row in (matris[:i]+matris[i+1:])]

def detMatris(matris):
    if len(matris) == 2:
        return matris[0][0]*matris[1][1]-matris[0][1]*matris[1][0]
    
    det = 0
    for i in range(len(matris)):
        det += ((-1)**i)*matris[0][i]*detMatris(minorMatris(matris, 0, i))
    return det

def randomMatris(i, j):
    matris = [[random.randint(0, 9) for a in range(i)] for b in range(j)]
    return matris

s = int(input("Boyut belirtin: "))
matris = randomMatris(s, s)

print("Matris: {}".format(matris))

print("Kofaktörle hesaplanmış determinant: {}".format(detMatris(matris)))
