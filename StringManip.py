#Jack Thomas
#7/Sep/2020
#Question 1
#name = input("Enter your full name:")
#print(name.replace(" ","\n"))

#Question 2
#numberIn = int(input("Enter a number:"))
#stringIn = input("Enter your email:")

#i=0
#while i < numberIn:
    #print(i+1,"_",stringIn,sep="")
    #i+=1

#Question 3
#import math

#stringIn = input("Enter string:")
#if len(stringIn) >= 7 and len(stringIn) % 2 == 1:
    #mid=math.ceil(((len(stringIn))-1)/2)
    #print(stringIn[mid-1],stringIn[mid],stringIn[mid+1],sep="")

    #print(stringIn[math.ceil((((len(stringIn))-1)/2)-1)],stringIn[math.ceil(((len(stringIn))-1)/2)],stringIn[math.ceil((((len(stringIn))-1)/2)+1)],sep="")

#Question 4
stringIn = input("Enter string:")
aCount = 0
eCount = 0

i=0
while i != len(stringIn):
    if stringIn[i].lower() == "a":
        aCount+=1
    elif stringIn[i].lower() == "e":
        eCount+=1
    i+=1

print("a:",aCount,sep="")
print("e:",eCount,sep="")