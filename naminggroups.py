import re
if __name__ == '__main__':
    print('start')
    # '?P<>' to name a group -- group name inside the <>, followed by RE for group
    # (?P<City>)  (?P<State>)  (?P<ZipCode>)
    charStr = 'OSAKA rainyton 9122101'
    #mobj = re.search(re.compile('((?P<State>[A-Z]+) (?P<City>[a-z]+) (?P<ZipCode>[0-9]+))'), charStr)
    mobj = re.search('((?P<State>[A-Z]+) (?P<City>[a-z]+) (?P<ZipCode>[0-9]+))', charStr)
    print('State:', mobj.group('State'))
    print('City:', mobj.group('City'))
    print('ZipCode:', mobj.group('ZipCode'))
    # output:
    # State: OSAKA
    # City: rainyton
    # ZipCode: 9122101


    charStr1 = 'Osaka RainyTon 9811812'
    mobj = re.search('(?P<State>[A-Za-z]+) (?P<City>[A-Za-z]+) (?P<ZipCode>[0-9]+)', charStr1)
    print('State1:', mobj.group('State'))
    print('City1:', mobj.group('City'))
    print('ZipCode1:', mobj.group('ZipCode'))
    # output:
    # State1: Osaka
    # City1: RainyTon
    # ZipCode1: 9811812

    print('end')