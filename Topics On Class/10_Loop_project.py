# Hide the no. n = 18
# then give hint to the person so guess the no.
"""Hint is like if the guessed no. is greater than hidden no. then give a hint "You have guessed
a higher no. reduced the no. something.
and same for lesser one give a hint to increase the no. by something's."""
# The no. of hint will be 9. After completely use all the guesses prompt a masses "Game Over"
# If someone complete the game before 9 guess has completed Show you win " And show how many guess they take"
n1 = 12
while True:
    n2 = int(input("Guess the Number:-- "))
    odd = (n1 - n2) % 2 == 1
    even = (n1 - n2) % 2 == 0
    if n1 == n2:
        print("Congratulations! You Guess the Write Number.")
        print("And the number of guess you take is:", {})
        break
    else:
        print("Try again. You guess the wrong number")
        if n1 != n2:
            print("Guess-1")
            if n1 > n2 :
                print("You guessed lower number ", )
                if odd:
                    print("The original number is an Odd Number.")
                elif even:
                    print("The original is an Even Number.")
            else:
                print("You guessed higher number ")
                if odd:
                    print("The original number is an Odd Number.")
                elif even:
                    print("The original is an Even Number.")

        continue
