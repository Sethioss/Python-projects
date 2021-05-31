"""
numeral_base_converter is a Python module which quickly allows you to convert numbers from a numerical base to another.

The available bases go from base 2 (Binary) to 36 (Z being the maximum base, defining base 36)

Initialize the calculator with numeral_base_converter.init() before usage. You can also launch the
main program with numeral_base_converter.start()"""

def init():
    """Initializes the calculator. Get access to base_tenth variable"""
    global base_tenth
    base_tenth = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL', 'mM', 'nN', 'oO'
              , 'pP', 'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ']

def check_answer(answer, comparison):
    for letter in answer:
        for element in comparison:
            if letter not in str(element):
                return False
    return True

def to_decimal(number):
    """Converts any number to a decimal value (F -> 16)"""
    for i in range(len(base_tenth)):
        if number in base_tenth[i]:
            number = base_tenth.index(base_tenth[i])
                
            #print(number)
            return number


def to_abovedec(number):
    """Converts any base 10 value to its original base corresponding value
    (16 -> F) if necessary"""
    global base_tenth
    if int(number) >= 10:
        number = base_tenth[int(number)][1:]
    else:
        number = base_tenth[int(number)]

    #print(number) 
    return number

def to_base_ten(number, og_base):
    """Convert any number to base 10 (F1 -> 17). Works as the step one of base_to_base conversion.
    (Warning: Takes strings for arguments)"""
    result = ''
    sign = ''
    result_int = 0
    j = 0

    if('-' in number):
        number = number[1:]
        sign = '-'
        #print(sign)
        
    number_size_in_digits = len(number)
    
    for i in range(number_size_in_digits -1, -1, -1):

        if int(to_decimal(number[j])) >= int(og_base):
            result = 'ERR::103'
            print('')
            print('----------------ERROR----------------')
            msg = result + " Input error: The number " + '"' + number + '" ' + "doesn't correspond to its defined base " + '"' + og_base + '".'
            print(msg)
            msg = 'Error casting the number ' + number + ' into base ' + str(og_base)
            print(msg)
            print('-------------------------------------')
            print('')
            global calculation_finished
            calculation_finished = True
            global detected_error
            detected_error = True
            return result

        else:
            numeral = int(to_decimal(number[j])) * int((og_base))**i
            
            if(i==0):
                result_int = result_int + int(to_decimal(number[j]))
            else:
                result_int = result_int + numeral
            
        j = j+1

        if(sign == '-'):
            result = sign + str(result_int)
        else:
            result = str(result_int)
            
    msg = sign + number + 'in base' + og_base + 'to base 10 is equal to' + sign + result
    #print(msg)
    return result
 
#Calculation logic
def calculate_to_base(number, base):
    """Convert any number to base 10 (17->F1). Works as the step one of base_to_base conversion.
    (Warning: Takes strings for arguments)"""

    result = ''
    number_int = 0
    base_int = int(base)
    sign = ''

    if(number == 'ERR::103'):
        msg = number + ' in base ' + base + ' is equal to ' + number
        #print(msg)
        return number

    if(base == 10):
        return number
    
    else:
        number_int = int(number)
        if(number_int == 0):
            result = '0'
            return result
        elif(number_int < 0):
            number = number[1:]
            number_int = int(number)
            sign = '-'
                        
    while(number_int) != 0:
        remainder = int(number_int % base_int)
        result = to_abovedec(str(remainder)) + result
        number_int = int(number_int / base_int)

    msg = sign + number + ' in base ' + base + ' is equal to ' + sign + result
    #print(msg)
    return str(sign) + str(result)
    


#Main loop
def main():
    """Main loop"""
    init()
    playing_program = True
    detected_error = False
    calculation_finished = False
    
    while(playing_program):
        while(not calculation_finished):
            calculation_finished = False
            user_input = ''
            base = 0
            og_base = 0

            print('')
            print('==============================================')
            print("Hey user, welcome to the numeral base converter!")

#base_to_base_mode-------------
            prompt = 'Welcome to the base to base convert! Here you can convert a number from a 2 to ' + str(len(base_tenth)) + ' numerical base to another base.'
            print(prompt)

            user_input = input("Input the number you'd like to convert. ").replace(' ', '')

#Check if input is acceptable--------------
            for i in range(len(user_input)):
                count = 0
                for j in range(len(base_tenth)):
                    if user_input[i] not in base_tenth[j] and '-' not in user_input[i]:
                        count = count + 1
                
                if count >= len(base_tenth) and not detected_error:
                    calculation_finished = True
                    detected_error = True
                    print('')
                    print('----------------ERROR----------------')
                    result = "ERR::102"
                    print(result + ' user_input ' + '"' + user_input + '"' + ' is not an acceptable value')
                    print('Error casting '+ '"' + user_input + '"' + ' as a valid number')
                    print('-------------------------------------')
                    print('')

            if(not detected_error):

                while int(og_base) < 2 or int(og_base) > len(base_tenth):
                    prompt = "Input the number's base (2 minimum," + str(len(base_tenth)) + " maximum). "
                    og_base = input(prompt)

                while int(base) < 2 or int(base) > len(base_tenth):
                    prompt = "Input the base to convert the number into (2 minimum," + str(len(base_tenth)) + " maximum). "
                    base = input(prompt)

#Results------------
        
                base_ten = to_base_ten(user_input, og_base)
                result = str(calculate_to_base(base_ten, base))
        
            print('')
            print('----------------Result----------------')
            print('')
            print(user_input, 'from base', og_base, 'to base', base, 'is equal to', result)
            print('')
            print('--------------------------------------')
            print('')
    
            calculation_finished = True
        while(calculation_finished):
            leave = ''
            while(leave != 'y' and leave != 'n'):
                leave = input('Do you want to calculate something else? (y, n) ')
                if(leave == 'n'):
                    playing_program = False
                    
            calculation_finished = False
            detected_error = False

def start():
    """Use to launch the original calculator program"""
    main()
    
if __name__ == "__main__":
    main()

