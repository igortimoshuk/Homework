MAX_NUMBER = 4 * 10 ** 6

square_sum = 0
cube_sum = 0
a = 1
b = 1
while a + b < MAX_NUMBER:
    c = a + b
    if c % 2 == 0:
        square_sum += c ** 2
        cube_sum += c ** 3
    a = b
    b = c

print(cube_sum / square_sum)