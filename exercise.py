print ("add your number")
inpnum = input()
print ("you entered", int(inpnum)+10)

print ("enter first number")
n1 = input()
print ("enter second number")
n2 = input()
print ('sum of these number is', int(n1) + int(n2))


print ("enter your first number")
T1=input()
print("enter your second number")
T2=input()
print ("multiplication of these two number is", int(T1)*int(T2))

mystr = "Akash is a Good boy"
# print (mystr)
#
# print(mystr[4])
# print(mystr[0:6]) #the latter alphabet in 0:6 the 6th one is left out of the print and 0-5 gets printed
# print(len(mystr))
# print(mystr[0:80]) #80 alphabets are not present still no error on the whole str gets printed instead
# print(mystr[0:10:2])
# print(mystr[::]) #default step is 1 and middle one stays the LEN and will print the whole lin
# print(mystr[::-1]) # string is reversed alphabets


print(mystr.isalnum()) # output is false becz the the statement has spaces and it will come true if the mystr=akashisagoodboy

print(mystr.isalpha) #still false as its not a alhanumeric word sentence
print(mystr.endswith("boy"))  #endswith boy is true as its right
print(mystr.endswith("bods"))
print(mystr.startswith('akash')) #true thing
print(mystr.count("b"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.find("is")) #"is" is starting from 6th index
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))  #the latter alphabets after the , is the one which replaces the former one
