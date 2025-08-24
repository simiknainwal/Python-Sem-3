#***** String Functions ******


# # str="\t\t\tGraphic Era     "
# # print(str)
# # print(str.lstrip())# trims the space at extreme left
# # print(str.rstrip())# trims the space at extreme right
# # print(str.strip())#trims the space at both the sides


# str="Red Green Blue Yellow"
# print(str.split("Blue"))#divides the string into two parts from a separator string: one part contains Red and Green while the other contains Yellow
# str1="Graphic Era Deemed University"
# print(str1.split("Nothing"))
# #Note: if the separator string is not present in the string then whole string is printed as it is

# print(str.partition("e"))# divides the string into three parts: first part contains the left side from separator string, second part is the separator string only and the third part contains the right side from separator string

# str2="."
# print(str2.join(str)) # joins str2 after each character of str except last 

#****** String conversion ******

# s="SIMIK NAINWAL"
# s1=s.upper()# capitalizes all the characters
# s2=s.lower()# change all the characters to lower case
# s3=s.swapcase()# changes the lower case characters to upper and vice-versa
# s4=s.capitalize()# only first character capitalizes
# #Note: It changes the first character to upper case and converts the other characters to lower case
# s5=s.title()# Starting character of each word becomes capital and convert the others to lower case
# print(s)# As we know string is immutable so upper() doesn't change the original string instead it makes a copy of that string 
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)




#****** String slicing ******

str="Simik"
print(str[0:2]) # Si
print(str[-5:-2])# Sim
print(str[1:5:1])# str[start:stop:step]   imik