import re
if __name__ == '__main__':
    print('main')
    charStr = "a2bcdefnc abcde123"
    print(re.search('\w\w\w', charStr).group())  # \w == [a-zA-Z0-9_]    \W opposite of \w, nothing include in [a-zA-Z0-9_], but match everything else of the set.
    print('end')