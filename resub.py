import re
if __name__ == '__main__':
    print('start')
    # re.sub - substitute a certain word or a serialize of words.
    charStr = '''U.S. stock-index futures pointed
    to a solidly higher open on Monday,
    indicating that major
    benchmarks were poised to USA reboundfrom last week’s sharp decline,
    \nwhich represented their biggest weekly drops in months.
    '''
    print(re.sub('U.S. |US|USA', 'United States ', charStr))
    # output: United States stock-index futures pointed ......
    print('end')