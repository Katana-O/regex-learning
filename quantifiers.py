import re
if __name__ == '__main__':
    print('main')
    # '+' = 1 or more
    # '?' = 0 or 1
    # '*' = 0 or more
    # '{n,m}' = n to m repetitions {,3} (any number up to 3), {3,} (3 to any number)
    # '\w' = [a-zA-Z0-9_]
    # '\W' = opposite of \w, nothing include in [a-zA-Z0-9_]
    charStr = "abcdefg abc123"
    print(re.search('\w+', charStr).group()) # output:abcdefg. It keeps going until it hits an empyt space
    charStr1 = "abcdefg   abc123"
    print(re.search('\w+\W+\w', charStr1).group()) # output:abcdefg   a.
    charStr2 = "abcdefgabc123"
    print(re.search('\w+\W?\w', charStr2).group())  # output:abcdefgabc123. '?' means there is one or not.
    charStr3 = "abcdefgabc123"
    print(re.search('\w{3}', charStr3).group())  # output:abc. {n} means it matches up to 3 characters.

    # '\d' = matches digits [0-9]
    # '\D' = matches any non-digit character; ~\d
    charStr4 = "23abc2de++"
    print(re.search('\d+', charStr4).group()) # output:23
    print(re.search('\D+', charStr4).group())  # output:abc

    # '\s' = matches any whitespace character
    # '\S' = matches any non-whitespace character
    charStr5 = '23abcde++ 123'
    print(re.search('\S+', charStr5).group())  # output:23abcde++. pull out all non-space text.
    print(re.search('\s+', charStr5).group())  # output:' '

    # '.' the dot matches any character except the newline.
    charStr6 = '''djsalkjdslak
    jdskajdlkasjlk
    qiwueoiw123'''
    print(re.search('.+', charStr6, flags = re.DOTALL).group()) # output:[everything]. Using DOTALL flags means include the newline.





    print('end')