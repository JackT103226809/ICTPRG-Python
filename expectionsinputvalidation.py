#question1
#while True:
  #try:
    #InputNumber = int(input("Enter a number: "))
    #print(str(InputNumber))
    #break
  #except ValueError:
    #print("That is not a number, try again!")

#question2
#import ipaddress

#def IPValidation():
  #while True:
    #try:
      #InputIP = ipaddress.IPv4Network(input("Enter a IPv4 address: "),True)
      #print(InputIP)
      #break
    #except ValueError:
      #print("That is not a valid IPv4 adress, try again!")
    
#IPValidation()

#question3
#def EnoughWords(Minn,Maxx):
  #while True:
    #InputString = input("Enter a sentence: ").lower()
    #InputString = InputString.split()
    #if len(InputString) not in range(Minn,Maxx):
      #print("The string needs more words than",str(Minn),"words and less words than",str(Maxx),"words!")
    #else:
      #for x in InputString:
        #print(x)
      #break

#EnoughWords(2,7)

#question4
#import re

#while True:
  #InputEmail = input("Enter a email: ").lower()
  #if not re.match(r"^(?=.*\.)[a-z]{2,32}@[a-z.]{2,32}$", InputEmail):
    #print("Not a valid email adress, try again!")
  #else:
    #print(InputEmail)
    #break

#question5
import re

while True:
  InputPass = input("Enter a password: ")
  if not re.match(r"^(?=.*\d)(?!.*password).*(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+])(?=.*[a-zA-Z]).{7,}$", InputPass):
    print("Not a valid password, try again!")
  else:
    print(InputPass)
    print("Valid password")
    break

#this is why this test took me 5 hours, I was learning regex and jeez its a lot!