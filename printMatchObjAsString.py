import re
if __name__ == '__main__':
    print('main')
    charStr = "abcdefnc abcde123"
    mobj = re.search('de', charStr)  # re.search searches anywhere in the string, but it only pulls out the first instance.
    print(mobj.group()) # default value is 0.
    charStr1 = '123abc456'
    print(re.search('[a-z]', charStr1).group())
    print('end')