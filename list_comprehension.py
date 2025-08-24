# Update in a list.
# alpha=['a','b','c','d','e','f']
# print(alpha)
# alpha[1]='B'
# print(alpha)
# alpha[2:4]=['C','D'] # replaces at index 2 and 3.
# print(alpha)

# ****** List Comprehension ******
# It offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newList=[expression(element)for element in oldList if condition]

# num1=[]
# for i in num:
#     x=i+10
#     num1.append(x)
# print(num)
# print(num1)    

num=[1,2,3,4,5,6]
# num1=[i+10 for i in num] #'if' condition is optional.
# i+10 is expression rest all is looping statement.
# looping statement traverses through the list and the value is changed according to condition and the expression.
num1=[i for i in num if(i%2==0)]
# print(num)
# print(num1)


values=['a',1,'b',2,'c',3,'d']
#Write code to print list with only the num
# newList=[i for i in values if(i.isdigit())]
# print(newList)

# newList=[i for i in values if(type(i)==int)]
# newList=[i for i in values if(str(i).isnumeric())]
newList=[i for i in values if not str(i).isalpha()]
print(newList)