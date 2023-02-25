lis1 = ["Sam", "Rohan", "Gurmit", "Dip"]
# for itme in lis1:
#     print(itme)  ### """ This is how We call all the items in lis1 by just one line of code. Known as For loop """

### We also use it for list under list. Let's see
# lis2 = [["Sam", 4], ["Rohan", 7], ["Gurmit", 5], ["Dip", 2]]
# for item1,candy in lis2:
#     print(item1,"eats candy", candy)
#
### We can use for loop also for tuple as well as dictionary.
# tpl = ("Tomy", "Snupy", "Sheru")
# for item3 in tpl:
#     print(item3)

### But for Dictionary we could not call it directly.

dic1 = {"Somi":"it is the first part of my name.",
        "Candy":"it is a chocolate"}
# for item4 in dic1:
#     print(item4) # it only prints the key not the whole things. Hence the 2nd method down below.

# for item4 in dic1.items():  # now it's working without .items() it wouldn't work.
#     print(item4)

""" QUIZ : make a list put some alpha-numeric values in it and then only print numbers which less then 6"""
list1 = ["kite", 55, 6, 4, 3, 7, 9, "Popy", 1, 2, 5, 88]
# for itm in list1:
#     if str(itm).isnumeric() and itm < 6:
#         print(itm)

for itm in list1:
    if str(itm).isnumeric() and itm <= 6:
        print(itm)
""" End of QUIZ """