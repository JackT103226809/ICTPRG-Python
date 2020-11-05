#question 1
# Write the function between the START and END tags
# START
#def AddTwoNumbers(x,y):
    #return x + y
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
#print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
#print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))

#question 2
# Write the function between the START and END tags
# START
#def AddInString(x,y,z):
    #return x+y+z
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
#print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
#print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
#print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))

#question 3
# Write the function between the START and END tags
# START
#def FibonacciAdder(y):
    #total = 0
    #for x in range(y):
        #total = total + Fib(x)
    #return total

#def Fib(x):
   #if x <= 1:  
       #return x  
   #else:  
       #return(Fib(x-1) + Fib(x-2))
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
#print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
#print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))

#question4
# Write the function between the START and END tags
# START
#def MultiplyElementsInList(multiply):
    #total=1
    #for x in multiply:
        #total = total*x
    #return total
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
#print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
#print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
#print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))

#question5
# Write the function between the START and END tags
# START
#def IsPalindrome(strinput):
    #if strinput.replace(" ","").lower() == strinput[::-1].replace(" ","").lower():
        #return True
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
#print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
#print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
#print("Test 4 Passed: " + str(IsPalindrome("frank") == False))

#question6
# Write the function between the START and END tags
# START
#def SortWordsAlphabetically(strinput):
    #SortArray = strinput.lower().split("-")
    #SortArray = sorted(SortArray)
    #output = ""
    #for x in SortArray:
        #output = output + x + "-"
    #return output[:-1]
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
#print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
#print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))

#question7
def PrintBoxByWidth(w):
    for x in range(w):
        print("x", end='')
    print("")
    print("x", end='')
    for x in range(w-2):
        print(" ", end='')
    print("x", end='')
    print("")
    print("x", end='')
    for x in range(w-2):
        print("o", end='')
    print("x", end='')
    print("")
    print("x", end='')
    for x in range(w-2):
        print(" ", end='')
    print("x", end='')
    print("")
    for x in range(w):
        print("x", end='')

PrintBoxByWidth(60)