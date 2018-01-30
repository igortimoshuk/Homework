EPS = 2 * 10 ** (-16) 


def sollution1(b, c): #Wieth theorem
    D = b ** 2 - 4 * c
    if b > 0:
        x1 = (-b - D ** 0.5) / 2
        x2 = c / x1
    elif b < 0:
        x1 = (-b + D ** 0.5) / 2
        x2 = c / x1 
    else:
        x1, x2 = c ** 0.5, c ** 0.5
    return x1, x2

def sollution2(b, c): #Taylor series
    if b:
        if (4 * c / b ** 2) ** 4 / 32 < EPS:
            x1 =  - c / b - (4 * c / b ** 2) ** 2 / 16 * b - (4 * c / b ** 2) ** 3 / 32 * b
            x2 = - b - x1
        else:
            D = b ** 2 - 4 * c
            x1 = (- b + D ** 0.5) / 2
            x2 = (- b - D ** 0.5) / 2
    else:
        x1, x2 = c ** 0.5, c ** 0.5        
    return x1, x2

b = 4.0 #2.0 0.5 10 ** 20 -10 ** 20
c = 3.0 #1.0 4.0 3 4

#b, c = map(float, input().split())

print(' '.join(map(str, sollution1(b, c))))
print(' '.join(map(str, sollution2(b, c))))