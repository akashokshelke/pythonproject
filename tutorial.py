grocery = ["harpic","vim bar","tooffes","condoms","watches", 56]  #numbers can be put as in not "" needed
print(grocery)
print (grocery[1])
print (grocery[3])
print(grocery[5])
numbers = [1,3,5,5,6,6,7,3,4]
print(max(numbers))#similarly min can also be used same way
numbers.append(7) #in the end of the series it adds 7 as a value
numbers.append(74) #any digits can be added in series using this code  .append() simulaneously

# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse() #reverses sorted numbers if sort is written earlier

#this is called slicing , and will return a modified list back and original stays same but if "sort,reverse" used then,original is also changed
print(numbers[1:]) #will print every value
print(numbers[0:5])



numbers = []           #so this way you can also create a continuous list in  this way in the program
numbers.append(23)
numbers.append(273)
numbers.append(23)




numbers = [1,3,5,5,6,6,7,3,4]
print(numbers)
numbers.insert(1,66)
numbers.insert(4,245)
numbers.insert(3,654)
print(numbers)
numbers.remove(6)   #6th digit is removed whatver it is..6 is the index
print (numbers)


numbers.pop(4) #this will remove the 4th digit or whatever we assign
print(numbers)



