# ***** Variable-length Positional Arguments *****

def Total(*args):
    sum=0
    print(type(args))
    print(args)
    for i in args:
        sum=sum+i
    print(sum)  
# Total(1,2,3)  
# Total(1,2,3,999,5)  


def greetings(msg,*args):# '*' to unpack the value.
    for i in args:
        print(msg,i)
        
# greetings("Good Morning","Simik","Sarthi","Anirrudh")  
# greetings("Namaste","Hello")      


# ******Variable-length Keyword Arguments ******
#Sometimes number of keyword arguments passes to a function is not certain. So we use variable-length keyword arguments using **kwargs.
#All the arguments has the value so use variable-length keyword arguments otherwise use variable-length positional args.
def student(**kwargs):  # '**' indicates unpacking key and value.
    for key,value in kwargs.items():
        print(key,value)
        # print(kwargs) key : value pairs 
# student(name="Sarthi", sgpa=10, sem=3)        
# student(name="Simik",sem=3,sgpa=9)



# ****** Exceptional Handling ******

while(True): 
    try:     # Include only those statements inside "try" which might raise an exception.
        a=int(input())
        b=int(input())
        div=a/b
        print(div)
    except ZeroDivisionError as e:# shows the error name for the input values.
        print("Error is: ",e)  
    
    except ValueError as e2:
          print("Error is: ",e2)  
          
    except: print("Other error")          
    print("Next Line 1")
    print("Next Line 2")