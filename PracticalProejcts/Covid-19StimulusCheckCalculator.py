MaxCashForSingle= 1200
MaxCashFormarried = 2400

filling_status = int(input('Enter your filling status,  S for single or M for married: ')).capitalize

income = int(input('Enter your 2018 Federal Income: '))

children = int(input('How many dependents under the age of 17 do you have?: '))

CashForChildren = 500 * children
# reminder that *args and kwargs can be used  for a varrying number of aguments 
def stimulusCheck(*args):
    if filling_status == 'S':
        print('your stimulus check will mostlikely be: ',round(MaxCashForSingle - ((income - 75000)/100)+ CashForChildren))
    else:
        print('your stimulus check will mostlikely be: ',round(MaxCashFormarried -((income - 150000)/100)+CashForChildren))

def maximum_posible_stimulusCheck(*args):
    if filling_status == 'S':
        print('Your stimulus check will most likely be :',MaxCashForSingle + CashForChildren)
    else:
        print('Your stimulus check will most likely be :',MaxCashFormarried + CashForChildren)


# if you don't qualify for the stimulus check but have children
def minimum_stimulusCheck(*args):
    print('your stimulus check will mostlikely be:', CashForChildren)

if (filling_status == 'S' and income > 99000) or (filling_status == 'M' and income > 198000):
        minimum_stimulusCheck()

elif (filling_status == 'S' and income > 75000) or (filling_status == 'M' and income > 150000):
        stimulusCheck()

else:
    maximum_posible_stimulusCheck()


