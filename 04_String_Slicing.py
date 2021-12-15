mystr = "My name is Soumitra Saha, and I am learning Python for last 1 week."

print(mystr)
print(len(mystr))

""" ========== String Slicing =============== """
print(mystr[0:9])  # Counting Starts from 0 and end at 8 in this case.
print(mystr[0:50:2])  # Here [::2] 2 represent the skipping
print(mystr[::])  # Here automatically taking the values like[0:67:1] 0 = 1st one, 67 = last one and 1 = no skipping.

print(mystr[-8:-1])  # In this particular case the counting will start from back to the start.i.e.- the last no. is -1
print(mystr[::-1])  # It totally flip the line.
print(mystr[::-2])  # First it flip the line and then skip every 2 alphabet

""" ================== String Functions ====================== """
print(mystr.isalnum())  # it refers alpha numeric strings,i.e.- There is no space b/w words.
print(mystr.isalpha())  # Search online.
print(mystr.endswith("Week"))  # Result will be true.
print(mystr.count("i"))  # it will count the given argument. In here the argument is "i"
print(mystr.capitalize())  # it only capitalize the first alphabet.
print(mystr.find("am"))  # it will find the given argument.
print(mystr.replace("am", "is"))  # it will replace the former argument with the given argument.
"""In here I observe a great thing that not only the "am", which is a word it self changes into "is" but also the "am"
which is inside of "Name" also change into "is" """
print(mystr.lower())
print(mystr.upper())
'''print(mystr.) ---> this is left black is not because there are no other string method left.
 It is black because you have to search online the other ones.'''