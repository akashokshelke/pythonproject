print("numbers")
#Dictionary is nothing but key value points.
d1 = {}
print (type(d1))
d2 = {"harry":"burger", "akash":"cheese" , "ashwar" :"pavbhaji"}
print(d2)
print(d2["harry"])
print (d2["ashwar"])

d1 = {}
d2["kajal"] = "chole bhature"
print (d2)
del d2["kajal"]
print(d2)
print (d2.copy()) #it copies the file and then delete the entry so the original does not break

d3= d2.copy()
del d3["akash"]

print (d2.get("harry"))
d2.update({"leena" : "maggi"}) #have to use {} under () to uodate the value in the dictionary
print(d2)
print(d2.keys()) # will show the keys (word before : in the dictionary)
print(d2.items())

