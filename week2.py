#Jack Thomas
#3/August/2020

#Question 1
name=input("what is your name?")
if(name=="frank" or name=="george"):
    print("Hello ",name,sep="")
else:
    print("Go away ",name,sep="")

#Question 2
birthyear=int(input("What year were you born?"))
if(2020-birthyear>=18):
    print("You're ",2020-birthyear," old!",sep="")
    print("Come in and have a drink!")
elif(2020-birthyear<18):
    print("You're ",2020-birthyear," old!",sep="")
    print("Sorry no beer for you!")

#Question 3
credentials=["admin","password123"]
username=input("whats your username?")
password=input("whats your password?")
if(username==credentials[0] and password==credentials[1]):
    print("access granted!")
else:
    print("access denied")

#Question 4
database=[["bob","password1234"],["fred","happyPass122"],["lock","passwithlock44"]]
username=input("whats your username?")
password=input("whats your password?")
i=0
while(i<len(database)):
    if(database[i][0]==username):
        print("username found")
        if(username==database[i][0] and password==database[i][1]):
            print("access granted!")
        else:
            print("incorrect password")
        break
    i+=1
    if(i==len(database)):
        print("username not found")
        break

#Question 5
grade=int(input("What grade did you get?"))
if(grade<=100 and grade>=90):
    print("You will receive a High Distinction")
elif(grade<=89 and grade>=80):
    print("You will receive a Distinction")
elif(grade<=79 and grade>=70):
    print("You will receive a Credit")
elif(grade<=69 and grade>=50):
    print("You will receive a Pass")
elif(grade<=49 and grade>-1):
    print("You've failed")
else:
    print("you sure thats correct?")