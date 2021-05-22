import re
if __name__ == '__main__':
    print('start')



    # on group, we have to satisfy the entire group
    charStr = 'abababababababab' # ab repeated many times
    print(re.search('(ab)+', charStr).group()) # output: abababababababab
    print('test->', re.search('(ab1)+', charStr))  # output: test-> None, we got None cuz our pattern is not satisfied.

    # we only need to satisfy one character in the character set.
    charStr1 = 'ababababababababab' # ab repeated
    print(re.search('[ab]+', charStr1).group()) # output: ababababababababab, pattern is satisfied cuz it's going to match either a or b.
    print('test:', re.search('(ab)+', charStr1).group(1))  # output: ababab
    #print('test:', re.search('(ab)+', charStr1).group(2))  # output: Error.
    charStr2 = 'abababbbbbb'
    print(re.search('(ab)+', charStr2).group()) # output: ababab
    print(re.search('(ab)', charStr2).group())  # output: ab , we got only 'ab' cuz we lack the '1 or more' functionality
    charStr3 = 'ac123abab456abab666ab'
    print(re.search('(ab)+', charStr3).group())  # output: abab, for '(ab)+', once it finds a match, it discontinue on finding the 2nd instance
    print(re.search('(ab)+', charStr3).group(1))  # output: ab
    mobj = re.search('(ab)+', charStr3)
    charStr4 = 'ac123abababab456abab666ab'
    mobj = re.search('(ab)+', charStr4)
    print(mobj.group()) # output: abababab

    charStr5 = 'ba12ba34ba'
    try:
        print(re.search('(ab)+', charStr5).group()) # output: Error, Nonetype object has no attribute 'group', cuz our group pattern is not satisified.
    except:
        pass

    charStr6 = 'ababababab'
    mobj = re.search('(ab)+(ab)+', charStr6) # regs = ((0, 10), (6, 8), (8, 10))
    mobj1 = re.search('(ab)(ab)', charStr6)  # regs = ((0, 4), (0, 2), (2, 4))

    charStr7 = '123456789'
    match = re.search('(\d)+', charStr7)
    print(match.group(0)) # output: 123456789. Quantifier is working that's why we got the whole string.
    print(match.group(1)) # output: 9. We always get the last value of the entire group with quantifiers.
    print(match.groups()) # output: ('9',)

    # Quantifiers with groups within finall
    charStr8 = '123456789'
    print(re.findall('(\d)+', charStr8)) # output: ['9']
    charStr9 = '1234 56789'
    print(re.findall('(\d)+', charStr9))  # output: ['4', '9']
    print('test->', re.findall('(\d+)', charStr9))  # output: test-> ['1234', '56789']
    print(re.findall('((\d)+)', charStr9)) # output: [('1234', '4'), ('56789', '9')]

    charStr10 = 'ababbbbb ababababcccc'
    print(re.findall('((ab)+)', charStr10)) # output: [('abab', 'ab'), ('abababab', 'ab')]

    charStr11 = '1234 56789 abc 987 bcd 654'
    print(re.findall('(\d+)', charStr11)) # output: ['1234', '56789', '987', '654']
    print(re.findall('\d+', charStr11))  # output: ['1234', '56789', '987', '654']. same as above



    print('end')