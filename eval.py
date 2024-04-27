#build a simple arithmetic calculator that takes in input
#the calculator uses the eval function to run
def calculator():
    while True: 
        calc = input("Enter calculation (or 'done' to exit): ") #takes user input if user input is done ends the operation
        if calc.lower() == 'done': #changes the user input text for done to lowercase  to run the code incase the done is typed in uppercase
            break #stops the operation loop

        try: 
            calculation= eval(calc) #runs the operation using the evaluation function by taking the operation in
            print("Result:", calculation) # prints the ran calculations
        except NameError as str:  #this check for errors in user input for string values and prints the bellow statement
            print("Invalid input. Please enter a valid number.")
calculator()









    
    

    
    
    


 





