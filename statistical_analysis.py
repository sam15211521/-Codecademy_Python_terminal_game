class DatatoAnalyse:
    data_total_amount = 0           #maybe need this, maybe not
    
    def __init__(self, name='', amount=0):          #this program is only to be used with simple bar graph data with a name of the item and amount of that item.
        self.name = name
        self.amount = amount

Raw_input_data_list_individual =[]      #this is where all raw data goes
data_dictionary_name_and_amount ={}     #this is where all data that has been analysed to have the catigory and amount go


#def information list

#def summing_data():         #takes the data from amount and adds them together          #also keeps track of what data has what sum



#def counting_data():


#def mean():

#def median():
    
#def mode():


#def DataSorter():
def raw_data_printer():
    print('--------------')
    print(Raw_input_data_list_individual)
    print()   
    print(data_dictionary_name_and_amount)


def raw_data_to_grouped(lst=Raw_input_data_list_individual): #groups raw data in a list to form a dictionary with the catigory and the number of times that catigory occurs
    instances = []
    for name in lst:
        if name not in instances:
            instances.append(name)
    for name in instances:
        data_dictionary_name_and_amount[name] =lst.count(name)

def correction(): #checks if data is correct, and allows for corrections
    checking = input('''\n Real quick, check the data above and make sure it looks correct. 
    Press Y for correct
    Press N for not-correct
    Y/N: ''').upper()
    
    while checking != 'Y' and checking !='N':
        print('--------------')
        print(Raw_input_data_list_individual)
        print()   
        print(data_dictionary_name_and_amount)
        checking =input('''\n please enter "Y" if data is correct and "N" for if the data is incorrect: 
        Y/N: ''').upper()
    
    if checking == 'N':

        raw_data_printer()
        print('''
        OK.
        ''')
        #may need to loop this section
        #checking_flag =True
        #while
        data_corector = input('''What is not corect about the data? Type the number of your answer.
        1 The catigory(s) are wrong.
        2 There are too many/ not enough instances of a catigory.
        3 I accedently included instences of one catigory into another one. 
        
        Enter choice: ''')

        while data_corector not in ['1','2','3']:
            data_corector = (input('''please enter: 
            1 for wrong catigories
            2 for wrong amount of instance
            3 for included instences in wrong catigory
            
            Enter choice: '''))
        if data_corector == 1:
            wrong_catigories = input('')
        if data_corector == 2:
            pass
        if data_corector == 3:
            pass






    elif checking == 'Y':
        print("Sounds good.")
        TypeofAnalysis()




def UserInterface_DataInput(): # The initial user interface for when you need to add data to the project
    
    opening = input('''Hello, what would you like to do? (type number to do so)
    1. Enter data individually (name only)
    2. Enter data with name and amount 
    Enter Here: ''')
    print()
    
    while opening != '1' and opening != '2':
        opening = input('Please input 1 for individualy or 2 for catigory and amount: ')
    
    if opening =='1': #this part simply places your inputs into a list that can then be analysed at a later time
                      #only adds raw data to be analysed
        finished_with_data_input =False
        while finished_with_data_input == False:
            data_individual = input('Alright, please enter name of item: ')
            Raw_input_data_list_individual.append(data_individual)
            continue_input = input('Do you have more data to input? Y/N: ')
            print()
            c_i_upper =continue_input.upper()
            
            
            if c_i_upper != 'Y' and c_i_upper != 'N':
                input ('Improper response please type "Y" if you have more data or "N" if you do not have more data: ')
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
            data_input_name = input('\n Alright, please enter name of the catigory: ')
            name_number_list .append(data_input_name)
            data_input_amount = input('\n Please input amount of instances of the catigory: ')
            input_exception = True
            while input_exception:
                try:
                    a = type(int(data_input_amount))
                    input_exception = False
                except:
                    data_input_amount = input('\n Please input number (1, 10, 2999) amount: ')
            name_number_list.append(data_input_amount)
            if name_number_list[0] not in data_dictionary_name_and_amount:
                data_dictionary_name_and_amount[name_number_list[0]] =int(name_number_list[1])
            else:
                data_dictionary_name_and_amount[name_number_list[0]] +=int(name_number_list[1])
            name_number_list = []
            continue_input = input('\n Do you have more data to input? Y/N: ')
            
            c_i_upper =continue_input.upper()
            
            
            
            if c_i_upper != 'Y' and c_i_upper != 'N':
                while c_i_upper not in ['Y','N']:
                    c_i_upper =input ('\n Improper response please type "Y" if you have more data or "N" if you do not have more data: ').upper()
                    print()
                    if c_i_upper == 'N':
                        finished_with_data_input = True
                    else:
                        finished_with_data_input =False
                


            else:
                if c_i_upper == 'N':
                    finished_with_data_input = True
                else:
                    finished_with_data_input =False
        for catigory, value in data_dictionary_name_and_amount.items():
            for i in range(value):
                Raw_input_data_list_individual.append(catigory)

    print()
    print(Raw_input_data_list_individual)
    print()   
    print(data_dictionary_name_and_amount)
    correction()

def TypeofAnalysis():
    pass   

UserInterface_DataInput()