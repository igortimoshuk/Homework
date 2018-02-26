

def gauss(A, b1):
    N = len(A)
    try:
        b = []
        for i in range (N):
            b.append([i, b1[i]])
        for i in range(N):
            maxim = i
            for j in range(i, N):
                if A[j][i] > A[maxim][i]:
                    maxim = j
                    
            A[i], A[maxim] = A[maxim], A[i]
            b[i][1], b[maxim][1] = b[maxim][1], b[i][1]
            basis = A[i][i]
            
            for j in range(i, N):
                A[i][j] /= basis
            b[i][1] /= basis
            
            
            for j in range(i + 1, N):
                if A[j][i]:
                    multiply = A[j][i]
                    for k in range(i, N):
                        A[j][k] -= multiply * A[i][k]
                    b[j][1] -= multiply * b[i][1]
                      
        for i in range(N - 1, 0, -1):
            diff = b[i][1]
            for j in range(i):
                b[j][1] -= diff * A[j][i]
                A[j][i] = 0
                
        b.sort()
        for i in range(N):
            b1[i] = b[i][1]
        return A, b1
    except:
        return 'No sollution'

def print_matrix(A):
    N = len(A)
    for i in range(N):
        print(' '.join(map(str, A[i])))

N1 = 2
A1 = [[1, 2], [2, 3]]
b1 = [5, 8]

print_matrix(gauss(A1, b1)[0])
print(' '.join(map(str, gauss(A1, b1)[1])))

N2 = 3
A2 = [[1, 2, 3], [1, 3, 5], [1, 4, 8]]
b2 = [7, 10, 14]
print_matrix(gauss(A2, b2)[0])
print(' '.join(map(str, gauss(A2, b2)[1])))

N3 = 10
A3 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
b3 = [3, 3] + [2] * 8
print_matrix(gauss(A3, b3)[0])
print(' '.join(map(str, gauss(A3, b3)[1])))
