import re
if __name__ == '__main__':
    print('main')
    charStr = "abcdefg abc123"
    print(re.findall('a|e', charStr))
    print('end')