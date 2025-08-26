# Consider a list with five differnet celsius values.Convert all the celcius values into Farenheit.Using List Comprehension.
# Farenheit=(9/5)*celcius + 32

l=[23,24,45,34,12]
newList=[(9/5)*i+32 for i in l]
print(newList)
