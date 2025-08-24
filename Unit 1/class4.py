# ****** Functions ******
def sum(a,b):
    return a+b

# print(sum(b=6,a=9))

def student(name,sem,sgpa):
    print(name,sem,sgpa)
    
student("Simik",3,9.4) #Positional arguments
student(sgpa=4,name="Sim",sem=6)  # Keyword arguments