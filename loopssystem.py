# list1 = ["akash", "kajal" , "nisha" , "prakash"]
# print (list1)
# for item in list1: #using the for and in the program repeats itself for every item and print everything
#     print(item)

list1 = [["akash",1], ["kajal",2],["nisha",3] ,["prakash",4]] #its a list of list
for item,lollypop in list1:
    # print (item)
    # print(item,"and the lollopop is",lollypop) #this way we can unpack a list given as per reqiured format
 dict1=dict(list1)
# print(dict1) #this will print the values in dict form {}

# # for item,lollypop in dict1: #will throw error but if added .items() it will not
# for item,lollypop in dict1.items():
#     print(item,"and the lollopop is",lollypop)

for items in list1:
    print(item)  #will print on the key #use if,else in this to increase reach