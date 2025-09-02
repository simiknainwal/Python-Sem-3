#***** Set *****
#=>Sets are unordered and doesn't allow duplicate values.
#=>Sets can only remove and add.

# num={1,2,3,4,5,3,2}
# print(num)
# print(type(num))

a={11,22,33,44,55,22}
b={55,44,33,22,11}
c={33,44,22,55,11}
# print(a)
# print(b)
# print(c)
#We get elements in different arrangement because the elements are stores in hash key form
#For repeated values hash keys is same so we don't get duplicate values.
#We can't apply slicing
s={11,22,33,44,55}
# for i in s:
    # print(i)
    
    
#****** Set Methods ******
#s.add(x)
# s.update(t)=>To join two sets
# s.clear()
# s.remove(x)
# s.discard(x)  Check the difference between remove and discard.

#The below methods gives output in true or false
# s1.issuperset(s2)
# s2.superset(s1)
# s1.isdisjoint(s2)

#union()
#intersection()
#difference()
#symmetric_difference()

num={1,2,3,4,5}
num1={6,7,8,9}
# num.update(num1)#In the argument we are passing a set
# num.add(3) # in argument we are passing a number
# num.clear()
# num.remove(6) #gives error if value is not in the set
num.discard(6)#doesn't give the error if value is not in the set
# print(num)# the value gets overwrited.


batsmen={"Shubhman Gill","Kohli","Dhoni","Rohit","Hardik","Jadeja"}
bowlers={"Siraj","Hardik","Jasprit","Krishna","Jadeja"}
print(batsmen.union(bowlers))
print(batsmen.intersection(bowlers))
print(batsmen.difference(bowlers))
print(batsmen.symmetric_difference(bowlers))
# print(batsmen & bowler) Also does the intersection operation

