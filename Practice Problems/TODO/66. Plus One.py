def increaseByOne(digits):
    list = []
    carry = 0
    sum = 0
    lastIndex = 0
    # Iterating from the end:
    for i in range(len(digits)):
        idx = len(digits)-1-i
        # Condition:
        print(idx)
        lastDig = digits[idx]
        if(lastDig == 9):
            prevLastEle = digits[idx -1]
            sum = carry + prevLastEle%10
            carry = prevLastEle / 10
            list.insert(0, sum)
        else:
            lastIndex = i
            break
    # If still digits left in the list:
    if(lastIndex != 0):
        for i in range(lastIndex):
            list.insert(i, digits[i])


def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    #  Condition for the last element
    lastIndex = len(digits) -1
    currentNumber = digits[lastIndex]
    currentNumber += 1
    if(currentNumber < 9):
        digits[lastIndex] = currentNumber
    else:
        # Calling Increase function:
        increaseByOne(digits)
        

    # Return the list of digits:
    return digits

res = plusOne(object,[1,2,9])
print(res)