# print("hello")
l=list("Hello")
# print(l)
print(5//1.5)#prints the integer output
num=int(input("Enter a number:\n"))
if num%2==0:
    print("Even")
else:
    print("Odd")    
   
# ***** Match Case *****
unit=int(input("enter the units:"))
match unit:
        case unit if unit<=100:
            bill=0
        case unit if unit>100 and unit<=200:
            bill=(unit-100)*5 
        case unit if unit>300:bill=(unit-200)*10 +500
print(bill)                       