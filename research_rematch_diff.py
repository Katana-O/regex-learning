import re
if __name__ == '__main__':
    print('main')
    charStr = "abcdefnc abcde123"
    mobj = re.search('hey', charStr)  # re.search searches anywhere in the string, and it only pulls out the first instance.
    re.match('hey', charStr)          # re.match only search the beginning of the string
    print('end')