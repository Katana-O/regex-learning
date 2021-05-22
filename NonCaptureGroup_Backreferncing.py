import re
if __name__ == '__main__':
    print('start')
    # ?:
    # The symbol above represents non-capture groups and look slightly similar to the syntax for naming groups
    # ?P
    # The symbol above represents Naming group (Don't confuse the two)
    charStr = '1234 56789'
    # quick review:
    mobj = re.search('(\d)+', charStr)   #
    print(mobj.group(1))                 # output: 4
    mobj = re.search('(\d+)', charStr)   #
    print(mobj.group(1))                 # output: 1234

    # quick review again:
    print('group a')
    print(re.search('(\d)+', charStr).groups())  # output: ('4',)
    print(re.search('(\d)+', charStr).group(0))  # output: 1234
    print(re.search('(\d)+', charStr).group(1))  # output: 4
    print('group b')
    print(re.search('(\d+)', charStr).groups())  # output: ('1234',)
    print(re.search('(\d+)', charStr).group(0))  # output: 1234
    print(re.search('(\d+)', charStr).group(1))  # output: 1234


    # let's get start, re.findall output the entire pattern
    charStr1 = '1234 56789'
    print(re.findall('(\d)+', charStr1))   # output: ['4', '9']
    print(re.findall('(?:\d)+', charStr1)) # output: ['1234', '56789']
    print(re.findall('(\d+)', charStr1))   # output: ['1234', '56789']

    # ?:
    # usage: we just want to use this group to find what we looking for
    charStr2 = '''
    i love cats
    i love dogs
    i hate pork
    i love meat
    '''
    print(re.findall('i love (cats|dogs)', charStr2))           # output: ['cats', 'dogs']
    print(re.findall('i love (?:cats|dogs)', charStr2))         # output: ['i love cats', 'i love dogs']
    print(re.findall('i love (?:cats|dogs|meat)', charStr2))    # output: ['i love cats', 'i love dogs', 'i love meat']
    print(re.findall('i love \w+', charStr2))                   # output: ['i love cats', 'i love dogs', 'i love meat']

    charStr3 = '123123 = Alex, 123123123 = Danny, 123123123123 = Mike, 124125 = Rick, 124123 = Kenny'
    print(re.findall('(?:123)+ = (\w+),', charStr3))            # output: ['Alex', 'Danny', 'Mike']


    charStr4 = '1*1*1*1*22222 1*1*3333 2*1*2*1*222 1*2*2*2*333 3*3*3*444'
    print(re.findall('(?:1\*){2,}(\d+)', charStr4)) # output: ['22222', '3333']
    for i in re.finditer('(?:1\*){2,}(\d+)', charStr4):
        print(i.group(1)) # output: 22222  3333

    # Backreferencing
    # making a reference to the captured group within the same regular expression
    # B.R. is functional when raw is given.
    charStr5 = 'Merry Merry Christmas'
    print(re.search(r'(\w+) \1', charStr5).group())  # '\1' is actually refer to a syntax to a group.






    print('end')