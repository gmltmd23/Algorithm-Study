import sys
input = sys.stdin.readline

ppapString = input().rstrip()
if ppapString == 'P' or ppapString == 'PPAP':
    print('PPAP')
else:
    stack = []
    staticPPAPString = ['P', 'P', 'A', 'P']
    for character in ppapString:
        stack.append(character)
        if staticPPAPString == stack[-4:]:
            for _ in range(3): stack.pop()
    if stack == ['P']:
        print('PPAP')
    else:
        print('NP')