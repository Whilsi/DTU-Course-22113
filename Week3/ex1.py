import re

string = input('Type a number: ')

print(string)

result = re.match(r'^(-?\d+(\.?\d+|))$',string)

if result is not None:
    print('The input is a number')
else:
    print('The input is not a number')