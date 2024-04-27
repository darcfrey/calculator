"""num1 = input("enter number;")
num2 = input("enter second number;")
#addition
sum = num1 + num2
print("Sum:", sum)
#minus
minus = num1 - num2
print("minus:", minus)  
#multiplication
multiplication = num1 * num2
print("multiplication:", multiplication) 
#division
division = num1 / num2
print("division:", division)  
#modulus
modulus = num1 % num2
print("modulus:", modulus) 
name = input("enter name;")
print(name)


#name to be accepted
accepted_name = "opoola yusuf"  
user_name = input("Enter your name: ") #user name input
 #code to check
if user_name == accepted_name:  
    print("Access granted!")
else:
    print("Access denied.")

#get age from user
age = int(input("enter your age: "))
if 0<= age <= 3:
    print("infant") #print infant for any nymber lower or equal to three
elif 4 <= age <13:
    print("child") #print child for any number greater than or equal to 4 but lower than 13
elif 13 <= age <20:
    print("teen") #print teen for any number greater than or equal to 13 but lower than 20
elif 20 <= age <40:
    print("adult") #print adult for any number greater than or equal to 20 but lower than 40
else:
    print("elder" if 40 <= age <=90 else "to old to matter") #print elder if greater than 40 but less than 90 anything higher prints to old to matter 


name ="emmanuel"
letter= input("enter letter")
if letter in name:
    print("m is in emmanuel")
else:
    print("the letter is absent")


A=5
B=4
C=3
D=2
E=1
F=0
course_unit1= input ("ics105 unit :")
course_unit2= input ("ics105 unit :")
course_unit3= input ("ics105 unit :")

#enter math inputs 
a= int(input("enter a: "))
b= int(input("enter b: "))
c= int(input("enter c: "))
quad_eq1= -b +(((b**2)-(4*a*c))/2*a)**0.5
quad_eq2= -b -(((b**2)-(4*a*c))/2*a)**0.5
print(quad_eq1)
print(quad_eq2)


i=0
while i<=5:
    print(i)
    i=i+1

print("even numbers from 1 to hundred")
for i in range(2, 100, 2):
    print(i, end=" \n") 
    # Print even numbers from 1 to 100

print("Odd numbers from 1 to 100:")
for i in range(1, 100, 2):
    print(i, end=" \n") 
# Print odd numbers from 1 to 100

fruit=["banana","apple","orange","pineapple","pear"]
fruit.append("avocado")
print(fruit)


A=5
B=4
C=3
D=2
E=1
F=0
total_grade= (grade)
total_unit= unit

grade=input("enter your grade :")
unit=int(input("enter your unit :"))

if grade == 'A':
            grade_point = 4
elif grade == 'B':
            grade_point = 3
elif grade == 'C':
            grade_point = 2
elif grade == 'D':
            grade_point = 1
else:
            grade_point = 0
           
cgpa=float(total_grade/total_unit)

print("your cgpa is :", (cgpa) )
# import random

#my_str = [2,"hi" ,"nigga"]
#print(my_str[2])

user = ["darcfrey", "bumblebig", "steven", "emmanuel", "samuel"]
username = input("your username :")
while True :
    if username in user :
        print("access granted")
    else :
        print ("invalid parameters") 
        break   """
#a ="yo"
#b = "how you doing"
#c = "im good"

#print("{} {} {}".format(a,b,c))

"""y ="yo my nigga"
print(y.replace("m", "d"))
print(len(y))
print(y.index("m"))
print("my" in y)
for x in range (1,101,1):
   print(x"is odd")

y = [1,2,3,4,5,6]
y.pop(3)
print(y)
#authentication system that gives access to 5 users in a list
users= ["yusuf""bumblebig""steven""samuel""emmanuel"]
password = ["yusuf""bumblebig""steven""samuel""emmanuel"]
username=input ("your user name")
password=input("your password")
if username in users:
  print("access granted")

def is_palindrome(word):
  return word == word[::-1]

# Test the function
word = input("Enter a word: ")
print(is_palindrome(word))"""


# import random

# def number_guessing_game():
#     number_to_guess = random.randint(1, 1000)
#     guess = None
#  #this starts a  loop that will continue until the user guesses the number
#     while guess != number_to_guess:
#         guess = int(input("Guess the number (between 1 and 1000): "))
# # print you guessed the number
#         if guess == number_to_guess:
#             print("Congratulations! You guessed the number.")
#           #check absolute distance between the guess and the number to guess and print a hint number higher or lower within a distance of 10
#         elif abs(guess - number_to_guess) <= 10:
#             print("You're very close! Guess a bit ", end="")
#             if guess < number_to_guess:
#                 print("higher.")
#             else:
#                 print("lower.")
#               #check absolute distance between the guess and the number to guess and print a hint number higher or lower within a distance of 50
#         elif abs(guess - number_to_guess) <= 50:
#             print("You're close! Guess ", end="")
#             if guess < number_to_guess:
#                 print("higher.")
#             else:
#                 print("lower.")
#               #number very much higher than the number to guess
#         elif guess < number_to_guess:
#             print("You're far off! Guess higher.")
#           #number very much lower than the number to guess
#         else:
#             print("You're far off! Guess lower.")

# # Start the game
# number_guessing_game()


#build a simple arithmetic calculator that takes in input
#the calculator uses the eval function to run
# def calculator():
#     while True: 
#         calc = input("Enter calculation (or 'done' to exit): ") #takes user inputt if user input is done ends the operation
#         if calc.lower() == 'done': #changes the user input text for done to lowercase  to run the code
#             break #stops the operation loop

#         try: 
#             calculation= eval(calc) #runs the operation using the evaluation function by taking the operation in
#             print("Result:", calculation) # prints the ran calculations
#         except NameError as str:
#             print("Invalid input. Please enter a valid number.")
# calculator()


# #a calculator
# def calculator():
#     while True:  # it takes the input for the calculator and also the whether it is +,-,*,/ and also continously ask for the new input after one round of calculations
#         try:
#             num = int(input("Enter a number: "))
#             operator = input("Enter an operator: ")
#             num2 = int(input("Enter a number: "))
#             #it checks for the operator selected and chosses the one it runs
#             if operator == "+":
#                 print(num + num2)
#             elif operator == "-":
#                 print(num - num2)
#             elif operator == "*":
#                 print(num * num2)
#             elif operator == "/":
#                 if num2 != 0:   #checks if the number is 0 and if it is it will not run
#                     print(num / num2)
#                 else:
#                     print("Division by zero is not allowed")  #this prints if the number is 0
#             else:
#                 print("Invalid operator") #this prints if the operator is not +,-,*,/

#         except ValueError:
#             print("Invalid input. Please enter a valid number.") #invalid input is not run so it asks for a valid number
        
#         done = input("Do you want to continue (yes/no)? ").lower() #asks if you wnat to continue
#         if done != "yes":
#             break

# calculator()



#oop

from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer

def generate_response(model, tokenizer, input_text, max_length=100):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    model, tokenizer = load_model()
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(model, tokenizer, user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

    
    

    
    
    


 





