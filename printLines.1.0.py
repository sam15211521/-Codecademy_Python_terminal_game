dictionary = {94: 2, 83: 4}

def printLines(num_of_lines, units ='unitless'): #unit must be a string
    count = ''
    
    for i in range(num_of_lines):
        count += '|'
    return str(count) + '   ' + str(len(count)) +' ' +units

#print(printLines(3))


def bar_graph(dic):
    
    bar_graphic = ''
    for catigory, amount in dic.items():
        
        catigory_string = str(catigory)
        amount_of_instences = amount
        count =': '        
        
        for i in range(amount):
            count += '|'
            
        line_string = catigory_string + ' -- ' + str(amount_of_instences) + count
        bar_graphic += line_string +'\n'
    return bar_graphic






bar_graph(dictionary)