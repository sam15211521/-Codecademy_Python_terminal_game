def printLines(num_of_lines):
    count = ''
    
    for i in range(num_of_lines):
        count += '|'
    return str(count) +'\n' +'there are ' + str(len(count)) +' units'

print(printLines(3))