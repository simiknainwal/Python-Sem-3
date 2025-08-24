l=['Anirrudh',2,3,'simik','sarthi']
while(True):
        try:
            index=int(input())
            add=99+l[index]
            print(l[index])
        except IndexError as e:
            print("Error is: ",e)   
        except TypeError as e2:  
            print("Error is: ",e2)     