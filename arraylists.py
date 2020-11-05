#Jack Thomas
#24/Aug/2020
#Question1
#values = [66, 43, 1, 6, 2, 99, 4]
#for x in values:
  #if x<10:
      #print(x)

#Question2
#date=input("Whats the current date? [dd/mm/yyyy]")
#date=date.split("/")
#print("Day:"+date[0])
#print("Month:"+date[1])
#print("Year:"+date[2])

#Question3
#summ=0
#maxx=0

#values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#for x in values:
    #summ+=x
    #if x>maxx:
        #maxx=x

#print("sum:",summ)
#print("average:",summ/len(values))
#print("maximum:",maxx)

#Question4
#name=input("what is your name?")
#nameAsArray=name.split()
#initials=""

#for x in nameAsArray:
    #initials+=x[0]

#print("full name:",name)
#print("initials:",initials)

#Question5
#notString=False
#numberArray=[]
#while(notString==False):
    #try:
        #number=int(input("Enter a number: "))
        #numberArray.append(number)
    #except ValueError:
        #notString=True
        #break

#print("you entered:",numberArray)

#Question6
#number=input("enter a large number: ")
#summ=0
#bodge=""

#print("sum of digits: ",end="")
#for x in number:
  #summ+=int(x)
  #bodge+=x+"+"
#print(bodge[:-1],"=",summ,sep="")

#Question7
notString=False
numberArray=[]
while(notString==False):
    try:
        number=int(input("Enter a number: "))
        numberArray.append(number)
    except ValueError:
        notString=True
        break

i=0
dupelicates=[]
count=0
while i<len(numberArray):
    for x in numberArray:
        if numberArray[i]==x:
            count+=1
        if count>=2:
            if numberArray[i] not in dupelicates:
                dupelicates.append(numberArray[i])
    count=0
    i+=1
print("Repeating numbers: ",dupelicates)