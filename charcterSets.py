import re
if __name__ == '__main__':
    print('main')
    # [A-Z] '-' is a metacharacter when used in [] (custom character sets)
    charStr = 'Hello, There, How, Are, You 123...'
    print(re.findall('[A-Z]', charStr)) # output: ['H', 'T', 'H', 'A', 'Y']
    print(re.findall('[A-Z,1.]', charStr)) # output: ['H', ',', 'T', ',', 'H', ',', 'A', ',', 'Y', '1', '.', '.', '.']. A comma means it's gonna search for a comma, and dot loses its meaning when in a character set.

    # Quantifiers with Customer Sets
    charStr1 = 'HELLO, There, how, Are , you'
    print(re.search('[A-Z]+', charStr1).group()) # output: HELLO
    print(re.search('[A-Z]{2,}', charStr1).group())  # output: HELLO. Output 2 or more.
    print('result:', re.search('[A-Za-z\s,]+', charStr1).group())  # output: HELLO, There, how, Are , you

    # '^' means start of the line when use outside of custom bracket, means not when use inside a custom bracket
    charStr2 = 'HELLO, There, How, Are, You...'
    print(re.search('[^A-Za-z\s,]+', charStr2).group())  # output: ...   we negate custom set only outputs "..."
    print(re.findall('[^A-Z]+', charStr2))  # output: [', ', 'here, ', 'ow, ', 're, ', 'ou...']. remember group() is only for re.search
    print(re.findall('[A-Z]?[a-z\s,]+', charStr2))
    charStr3 = 'ABCDEF aPOIUsA'
    print(re.findall('[^A-Z\s]+', charStr3)) # output: ['a', 's'].
    print(re.findall('[^A-Z\s]', charStr3))  # output: ['a', 's']. same result as above
    print('end')