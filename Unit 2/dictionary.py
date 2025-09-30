#****** Dictionary ******

#=>Dictionary are used to store data values in key-value pairs.
#=>It is a collection of ordered, changeable and doesn't allow duplicates.
#=>Dictionaries are written with curly brackets, and have key and values.

student=['Dia',3,'CSE']
# print(student)

student={
    'name':'Dia',
    'sem':3,
    'Course':'CSE'
}
# print(student)
# print(type(student))

#If we do this with list then we can't understand what the first value indicates and what second indicates.

fruits_price=[("Mango",150),('Apple',120),('Cherry',200)]
# for fruits,price in fruits_price:
    # print(fruits,price)
    
fruits_price={
    "Mango":150,
    "Apple":120,
    "Cherry":200
}
# print(fruits_price)


students={
    #Empty dictionary.
}

# print(students)

student={
    'name':'Dia',
    'sem':3,
    'Course':'CSE'
}
# print(student["name"])


# for k in student:
#     print(k) #We can access keys.

# for v in student:
#     print(student[v])    #We can access values through this.

# for key,values in student.items():
#     print(key,values)



#****** Adding a key-value pair in dictionary ******

student["cgpa"]=8.3
# print(student)

#Updating a value

student.update({"sem":5})
# print(student)


#****** Dictionary Methods *****
#=>pop(x): It removes the item with specified name.We pass the key inside the pop()
#=>del: It removes the item with specified name.
#=>clear(): empties the dictionary.
#=>popitems(): 
#=>dict.keys(): Returns all the keys.
#=>dict.values(): Returns all the values.
#=>dict.items(): Returns key-value pairs as tuples.
#=>dict.get(key,default): Safely gets value, returns default if key not found.
#print(student.get("grade","Not Assigned"))
#=>dict.copy(): Returns a shallow copy(same type).
#=>dict.setdefault(key,default): Returns the value if key exists, otherwise adds key with default value.

student={
    'name':'Dia',
    'sem':3,
    'Course':'CSE',
    'sample':234
}

# student.pop("Course")
student.popitem() #pops last key-value pair.
# del student['name']
# student.clear()
print(student)

student={
    'name':'Dia',
    'sem':3,
    'Course':'CSE',
    'grade':'A+'
}

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("nam",9))
# print(student.get("sgpa","Not"))
# print(student.get('grade',"Not assigned"))

student={
    'name':'Dia',
    'sem':3,
    'Course':'CSE',
    'grade':'A+'
}

student.setdefault("grade","0")
# print(student)
student.setdefault("email","0")
# print(student)


# ****** Practice Questions ******

#Q1 
employee={"id":101,"name":'John',"salary":200000}
# print(employee)
employee.update({"salary":60000})
employee["dept"]="HR"
# print(employee)

#Q2
laptop={"name":'Omen',"processor":'i914HX',"OS":'Linux'}
#print(laptop["name"])
#print(laptop.get("OS","No"))

#Q3
# text=input("Enter a string: ")
# word_count={}
# for word in text.split():
#     word_count[word]=word_count.get(word,0)+1

# print(word_count)    
        
        
#Q4
# max=0
# min=100
# c=""
# scores={"Alice":88,"Bob":75,"Charlie":92,"David":60} 
# print(scores)
# for i in scores:
#     if(scores[i]>max):
#         max=scores[i]       
#     if(scores[i]<min):
#         c=i
# print("Maximum marks are ",max)
# scores.pop(c) 
# print(scores)
# scores["Eve"]=81
# print(scores)