dictionary = {94: 2, 83: 4}

def printLines(num_of_lines, units ='unitless'): #unit must be a string
    count = ''
    
    for i in range(num_of_lines):
        count += '|'
    return str(count) + '   ' + str(len(count)) +' ' +units

#print(printLines(3))


def bar_graph(dic):
    print(dic.items())
    bar_graphic = ''
    for catigory, amount in dic.items():
        for a in range(catigory):
            count = ''
        
            for i in range(amount):
                count += '|'
            bar_graphic += count + '\n'

    pass






bar_graph(dictionary)