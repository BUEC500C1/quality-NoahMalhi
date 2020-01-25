def conv_to_rom(arab_in):
    if arab_in >= 1000:
        print('M', end = '')
        return (arab_in - 1000)
    elif arab_in >= 900:
        print('CM', end = '')
        return (arab_in - 900)
    elif arab_in >= 500:
        print('D', end = '')
        return (arab_in - 500)
    elif arab_in >= 400:
        print('CD', end = '')
        return (arab_in - 400)
    elif arab_in >= 100:
        print('C', end = '')
        return (arab_in - 100)
    elif arab_in >= 90:
        print('XC', end = '')
        return (arab_in - 90)   
    elif arab_in >= 50:
        print('L')
        return (arab_in - 50)
    elif arab_in >= 40:
        print('XL', end = '')
        return (arab_in - 40)
    elif arab_in >= 10:
        print('X', end = '')
        return (arab_in - 10)
    elif arab_in >= 9:
        print('IX', end = '')
        return (arab_in - 9)
    elif arab_in >= 5:
        print('V', end = '')
        return (arab_in - 5)
    elif arab_in == 4:
        print('IV', end = '')
        return (arab_in - 4)
    elif arab_in >= 1:  
        print('I', end = '')
        return (arab_in - 1)
    else:
        return 0

arab_in = int(input("Enter a number : "))
for x in range(arab_in):
    arab_in = conv_to_rom(arab_in)
    if arab_in == 0:
        break
    
print('')
if arab_in < 0:
        print ("Enter value greater than 0")
print('Done')