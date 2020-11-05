#Jack Thomas
#12/october/2020
#question 1
#num1 = int(input("enter number one:"))
#num2 = int(input("enter number two:"))
#out = num1 + num2

#f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/maths.txt", "w")
#f.write(str(out))

#print("Answer printed to maths.txt")
#f.close()

#question 2
#namesArray = []

#while True:
    #name = input("Enter a name:")
    #namesArray.append(name)
    #if name == "":
        #break

#f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/people.txt", "w")
#for x in range(len(namesArray)):
    #f.write(namesArray[x]+"\n")

#print("Names printed to people.txt")
#f.close()

#question 3
#namesArray=[]

#f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/names.txt", "r")
#for x in f:
    #namesArray.append(x)
#f.close()

#f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/names-formated.txt", "w")
#for x in range(len(namesArray)):
    #namesArray[x]=namesArray[x].title()
    #f.write(namesArray[x])
#f.close()

#print("Names formatted to names-formated.txt")

#question 4
#import math

#f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/factorial.txt", "w")
#for x in range(1,11):
    #f.write(str(math.factorial(x))+"\n")

#print("factorial of numbers 1 to 10 printed to factorial.txt")
#f.close()

#question 5
username = input("username:")
password = input("password:")
access = False

f = open("/home/zdog/Tafe/2020-VE03-ICTPRG407/Quiz: Reading and Writing Files/logins.txt", "r")
fSplit = f.read().split(",")
f.close()

fSplit[len(fSplit)-1] = fSplit[len(fSplit)-1][:-1] #this code removes the end of line character from my array, was gonna remove it from the .txt with vim but i dont know how to use vim lol

for x in range(len(fSplit)):
    iSplit = fSplit[x].split(":")
    if iSplit[0] == username:
        if iSplit[1] == password:
            access = True
            break

if access == True:
    print("Access Granted")
else:
    print("Access Denied")