
#a calculator
def calculator():
    while True:  # takes the input for the calculator and also  whether it is +,-,*,/ and also continuously asks for the new input after one round of calculations
        try:
            num = int(input("Enter a number: "))
            operator = input("Enter an operator: ")
            num2 = int(input("Enter a number: "))
            #it checks for the operator selected and chooses the one it runs
            if operator == "+":
                print(num + num2)
            elif operator == "-":
                print(num - num2)
            elif operator == "*":
                print(num * num2)
            elif operator == "/":
                if num2 != 0:   #checks if the number is 0 and if it is it will not run
                    print(num / num2)
                else:
                    print("Division by zero is not allowed")  #this prints if the number is 0
            else:
                print("Invalid operator") #this prints if the operator is not +,-,*,/

        except ValueError:
            print("Invalid input. Please enter a valid number.") #invalid input is not run so it asks for a valid number
        
        done = input("Do you want to continue (yes/no)? ").lower() #asks if you want to continue
        if done != "yes":
            break

calculator()

