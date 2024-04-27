build a simple arithmetic calculator that takes in input
the calculator uses the eval function to run
def calculator():
    while True: 
        calc = input("Enter calculation (or 'done' to exit): ") #takes user inputt if user input is done ends the operation
        if calc.lower() == 'done': #changes the user input text for done to lowercase  to run the code
            break #stops the operation loop

        try: 
            calculation= eval(calc) #runs the operation using the evaluation function by taking the operation in
            print("Result:", calculation) # prints the ran calculations
        except NameError as str:
            print("Invalid input. Please enter a valid number.")
calculator()









    
    

    
    
    


 





