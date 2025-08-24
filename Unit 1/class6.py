# ****** Exception Handling continues ******
# Exception means an unusual condition in a program resulting in the interruption in the flow of a program.
# Whenever an exception occurs the program stops the execution and thus the further code is not executed.
# 1) ZeroDivisionError: occurs when a number is divided by zero.
# 2) NameError: when name is not found.
# 3) IndexError: when you are trying to access an element in a list,tuple etc. that is outside the valid range of index.
# 4) IOError: when input/output operation fails. 
# 5) TypeError: when operation or function is applied to an object of wrong type.
# 6) KeyError: in dictionary

# Syntax of try, except and else block:
# # try:
#     block of code 
#   exception Exception1:
#   else:
#           run this code when there are no exceptions  
#           other block 


#Write a python program to read two numbers, perform division operation for two numbers and handle the exceptions properly with try, except and else block.
# while(True):
#     try:
#         num1=int(input("Enter a number:"))
#         num2=int(input("Enter a number:"))
#         div=num1/num2
#     except (ZeroDivisionError,ValueError) as e1:
#             print("Exception is ",e1)    
#     else:
#         print(div)
#     print("Next Statement 1")                
    
    
    
    
#Syntax of try, except, else and finally block:
# try:
#     block of code 
#   exception Exception1:
#   else:
#           run this code when there are no exceptions  
# finally:    Always run this code


# cities=["Bengaluru","Dehradun","Delhi","Romania","Mumbai"]

# while(True):
#     try:
#         index=int(input("Enter the index:"))
#         print(cities[index])
#     except (ValueError,TypeError,IndexError) as e1:
#             print("Error is ",e1)
#     else:
#             print("Else Block")
    
#     finally: 
#         print("This is final")            



# ****** Generate an exception ******

while(True):
    try:
        num=int(input("Enter a number:"))
        if num>0:
            print("Positive number is ",num)
        else:
            raise ValueError("Number must be positive") #Generating a message for our exception
    except ValueError as e1:
        print("Error is ",e1)
                
# raise keyword is used to generate our own message                 