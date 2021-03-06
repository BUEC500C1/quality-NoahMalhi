
def conv_to_rom(arab_in, endconv):

    #If 
    if arab_in >= 5000:
        endconv = endconv + '(V)'
        return (arab_in - 5000), endconv
    elif arab_in >= 1000:
        endconv = endconv + 'M'
        return (arab_in - 1000), endconv
    elif arab_in >= 900:
        endconv = endconv + 'CM'
        return (arab_in - 900), endconv
    elif arab_in >= 500:
        endconv = endconv + 'D'
        return (arab_in - 500), endconv
    elif arab_in >= 400:
        endconv = endconv + 'CD'
        return (arab_in - 400), endconv
    elif arab_in >= 100:
        endconv = endconv + 'C'
        return (arab_in - 100), endconv
    elif arab_in >= 90:
        endconv = endconv + 'XC'
        return (arab_in - 90)  , endconv 
    elif arab_in >= 50:
        endconv = endconv + 'L'
        return (arab_in - 50), endconv
    elif arab_in >= 40:
        endconv = endconv + 'XL'
        return (arab_in - 40), endconv
    elif arab_in >= 10:
        endconv = endconv + 'X'
        return (arab_in - 10), endconv
    elif arab_in >= 9:
        endconv = endconv + 'IX'
        return (arab_in - 9), endconv
    elif arab_in >= 5:
        endconv = endconv + 'V'
        return (arab_in - 5), endconv
    elif arab_in == 4:
        endconv = endconv + 'IV'
        return (arab_in - 4), endconv
    elif arab_in >= 1:  
        endconv = endconv + 'I'
        return (arab_in - 1), endconv
    else:
        return 0

def function_call():
    #Initilization of empty string to hold final value
    endconv = ""
   
    try:
        arab_in = int(input("Enter a number : "))

    #Except catches any invalid input such as a string, "FOO"
    except ValueError:
        endconv = "-"
        print(endconv)
        return

    #Loop to calculate each roman numeral; Max number allowed is 9999
    for x in range(arab_in):
        if arab_in > 9999:
            print("Entered value must be less than 10,000")
            endconv = "-"
            break
        arab_in, endconv = conv_to_rom(arab_in, endconv)
        if arab_in == 0 :
            break
        
    #If negative give an erroneous output message
    if arab_in < 0:
        endconv = "-"
        print ("Enter value greater than 0")   
    print(endconv)
    print('Done')
    return endconv
        

#uncomment below line to run regularly
#function_call()