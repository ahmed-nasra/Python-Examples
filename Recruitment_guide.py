age=int(input('candidate age'))
experience= int(input('number of years experience'))
if age >=18 and age<=26:
    if experience <=4:
        print('accepted')
    else:
        print('rejected')
else:
    print('not eligible')
