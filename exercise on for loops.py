#make a list and print only the integers and numbers >6

list1 = [int, float, "akash" ,"nisha" ,12,3,5,5,6,25,]
for item in list1:
    if str(item).isnumeric() and item >= 6:  #typecasting the list in the str system by adding str(items) since we also have str in list
      print(item)