MAX_NUMBER = 4 * 10 ** 6

square_sum = 0 #The first way
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
    
numbers = [1, 1] #The second way
while numbers[-1] + numbers[-2] < MAX_NUMBER:
    numbers.append(numbers[-1] + numbers[-2])

square_list_sum = sum([element ** 2 for element in numbers[2::3]])
cube_list_sum = sum([element ** 3 for element in numbers[2::3]])

print(cube_list_sum / square_list_sum)