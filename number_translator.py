ASSOCIATION = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'm':1000, 'd':500, 'c':100, 'l':50, 'x':10, 'v':5, 'i':1}

def from_arabic_to_roman(number):
    result = ''
    result += 'M' * (number // 1000)
    number %= 1000
    if number >= 900:
        result += 'CM'
        number %= 900
    elif number >= 500:
        result += 'D'
        number %= 500
        result += 'C' * (number // 100)
        number %= 100        
    elif number >= 400:
        result += 'CD'
        number %= 400
    else:
        result += 'C' * (number // 100)
        number %= 100
        
    if number >= 90:
        result += 'XC'
        number %= 90
    elif number >= 50:
        result += 'L'
        number %= 50
        result += 'X' * (number // 10)
        number %= 10        
    elif number >= 40:
        result += 'XL'
        number %= 40
    else:
        result += 'X' * (number // 10)
        number %= 10
        
    if number >= 9:
        result += 'IX'
        number %= 9
    elif number >= 5:
        result += 'V'
        number %= 5
        result += 'I' * (number // 1)
        number %= 1        
    elif number >= 4:
        result += 'IV'
        number %= 4        
    else:
        result += 'I' * (number // 1)
        number %= 1
    
    return result

def from_roman_to_arabic(data):
    letters = list(data)
    result = 0
    for i in range(len(letters)):
        letters[i] = ASSOCIATION[letters[i]]
    for i in range(len(letters)):
        if letters[i] < letters[min(i + 1, len(letters) - 1)]:
            result -= letters[i]
        else:
            result += letters[i]
    return result

print(1846, from_arabic_to_roman(1846))
print(999, from_arabic_to_roman(999))
print(1449, from_arabic_to_roman(1449))
print(1234, from_arabic_to_roman(1234))

print('MCCCCXLV', from_roman_to_arabic('MCCCCXLV'))
print('MMMCDXLXXXIX', from_roman_to_arabic('MMMCDXLXXXIX'))
print('MCDLXXIX', from_roman_to_arabic('MCDLXXIX'))
print('CDXLIV', from_roman_to_arabic('CDXLIV'))
print('MCMXCIV', from_roman_to_arabic('MCMXCIV'))