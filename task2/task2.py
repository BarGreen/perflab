import sys

# Список координат вершин четырехугольника:
tetr = []
with open(sys.argv[1]) as inf:
    for line in inf:
        tetr += [[float(i) for i in line.strip().split()]]

# Список точек:
point = []
with open(sys.argv[2]) as inf:
    for line in inf:
        point += [[float(i) for i in line.strip().split()]]

def rotate(A, B, C):
    return (B[0] - A[0])*(C[1] - B[1]) - (B[1] - A[1])*(C[0] - B[0])

# Проверка пересечений отрезков из вершин до точки и отрезков сторон:
def intersect(A, B, C, D): 
    if rotate(A, B, C)*rotate(A, B, D) == 0 and rotate(C, D, A)*rotate(C, D, B) == 0:
        return 1
    elif rotate(A, B, C)*rotate(A, B, D) == 0 and rotate(C, D, A)*rotate(C, D, B) != 0 \
        or rotate(A, B, C)*rotate(A, B, D) != 0 and rotate(C, D, A)*rotate(C, D, B) == 0:
        return 4
    else:
        return 0

def pointloc(P, A):
    if rotate(P[0], P[1], A) > 0 or rotate(P[0], P[3], A) < 0  \
    or rotate(P[2], P[1], A) < 0 or rotate(P[2], P[3], A) > 0:
        return 3
    else:
        x = 0
        x += intersect(P[0], A, P[1], P[2])
        x += intersect(P[0], A, P[2], P[3])
        x += intersect(P[2], A, P[0], P[1])
        x += intersect(P[2], A, P[0], P[2])
        x += intersect(P[1], A, P[0], P[3])
        x += intersect(P[1], A, P[2], P[3])
        x += intersect(P[3], A, P[0], P[1])
        x += intersect(P[3], A, P[1], P[2])
        if x == 1:
            return 2
        elif x == 13 or x == 17:
            return 1
        elif x == 9 or x == 12:
            return 0

# Список ответов и вывод:                
ans = []
for i in point:
    ans += [pointloc(tetr, i)]

for j in ans:
    print(j)