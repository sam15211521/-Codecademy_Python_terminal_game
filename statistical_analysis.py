class DatatoAnalyse:
    data_total_amount = 0           #maybe need this, maybe not
    
    def __init__(self, name='', amount=0):          #this program is only to be used with simple bar graph data with a name of the item and amount of that item.
        self.name = name
        self.amount = amount
    
#def information list

#def summing_data():         #takes the data from amount and adds them together          #also keeps track of what data has what sum
 #   summing_dict ={}

Raw_input_data_list_individual =[]      #this is where all raw data goes
data_dictionary_name_and_amount ={}     #this is where all data that has been analysed to have the catigory and amount go

#def counting_data():


#def mean():

#def median():
    
#def mode():


#def DataSorter():

def raw_data_to_grouped(lst=Raw_input_data_list_individual):
    instances = []
    couting_list =[]
    for name in lst:
        if name not in instances:
            instances.append(name)
    for name in instances:
        data_dictionary_name_and_amount[name] =lst.count(name)



def UserInterface():
    
    opening = input('''Hello, what would you like to do? (type number to do so)
    1. enter data individually (name only)'
    2. enter data with name and amount' 
    ''')
    print()
    
    while opening != '1' and opening != '2':
        opening = input('please input 1 for individualy or 2 for catigory and amount ')
    
    if opening =='1': #this part simply places your inputs into a list that can then be analysed at a later time
                      #only adds raw data to be analysed
        finished_with_data_input =False
        while finished_with_data_input == False:
            data_individual = input('Alright, please enter name of item ')
            Raw_input_data_list_individual.append(data_individual)
            continue_input = input('Do you have more data to input? Y/N ')
            print()
            c_i_upper =continue_input.upper()
            
            
            if c_i_upper != 'Y' and c_i_upper != 'N':
                input ('Inproper response please type "Y" if you have more data or "N" if you do not have more data ')
                print()
            else:
                if c_i_upper == 'N':
                    finished_with_data_input = True
                else:
                    finished_with_data_input =False
        
        raw_data_to_grouped()

   
        
        #if opening == '2':
    if opening == '2':  #instead of raw data, makes a dictionary with the name of a catigory and the number of instances with it.
        name_number_list = []
        finished_with_data_input =False
        while finished_with_data_input == False:
            data_input_name = input('\n Alright, please enter name of the catigory ')
            name_number_list .append(data_input_name)
            data_input_amount = input('\n please input amount of instances of the catigory ')
            name_number_list.append(data_input_amount)

            data_dictionary_name_and_amount[name_number_list[0]] =int(name_number_list[1])
            name_number_list = []
            continue_input = input('\n Do you have more data to input? Y/N ')
            
            c_i_upper =continue_input.upper()
            
            
            if c_i_upper != 'Y' and c_i_upper != 'N':
                input ('\n Inproper response please type "Y" if you have more data or "N" if you do not have more data ')
                print()
            else:
                if c_i_upper == 'N':
                    finished_with_data_input = True
                else:
                    finished_with_data_input =False


    print(Raw_input_data_list_individual)   
    print(data_dictionary_name_and_amount)

        

UserInterface()