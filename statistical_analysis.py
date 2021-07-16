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
            
            
            data_input_amount =integer_checker(data_input_amount, '\n Please input number (1, 10, 2999) amount: ') #checks if data is in an integer form or not
           
            
            
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

    raw_data_printer()
    correction()

def correction(): #checks if data is correct, and allows for corrections
    correction_variable = True
    while correction_variable == True:

        checking = input('''\n Real quick, check the data above and make sure it looks correct. 
        Press Y for correct
        Press N for not-correct
        Y/N: ''').upper()
        
        while checking != 'Y' and checking !='N':
            raw_data_printer()
            checking =input('''\n please enter "Y" if data is correct and "N" for if the data is incorrect: 
            Y/N: ''').upper()
        
        if checking == 'N':
            raw_data_printer()
            print('''
            OK.''')
            #may need to loop this section
            #checking_flag =True
            #while
            data_corector = input('''What is not corect about the data? Type the number of your answer.
            1 The catigory(s) are wrong.
            2 There are too many/ not enough instances of a catigory.
            3 I accedently included instences of one catigory into another one. 
            4 Actualy the data is correct.
            
            Enter choice: ''')

            while data_corector not in ['1','2','3']:
                data_corector = (input('''please enter: 
                1 for wrong catigories.
                2 for wrong amount of instance.
                3 for data is correct.
                Enter choice: '''))
            
            
            
            if data_corector == '1': #here is if you have made a wrong catigory
                problem_catigory =''
                catigory_counter =1
                raw_data_printer()
                print('Which of these catigories is wrong?')
                
                for catigory in data_dictionary_name_and_amount.keys(): #generates the names of each curent catigory.
                    print('{} {}'.format(catigory_counter, catigory))
                    catigory_counter +=1
                    ####### need to make sure it is not a valueError
                print("{} Actually they look correct".format(catigory_counter))
                wrong_catigories = input('Enter number: ')
                        ##
                if wrong_catigories == str (catigory_counter):  #this group of text allows usr to leave their selection
                    raw_data_printer() 
                    continue
                        ##    

                wrong_catigories = integer_checker(wrong_catigories, 'Please enter a choice as a number: ') #probably need to make this simalar to right abouve
                problem_catigory = list(data_dictionary_name_and_amount)[int(wrong_catigories)-1] #finds the name of the wrong catigory.
                What_to_do_to_catigory = input('What do you want to change the "{}" catigory to? '.format(problem_catigory)) #give the NEW name of the catigory.
                data_dictionary_name_and_amount[What_to_do_to_catigory] = data_dictionary_name_and_amount.pop(problem_catigory) #changes the name of the key into the new name.
                instance_index = 0
                
                for instance in Raw_input_data_list_individual: #replaces the values in the list with a value in the dictionary key
                
                    if instance == problem_catigory:
                        Raw_input_data_list_individual[instance_index] = What_to_do_to_catigory
                    instance_index +=1
                raw_data_printer()
               


            if data_corector == '2': #This is for if you need to change the amount of a catigory
                problem_catigory =''
                catigory_counter =1
                catigory_names =[]
                raw_data_printer()
                print('Which of these catigories has the wrong amount?')
                                
                for catigory in data_dictionary_name_and_amount.keys(): #generates the names of each curent
                    print('{} {}'.format(catigory_counter, catigory))
                    catigory_counter +=1
                    catigory_names.append(catigory)
                    ####### need to make sure it is not a valueError
                print("{} Actually they look correct".format(catigory_counter))
                
                
                wrong_catigories = input('Enter number: ')
                ###
                if wrong_catigories == str (catigory_counter): #this group of text allows usr to leave their selection
                    raw_data_printer() 
                    continue
                ###
                wrong_catigories = input('Enter number: ')
                
                wrong_catigories = integer_checker(wrong_catigories, 'Please enter a choice as a number: ') #generates the number used to find the problem catigory.
                print(raw_data_printer())
                amount_to_change = input('The current amount for "{}" is "{}" what do you want to change it to? '.format(str(catigory_names[int(wrong_catigories)-1]), str(data_dictionary_name_and_amount[catigory_names[int(wrong_catigories)-1]])))
                amount_to_change = integer_checker(amount_to_change, "\n I'm sorry only accept number amounts, please enter a number amount: ")
                data_dictionary_name_and_amount[catigory_names[int(wrong_catigories)-1]] = amount_to_change
                print(raw_data_printer())



            if data_corector == '3': #This closes the correction part and moves on to determining the analysis type
                print("Sounds good.")
                correction_variable = False
                TypeofAnalysis()






        elif checking == 'Y':#This closes the correction part and moves on to determining the analysis type
            print("Sounds good.")
            correction_variable = False
            TypeofAnalysis()


def TypeofAnalysis():
    mean_flag =False
    median_flag =False
    mode_flag = False
    S_D_flag = False
    bar_graph_flag =False
    
    analysis_choice_flags =[]
    analysis_choice_types = ['Mean', 'Median', 'Mode', 'Standard deviation', 'Bar graph']
    analysis_types = 'You have chosen to find the:'
    analysis_end_flag =False
    while analysis_end_flag ==False:
        analysis_choice = input('''\n What type of anaysis do  you want to do?
        1 Mean
        2 Median
        3 Mode
        4 Standard deviation
        5 Bar graph
        6 Everything
        7 I have what i need
        Enter Number: ''')
        
        if analysis_choice =='6':
            for choice in analysis_choice_types:
                if choice not in analysis_choice_flags:
                    analysis_choice_flags.append(choice)
                    analysis_types += ' ' + choice +','
            print(analysis_types)
            analysis_end_flag = True
        
        
        elif analysis_choice =='7':
            print(analysis_types)          
            analysis_end_flag = True
            

        elif analysis_choice in ['1', '2', '3','4','5']:
            choice_int = int(analysis_choice)-1
            if analysis_choice_types[choice_int] not in analysis_choice_flags:
                analysis_types += ' ' + analysis_choice_types[choice_int] +','
                analysis_choice_flags.append(analysis_choice_types[choice_int])
            print(analysis_types)
        else:
            print('\n Please input a number between 1 and 6\n\n')
    #print("\n This should be a type of alysis")   

UserInterface_DataInput()