#****** List ******
#->list can store heterogeneous data values.
#->Can store duplicates.
#->Are mutable i.e. can be modified or changed.
alpha=['a','b','c','d','e','f','g','h','i']
# print(alpha)
# print(type(alpha))
# print(alpha[0:4:1])# start:stop:increment
# print(alpha[-4])
# print(alpha[-4:-1])#-4<-1 is true i=-4;-4<-1;i++
# print(alpha[1:-3])

# print("Full list: ",alpha)
# print("Based on condition: ",alpha[-6:-1])
# print("Based on condition: ",alpha[::-1])
# print("Based on condition: ",alpha[-1:0:-1])
# print("Based on condition: ",alpha[2:-3])# 2:6 , -3+length(alpha) i.e. negative value +length(list)
# print(alpha[-3:-1])# 6:8 i.e.  negative index+length(alpha)

# for i in range(len(alpha)):
    # print(i)# 'i' is pointing to the element.
    # print(alpha[i],end=" ")# 'i' is pointing to indexes.
    
    

# ****** Adding the list elements ******
# We can use append(obj), insert(index,obj) and extend(obj)

# val=input("Enter the element:")
# print(alpha)
# alpha.append(val)
# alpha.append("YY")
# print("After append:",alpha)

# num=[3,4,5,6]
# num.insert(0,999)
# print(num)

# alpha=['a','b','c']
# num=[1,2,3]
# alpha.extend(num)
# print(alpha)


# ***** Remove the elements in the list *****
#=> remove(obj), pop(index), "del" keyword and clear()

alpha=['a','b','c','d','e','f','g','h']
print(alpha)
# alpha.remove('d')
alpha.pop()# removes the last index
# alpha.pop(3)
del alpha[1]
del alpha # alpha is deleted from the memory so we will get error.
# alpha.clear() # clears the list i.e. empty list
print(alpha)
