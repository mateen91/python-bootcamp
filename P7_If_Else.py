# CONDITIONS

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

if 5 == 4:
    print('Five is equal to four')
elif 5 != 4:
    print('Five is not equal to four')


cars = ['Honda', 'Toyota', 'Suzuki', 'Mitsubishi']

if 'Ford' in cars:
    print('Found Ford in cars')
elif 'Honda' not in cars:
    print('Did not find Honda in cars')
else:
    print('Honda is available but Ford is not')
