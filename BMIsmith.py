# This program will allow users to input their name, weight and height. Then the program will calculate their BMI based off of the data entered.
import time,sys

print("BMI Calculator\n") # shows user title of program

while True:
   
    name = str(input("What is your name? (Type 'end' to exit)\n")) # asks for their name
    
    if name=='end':  # ends program if user enters the word end                           
        sys.exit()
        
    weight = int(input("Please enter your weight in pounds:\n")) # asks user for weight

    height = int(input("Please enter your height in inches:\n")) # asks user for their height

    BMI = (weight / height ** 2) * 703  # calculates the BMI
    BMI = round(BMI, 2)  # Rounds BMI two decimal places

    if BMI < 18.5: # prints the users BMI and their weight status based off the calculation
        print ("\nYour BMI is " + str(BMI) + "\nYour weight status is: underweight\n") 

    elif BMI >= 18.5 and BMI <= 24.9:  # prints the users BMI and their weight status based off the calculation
        print("\nYour BMI is " + str(BMI) + "\nYour weight status is: normal\n")

    elif BMI >= 25.0 and BMI <= 29.9:  # prints the users BMI and their weight status based off the calculation
        print("\nYour BMI is " + str(BMI) + "\nYour weight status is: overweight\n")

    elif BMI > 30:  # prints the users BMI and their weight status based off the calculation
        print("\nYour BMI is " + str(BMI) + "\nYour weight status is: obese\n")
        
time.sleep(5) 
