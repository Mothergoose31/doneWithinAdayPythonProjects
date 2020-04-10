MaxCashForSingle= 1200
MaxCashFormarried = 2400

filling_status = str(input('Enter your filling status,  S for single or M for married: '))

income = int(input('Enter your 2018 Federal Income: '))

children = int(input('How many dependents under the age of 17 do you have?: '))

CashForChildren = 500 * children
# reminder that *args and kwargs can be used  for a varrying number of aguments 
def stimulusCheck(*args):
    if filling_status == 'S':
        print('your stimulus check will mostlikely be: ',round(MaxCashForSingle - ((income - 75000)/100)+ CashForChildren))
    else:
        print('your stimulus check will mostlikely be: ',round(MaxCashFormarried -((income - 150000)/100)+CashForChildren))



