import time
#start of project 
print('welcome to our Bank ')
# take the card number from user
cardNumber=input('plz enter the card Number')
pin=input('plz enter ur pin')
#create an list as indector for pin matrix
pins=['1023','1233','6523']
# create an tuple as indecator to exist acount
accountstuple=('1','2','3')
#create an list as indecator or the amount of money in account  in le
money={'1':12000,'2':4000,'3':3000000}
#cheak if card number is valid
if cardNumber in accountstuple and pin in pins[accountstuple.index(cardNumber)]:
    print('moument plz')
    time.sleep(1)
    print('welcome Sir')
    n='Y'
    while n=='Y':
        # start to take the operation that user want to exqute in Atm
        operation=input(' to withdrow press 1 / to deposit press 2   ')
        # if the user choose to withrow amount enter the withdrow system
        if operation=='1' :
        # take the caranc from user to calculate the defrance in currency
            currency=input('plz enter currency   :   $    /E  /le   ')
            if currency == '$':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]-=(int(AM)*30)
                 print('Done ... ur amount now  =  ' ,money[cardNumber])
                 n=input('for anather operation press Y   / for end process press N   ')
            elif currency == 'E':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]-=(int(AM)*34)
                 print('Done ... ur amount now  =  ' ,money[cardNumber])
                 n=input('for anather operation press Y   / for end process press N   ')
            elif currency == 'le':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]-=int(AM)
                 print('Done ... ur amount now  = %d  le ' ,money[cardNumber]) 
                 n=input('for anather operation press Y   / for end process press N   ')
        elif operation=='2' :
            currency=input('plz enter currency   :   $    /E  /le')
            if currency == '$':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]+=(int(AM)*30)
                 print('Done ... ur amount now  =  ' ,money[cardNumber])
                 n=input('for anather operation press Y   / for end process press N   ')
            elif currency == 'E':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]+=(int(AM)*34)
                 print('Done ... ur amount now  =  ' ,money[cardNumber])
                 n=input('for anather operation press Y   / for end process press N   ')                 
            elif currency == 'le':
                 AM=input('plz enter the amount of money')
                 # calculate the amount using the defrance in currency
                 money[cardNumber]+=int(AM)
                 print('Done ... ur amount now  = %d le ' ,money[cardNumber])
                 n=input('for anather operation press Y   / for end process press N   ')                 
        else :
            print('invalid operation')
            n=input('for anather operation press Y   / for end process press N   ')
else :
    print('moument plz')
    time.sleep(1)
    print('invalied card number')

