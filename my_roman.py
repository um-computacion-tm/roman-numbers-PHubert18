#dec_to_roman
def decimal_to_roman(decimal):
    val = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    roman = ''
    for num, word in val:
        while decimal >= num:
            roman += word
            decimal -= num
    return roman

#roman_to_dec
def roman_to_decimal(roman):
    dictionary = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000}
    total = 0
    prev = 0
    for word in roman[::-1]:
        num = dictionary[word]
        if num < prev:
            total -= num
        else:
            total += num
        prev = num
    return total
