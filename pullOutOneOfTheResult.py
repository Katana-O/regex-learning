import re
if __name__ == '__main__':
    print('main')
    charStr = "abcdefg abc123"
    mobj = re.search('0|b', charStr)  # re.search searches anywhere in the string, and it only pulls out the first instance.
    print(mobj.group()) # default value is 0.
    print('end')