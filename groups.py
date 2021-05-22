import re
if __name__ == '__main__':
    print('main')
    # quick review:
    charStr = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 2 legs'
    print(re.search('[A-Za-z]', charStr).group())  # output: J
    print(re.search('[A-Za-z]+', charStr).group())  # output: John
    print(re.findall('[A-Za-z]+', charStr)) # output: ['John', 'has', 'cats', 'but', 'I', 'think', 'my', 'friend', 'Susan', 'has', 'dogs', 'and', 'Mike', 'has', 'legs']
    print(re.findall('[A-Za-z]+ \w+', charStr))  # output: ['John has', 'cats but', 'I think', 'my friend', 'Susan has', 'dogs and', 'Mike has']
    print(re.findall('[A-Za-z]+ \w+ ', charStr))  # output: ['John has ', 'cats but ', 'I think ', 'my friend ', 'Susan has ', 'dogs and ', 'Mike has ']
    print(re.findall('[A-Za-z]+ \w+ \d+', charStr))  # output: ['John has 6', 'Susan has 3', 'Mike has 2']
    print(re.findall('[A-Za-z]+ \w+ \d+ \w+', charStr)) # output: ['John has 6 cats', 'Susan has 3 dogs', 'Mike has 2 legs']

    charStr1 = 'Hel9lo 123'
    print(re.search('[A-Za-z]+', charStr1).group())  # output: Hel
    print(re.findall('[A-Za-z]+', charStr1)) # output: ['Hel', 'lo']

    # the use of brackets denotes a group
    # () = metacharacter
    # group allows us to output the subsection we want.
    charStr2 = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 2 legs'
    print(re.findall('[A-Za-z]+ \w+ \d+ \w+', charStr)) # output: ['John has 6 cats', 'Susan has 3 dogs', 'Mike has 2 legs']
    print(re.findall('([A-Za-z]+) \w+ \d+ \w+', charStr2)) # output: ['John', 'Susan', 'Mike']
    print(re.findall('[A-Za-z]+ \w+ (\d+) \w+', charStr2))  # output: ['6', '3', '2']

    print(re.search('([A-Za-z]+) \w+ (\d+) (\w+)', charStr2).groups())  # output: ('John', '6', 'cats')
    print(re.search('([A-Za-z]+) \w+ (\d+) (\w+)', charStr2).group())   # output: John has 6 cats
    print(re.search('[A-Za-z]+ \w+ \d+ \w+', charStr2).group())         # output: John has 6 cats
    print(re.search('([A-Za-z]+) \w+ (\d+) (\w+)', charStr2).group(1))  # output: John
    print(re.search('([A-Za-z]+) \w+ (\d+) (\w+)', charStr2).group(2))  # output: 6
    print(re.search('([A-Za-z]+) \w+ (\d+) (\w+)', charStr2).group(0, 1, 2, 3))  # output: ('John has 6 cats', 'John', '6', 'cats')
    print(re.search('([A-Za-z]+) (\w+) (\d+) (\w+)', charStr2).group(0, 1, 2, 3))  # output: ('John has 6 cats', 'John', 'has', '6')
    print(re.search('([A-Za-z]+) (\w+) (\d+) (\w+)', charStr2).start(1))  # output: 0
    print(re.search('([A-Za-z]+) (\w+) (\d+) (\w+)', charStr2).start(2))  # output: 5



    # iterator:
    charStr3 = 'John has 6 cats but I think my friend Susan has 3 dogs and Mike has 2 legs'
    it = re.finditer('([A-Za-z]+) \w+ (\d+) (\w+)', charStr3)
    for i in it:
        print(i.group())



    print('end')