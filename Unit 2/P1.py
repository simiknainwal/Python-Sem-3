# Write a python program to perform the following operations:
#1) Create an empty list with name "Cricketers"
#2) Read 'n' of cricketer's names and add those values in list.
#3) Display the list in reverse order.
#4) Display the name of cricketers whose name is containing more than 8 characters.

cricketers=[] #Empty List
n=int(input("Enter the number of cricketers:"))
def read(cricketers):
        for i in range(n):
            name=input("Enter the name:")
            cricketers.append(name)

def display(cricketers):
    # print(cricketers[::-1])
    print("List of cricketers with more than 8 characters:")
    for i in range(n):
        if len(cricketers[i])>8:
            print(cricketers[i])
read(cricketers)
display(cricketers)
