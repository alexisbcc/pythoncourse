# Search for lines that contain 'numbers'
import re

todo = sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_394686.txt').read())])

print(todo)


#hand = open('regex_sum_394686.txt')
#total = 0

#for line in hand:

#    line = line.rstrip()

#    data = re.findall('[0-9]+', line)
#    if data:
#        for value in data:
#            total += int(value)

#print(total)
