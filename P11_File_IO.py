# File IO

f = open('demo.txt')
print(f.read())
f.close()

with open('demo.txt') as f:
    print(f.read())

with open('demo.txt') as f:
    for line in f:
        print(line)
