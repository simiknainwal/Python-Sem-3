while(True):
    try:
        age=int(input("Enter age:"))
        if age==0:
            raise ValueError("Age can't be zero")
        elif age<0:
            raise ValueError("Age is less than 0")
        elif age>120:
            raise OverflowError("Age is over 120")
        
        else:
            print(age)
    
    except (ValueError,OverflowError) as e1:
        print("Error is ",e1)