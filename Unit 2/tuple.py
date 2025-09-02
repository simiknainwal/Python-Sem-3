# ***** Tuple *****
#=>Tuples are ordered and immutable or they can't be modified.
#=>wriiten in () round brackets.
#=>Allow duplicate elements.
num=(1,2,3,4,5)
# print(num)
# print(type(num))

t=()#Empty tuple
# print(t)

num1=(10)#Python interpreter considers it as a integer value
num2=(10,)#It considers it as tuple
# print(num2)
# print(type(num1))
# print(type(num2))

num=('A',)
# print(type(num))

num=(1,2,3,4,5)
# print(num[::-1])# In the backend starting index is (length of variable) -1  
# 4>-1; 4--

# for i in num:
#     print(i)

# for i in range(0,len(num)):
#     print(i,num[i])

fruits=("Apple","Cherry","Kiwi","Berry")
# fruits[2]="Orange"#error
#To insert we have to do workaround=> first we convert tuple into list and then back into tuple.
fruitsl=list(fruits)
fruitsl.insert(2,"Simik")
fruits=tuple(fruitsl)
# print(fruits)

#Consider the given tuple cities=("Mumbai","Dehradun","Delhi","Bangalore","Chennai","Raipur").Find the index of city "Dehradun" and remove it using pop() and print the remaining values in the tuple

cities=("Mumbai","Dehradun","Delhi","Bangalore","Chennai","Raipur")
citiesl=list(cities)
# for i in range(0,len(citiesl)):
#     if citiesl[i]=="Dehradun":
#         x=i
x=citiesl.index("Dehradun")#To find the index of the word.
citiesl.pop(x)
cities=tuple(citiesl)
# print(cities)        

# num=(1,2,1,4)
# print(num)

x=(1,2,3)
y=(4,5,*x,6)#'*' unpacks the values of x and merges a tuple to another.
print(y)

numd=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
# print(numd[0])#prints the whole row
# print(numd[0][2])

#Also valid in list
# numdl=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(numdl)

# input = (1,2,3), element =4
#output = (1,2,3,4)

# num=()
# numl=list(num)
# x=(int)(input())
# for i in range(0,x):
#     e=(int)(input())
#     # numl.insert(i,e)
#     numl.append(e)
# print(numl)
# n=(int)(input())
# # numl=list(num)
# numl.append(n)
# num=tuple(numl)
# print(num)
