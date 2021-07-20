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
    input_exception = True
    while input_exception:
        try:
            type(int(data_input_amount))
            input_exception = False
        except:
            data_input_amount = input(correction_string)
            return(data_input_amount)
    return(data_input_amount)



opening = input('''Hello, what would you like to do? (type number to do so)
    1. Enter data individually (name only)
    2. Enter data with name and amount 
    Enter Here: ''')
print()

while opening != '1' and opening != '2':
        opening = input('Please input 1 for individualy or 2 for catigory and amount: ')

if opening =='1':                                                                  #this part simply places your inputs into a list that can then be analysed at a later time
                                                                                    #only adds raw data to be analysed
    
    finished_with_data_input = False
    while finished_with_data_input == False:
        data_individual = input('Alright, please enter name of catigory item: ')
        
        data_individual = integer_checker(data_individual, data_individual)

        Raw_input_data_list_individual.append(data_individual)

        continue_input = input('Do you have more data to input? Y/N: ').upper()
        print()
        


        if continue_input != 'Y' and continue_input != 'N':                         #this part determins if you need to add more code
                    input ('Improper response please type "Y" if you have more data or "N" if you do not have more data: ')
                    print()
        else:
                    if continue_input == 'N':
                        finished_with_data_input = True
                    else:
                        finished_with_data_input =False
    print(Raw_input_data_list_individual)

    raw_data_to_grouped()                                                           #takes the list of data we have made and turns it into a dictionary that counts number of instences
    print(data_dictionary_name_and_amount)




if opening == '2':                                                                  #instead of raw data, makes a dictionary with the name of a catigory and the number of instances with it.
    name_number_list = []
    finished_with_data_input =False
    
    while finished_with_data_input == False:                                        #checks if finished with data input
        data_input_name_string ='\n Alright, please enter name of the catigory: '
        data_input_name = input(data_input_name_string)  #the catigory in question
        data_input_name = integer_checker(data_input_name, data_input_name_string)         # checks to see if catigory is an integer, and converst if is
        ##
        data_input_amount_string ='\n Please input amount of instances of the catigory: '
        data_input_amount = input(data_input_amount_string)
        data_input_amount =integer_checker(data_input_amount,'\n Error: Please input number (1, 10, 2999) amount: ') #checks if data is in an integer form or not. if it is returns error.


        name_number_list = [data_input_name, data_input_amount]    
        if name_number_list[0] not in data_dictionary_name_and_amount:      #adds catigory and amount into the data dictionary for later analysis
                data_dictionary_name_and_amount[name_number_list[0]] = name_number_list[1]
        else:
            data_dictionary_name_and_amount[name_number_list[0]] += name_number_list[1] # if a catigory is the same as another, will add the two together
        

        name_number_list = []
        continue_input = input('\n Do you have more data to input? Y/N: ').upper()




        if continue_input != 'Y' and continue_input != 'N':
            while continue_input not in ['Y','N']:
                continue_input =input ('\n Improper response please type "Y" if you have more data or "N" if you do not have more data: ').upper()
                print('\n---\n')



        if continue_input == 'N':
            finished_with_data_input = True

        elif continue_input == 'Y':
            finished_with_data_input =False

print(data_dictionary_name_and_amount)