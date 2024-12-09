import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
option= input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

# ERROR/validation checks
if option == "investment":
    print("You have selected investment. This will calculate the amount of"
          "you'll earn on your investment.")
elif option == "bond":
    print("You have selected bond. This will calculate the amount you'll"
          "have to pay on a home loan.")
else:
    print('you have entered invalid option')


# investments calculations
if option == "investment":
    P_for_investments= int(input('how much money will you be depositing '))
    R_for_investments= float(input('what is the interest rate'
                                   '(please enter only the number) '))
    R_for_investments = R_for_investments/100# Converting to decimal to use in formula
    T_for_investments= int(input('how many number of years are going to invest '))
    interest= input('is it simple or compound interest ').strip().lower()
    
    if interest == 'simple':
        print('your investment is '
               + str(P_for_investments *(1 + R_for_investments*T_for_investments)))
    
    elif interest == 'compound':
        print('your investment is ' 
              + str(P_for_investments * math.pow((1+R_for_investments),T_for_investments)))

# Bond calculations 
if option == "bond":
 P= float(input('what is the present value of your house '))
 I= float(input('what is the interest rate(enter a number only) '))/ 100 / 12  # Convert to monthly rate as a decimal
 N= float(input('how many years will it take to repay the bond on your house '))
 print('your repayment amount a month is ' + str((I * P)/(1 - (1 + I)**(-N)) ))



    
