import statistics

Raw_input_data_list_individual =[]      #this is where all raw data goes
data_dictionary_name_and_amount ={}     #this is where all data that has been analysed to have the catigory and amount go

def find_mean(lst = Raw_input_data_list_individual):
    global mean_flag 
    mean_flag = True
    return statistics.mean(lst)
    
    

def find_median(lst = Raw_input_data_list_individual):
    global median_flag 
    median_flag = True
    return statistics.median(lst)
    
    
def find_mode(lst = Raw_input_data_list_individual):
    global mode_flag 
    mode_flag = True
    return statistics.mode(lst)    

def find_standard_deviation(lst = Raw_input_data_list_individual):
    global standard_deviation_flag 
    standard_deviation_flag = True
    return statistics.stdev(lst)
    

def find_bar_graph(dic = data_dictionary_name_and_amount):#num_of_lines, units ='unitless'):
    global bar_graph_flag 
    bar_graph_flag= True
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
    

def raw_data_printer():
    print('--------------')
    print(Raw_input_data_list_individual)
    print()   
    print(data_dictionary_name_and_amount)
    print()
    print('--------------')


def raw_data_to_grouped(lst=Raw_input_data_list_individual): #groups raw data in a list to form a dictionary with the catigory and the number of times that catigory occurs
    instances = []
    for name in lst:
        if name not in instances:
            instances.append(name)
    for name in instances:
        data_dictionary_name_and_amount[name] =lst.count(name)


def integer_checker(data_input_amount, correction_string): #checks if data is in an integer form
    try:
        int(data_input_amount)
        input_exception = False
    except:
        input_exception = False
        return correction_string        
    return int(data_input_amount)



opening = input('''Hello, what would you like to do? (type number to do so)
    1. Enter data individually (name only)
    2. Enter data with name and amount 
    Enter Here: ''')
print()

while opening != '1' and opening != '2':
        opening = input('Please input 1 for individualy or 2 for catigory and amount: ')

if opening =='1': #this part simply places your inputs into a list that can then be analysed at a later time
                      #only adds raw data to be analysed
    
    finished_with_data_input = False
    while finished_with_data_input == False:
        data_individual = input('Alright, please enter name of catigory item: ')
        
        data_individual = integer_checker(data_individual, data_individual)

        Raw_input_data_list_individual.append(data_individual)

        continue_input = input('Do you have more data to input? Y/N: ').upper()
        print()
        


        if continue_input != 'Y' and continue_input != 'N': #this part determins if you need to add more code
                    input ('Improper response please type "Y" if you have more data or "N" if you do not have more data: ')
                    print()
        else:
                    if continue_input == 'N':
                        finished_with_data_input = True
                    else:
                        finished_with_data_input =False
    print(Raw_input_data_list_individual)

    raw_data_to_grouped() #takes the list of data we have made and turns it into a dictionary that counts number of instences
    print(data_dictionary_name_and_amount)
