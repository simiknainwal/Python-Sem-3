def push(stack):
    if(len(stack)==4):
        print("Stack overflow")
    else:    
        value=(int)(input("Enter the value:"))
        stack.append(value)
    
def pop(stack):
    if len(stack)==0:
        print("Underflow")
    else:
        
        stack.pop()
            
    # print("POP")   
    
def display(stack):
    print(stack[::-1])    
     
stack=[]
print("Press 1. PUSH 2. POP 3. DISPLAY 4. Exit ")
while(True):
    choice=int(input("Enter your choice:"))
    if(choice==1):
        push(stack)
    if(choice==2):
        pop(stack)
    if(choice==3):
        display(stack)        
    elif(choice==4):
        print("Exitting")
        break    