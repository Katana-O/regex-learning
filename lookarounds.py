import re
# import regex
if __name__ == '__main__':
    print('start')
    # Allows us to confirm that some sort of subpattern is ahead or behind

    # 4 types of look arounds
    # Positive look ahead     ?=
    # Positive look behind    ?<=

    # Negative look ahead     ?!
    # Negative look behind    ?<!

    # similar syntax
    # ?: non-capturing groups
    # ?p naming groups

    # ***************************************************************************************
    # Positive look around
    # ***************************************************************************************
    charStr = '''
    ABC1    1.1.1.1     20151118    active
    ABC2    2.2.2.2     20151118    inactive
    ABC1    x.x.x.x     xxxxxxxx    active
    '''
    pattern = re.compile('ABC\w\s+(\S+)\s+\S+\s+(?=active)') # positive look-ahead
    print(re.findall(pattern , charStr)) # output: ['1.1.1.1', 'x.x.x.x']

    pattern = re.compile('ABC\w\s+(\S+)\s+\S+\s+(?:active)')
    print(re.search(pattern, charStr)) # output: <re.Match object; span=(5, 43), match='ABC1    1.1.1.1     20151118    active'>
    # Here "consumes" means the cursor moves ahead and 'consumes' the character.
    print(re.findall(pattern, charStr))  # output: ['1.1.1.1', 'x.x.x.x']

    charStr1 = 'abababacb'
    pattern = re.compile('(?<=b)(a)(?=b)')
    print(re.findall(pattern, charStr1)) # output: ['a', 'a']

    charStr2 = '98123818055818666'
    pattern = re.compile('(?<=8)(1)(?=8)')
    print(re.findall(pattern, charStr2)) # output: ['1', '1']

    # capture the entire look around
    charStr3 = 'abababacb'
    pattern = re.compile('(?=(bab))')
    print(re.findall(pattern, charStr3)) # output: ['bab', 'bab']

    charStr4 = 'ababababcb'
    pattern = re.compile('(?=(bab))')
    print(re.findall(pattern, charStr4)) # output: ['bab', 'bab', 'bab']

    # another example of positive look ahead
    charStr5 = 'I love cherries, apples, and strawberries.'
    pattern = re.compile(r'(\w+)(?=\.|,)') # Positive look ahead     ?=
    print(re.findall(pattern, charStr5)) # output: ['cherries', 'apples', 'strawberries']

    # consecutive look around fallacy
    charStr6 = '''
    cherry 100 red
    apple  150 green
    grapes 200
    '''
    pattern = re.compile(r'[a-z]+\s*(?= \d+)(?=\s*)(?=[a-z]+)')
    print(re.findall(pattern, charStr6))    # output: []

    # ***************************************************************************************
    # Negative Look Around
    # ***************************************************************************************
    # Negative look ahead  ?!
    # Negative look behind ?<!
    charStr7 = '''
    Remaining party applicants:
    
    Occupation: Party Planner
    Occupation: Baking
    Occupation: Cook
    Occupation: Publicist
    Occupation: baker
    '''
    pattern = re.compile('Occupation: (?!Baker|Baking|Cook).+', flags=re.IGNORECASE|re.MULTILINE)
    # this pattern means we're looking for anything ahead of Occupation is not 'Baker, Baking and Cook', That's the principle of Negative look around.
    # and why it denotes 'negative' instead of positive.
    print(re.findall(pattern, charStr7)) # output: ['Occupation: Party Planner', 'Occupation: Publicist']

    # Variable Width Assertions with Look Behinds



    print('end')