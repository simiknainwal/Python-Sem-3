num=[]
for i in range(10):
    n=int(input("Enter the number:"))
    num.append(n)

for i in range(10):
    if num[i]%3==0:
        num.remove(num[i])    
        
print(num)        