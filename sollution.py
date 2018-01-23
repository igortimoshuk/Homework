def sollution1(b, c):
    D = b ** 2 - 4 * c
    if b >= 0:
        x1 = (-b - D ** 0.5) / 2
        x2 = c / x1
    else:
        x1 = (-b + D ** 0.5) / 2
        x2 = c / x1        
    return x1, x2

def sollution2(b, c):
    if (4 * c / b ** 2) ** 3 / 8 < 10 ** (-13):
        x1 = - b
        x2 = - c / b - (4 * c / b) ** 2 / 16
        print(1)
    else:
        D = b ** 2 - 4 * c
        x1 = (- b + D ** 0.5) / 2
        x2 = (- b - D ** 0.5) / 2
    return x1, x2

b = 0.5 #4.0 2.0 0.5 10 ** 20 -10 ** 20
c = 5.0 #3.0 1.0 4.0 3 4

#b, c = map(float, input().split())

print(' '.join(map(str, sollution1(b, c))))
print(' '.join(map(str, sollution2(b, c))))