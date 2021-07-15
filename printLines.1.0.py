def printLines(num_of_lines, units ='unitless'): #unit must be a string
    count = ''
    
    for i in range(num_of_lines):
        count += '|'
    return str(count) + '   ' + str(len(count)) +' ' +units

print(printLines(3))