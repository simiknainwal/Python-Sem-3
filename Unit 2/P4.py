names=[]
def input(names):
    names=["John","Antony","Bob","Antony","David"]

def frequency(names):
    print(names.count("Alice"))

def delete(names):
        names.remove("Antony")

def add(names):
    names.insert("Anthony")
    
def display(names):
    print(names)

while(True):
    choice=int(input("Enter choice:")) 
    if(choice==1):
        input(names)
    if(choice==2):
        frequency(names)
    if(choice==3):
        delete(names)
    if(choice==4):
        add(names)
    if(choice==5):
        display(names)    
    if(choice==6):
        print("Exiting")
        break                            