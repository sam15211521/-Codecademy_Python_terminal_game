class DatatoAnalyse:
    data_total_amount = 0           #maybe need this, maybe not
    
    def __init__(name='', amount=0):          #this program is only to be used with simple bar graph data with a name of the item and amount of that item.
        self.name = name
        self.amount = amount
    
#def information list

#def summing_data():         #takes the data from amount and adds them together          #also keeps track of what data has what sum
 #   summing_dict ={}

Raw_input_data_list_individual =[]


#def counting_data():


#def mean():

#def median():
    
#def mode():


#def DataSorter():


def UserInterface():
    
    opening = input('''Hello, what would you like to do? (type number to do so)
    1. enter data individually (name only)'
    2. enter data with name and amount' 
    ''')
    if opening =='1':
        finished_with_data_input =False
        

        while finished_with_data_input == False:
            data_individual = input('Alright, please enter name of item ')
            Raw_input_data_list_individual.append(data_individual)
            continue_input = input('Do you have more data to input? Y/N ')
            print()
            c_i_upper =continue_input.upper()
            
            
            if c_i_upper != 'Y' and c_i_upper != 'N':
                input ('Inproper response please type "Y" if you have more data or "N" if you do not have more data ')
            else:
                if c_i_upper == 'N':
                    finished_with_data_input = True
                else:
                    finished_with_data_input =False
    print(Raw_input_data_list_individual)
        

UserInterface()