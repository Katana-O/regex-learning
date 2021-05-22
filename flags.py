import re
if __name__ == '__main__':
    print('start')
    # '^' matches at beginning of string, force our pattern to match at the beginning of the string.
    # '$' matches at end of string
    charStr = '''U.S. stock-index futures pointed to a solidly
    higher open on Monday, indicating that major benchmarks were poised to rebound
    from last week's sharp decline.
    '''
    print(re.search('futures', charStr, flags=re.MULTILINE).group()) # output: futures
    # re.MULTILINE only benefits to re.search not re.match.
    # re.DOTALL help us to include newline.
    print('end')