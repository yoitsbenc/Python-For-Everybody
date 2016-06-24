import re
fhand = open('FILENAME')
numbers = list()
total=0
for line in fhand:
    line = line.rstrip()
    if re.search('\S([0-9]+)', line):
        numbers = re.findall('([0-9]+)', line)
for n in numbers:
    total=total+int(n)
print total
        
