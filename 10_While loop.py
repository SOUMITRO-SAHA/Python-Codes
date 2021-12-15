i = 0
while 45 > i:
    # print(i)
    i += 1  # it is mandatory to mention a condition, otherwise the loop will go on unconditionally.
    # i = i + 1
''' Break and Continue Statement'''
i = 0
while (True):
    if i < 5:
        i += 1
        continue
    # print(i, end=" ")
    if i == 20:
        break  # stop the loop
    i += 1
    # print(i)
''' End of Break & Continue Statement'''
'''  QUIZ Time   '''
# i: int = int(input("Enter Your Number - "))
# while (True):
#     if i < 100:
#         i += 1
#         continue
#     print("You Entered ", i)
#     # print(i)
#     if i < 100:
#         break
#     i += 1
#     # else:
#     #     break
#     #     i += 1
#     # print("You Entered lower value than 100")
""" This is my code END """
""" Solution of the Quiz """
# while True:
#     i=int(input("Enter a Number - "))
#     if i>100:
#         print("Congratulation you have entered a number greater than 100. And your Number is - ",i)
#         break
#     else:
#         print("Sorry!, You have entered lesser Number than 100")
#         continue
""" End Solution"""
"""  Other Test Runs  """
while (True):
    i = int(input("Enter your No."))
    if i > 10:
        print("Hello Geek " * i, end="\n")
        break
    else:
        print("Sorry!")
        continue
