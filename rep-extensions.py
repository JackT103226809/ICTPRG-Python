#Jack Thomas
#17/Aug/2020
#Question1
#i=0
#j=0
#k=5
#while(i<k and j<5):
    #print("x",end='')
    #i+=1
    #if(i==k):
      #print("")
      #i=0
      #k-=1
      #j+=1  

#Question2
#i=0
#ik=0 #width of x's
#il=0 #width of whitespaces
#j=0 #height
#k=1 #ammount of x's
#l=(5-k)/2 #whitespace
#while(i<5 and j<4):
  #while(il<=l):
    #print(" ",end='')
    #il+=1
  #while(ik<k):
    #print("x",end='')
    #ik+=1
    #if(ik==k):
      #il=0
  #i+=1
  #if(i==5):
    #print("")
    #i=0
    #ik=0
    #il=0
    #j+=1
    #k+=2
    #l=(5-k)/2 

#Question3 changing varible names to be a little more descriptive so i dont loose my sanity trying to keep track of alphabet characters
words=["Hello", "World", "in", "a", "frame"]

wi=0
boxWidth=0
while(wi<(len(words))):
  if(len(words[wi])>boxWidth):
    boxWidth=len(words[wi])
    longg=len(words[wi])
  wi+=1
boxWidth+=2

boxHeight=len(words)+1
boxWidthDraw=0
boxHeightDraw=0

i=0

while(boxHeightDraw<=boxHeight):
  while(boxWidthDraw<boxWidth and (boxHeightDraw==0 or boxHeightDraw==boxHeight)):
    print("*",end='')
    boxWidthDraw+=1
  if(boxHeightDraw>0 and boxHeightDraw<boxHeight):
    print("*",end='')
    print(words[boxHeightDraw-1],end='')
    while(i<longg-len(words[boxHeightDraw-1])):
      print(" ",end='')
      i+=1
    print("*",end='')
    i=0
  print("") 
  boxWidthDraw=0 
  boxHeightDraw+=1