#Jack Thomas
#10/Aug/2020
#Question1
#i=0
#while i<=25:
  #print(i)
  #i+=1

#Question2
#lastnumber=0
#i=10
#while i<=50:
  #print(lastnumber+i)
  #lastnumber+=i
  #i+=1

#Question3
#number=0
#inRange=False
#while(inRange==False):
    #number=int(input("Enter a number:"))
    #if(number>=50 and number<=70):
        #print("number in range")
        #inRange=True
        #break
    #else:
        #print("number not in range")

#Question4
#i=0
#concatenate=""
#while(i<=25):
  #concatenate+=str(i)+","  
  #i+=1

#concatenate=concatenate[:-1]
#print(concatenate)

#Question5
#notString=False
#total=0
#while(notString==False):
    #try:
        #number=int(input("Enter a number, Type a string to stop."))
        #print(number)
        #total+=number
    #except ValueError:
        #notString==True
        #break

#print("Total:",total,sep="")

#Question6
#i=0
#j=0
#while(i<5 and j<5):
    #print("x",end='')
    #i+=1
    #if(i==5):
      #print("")
      #i=0
      #j+=1  