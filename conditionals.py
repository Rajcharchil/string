a = 8
## if-elif-else ladder in python 
if(a<3):
    print("the valu of a is greater than 3")
elif(a>13):    
    print("the valu of a is greater than 13")
elif(a>7):    
    print("the valu of a is greater than 7")
elif(a>17):    
    print("the valu of a is greater than 17")
else:    
    print("the valu of a is greater than 3 or 7")

# 2. if(condition 1):    = if condition is 1 is true  
    # print("yes")

    #elif(condition 2):    = if condition 2 is true

    #else:                 = otherwise
       # print ("may be")


## find greatest of four number
num1 = int(input("enter number1:"))       
num2 = int(input("enter number2:"))       
num3 = int(input("enter number3:"))       
num4 = int(input("enter number4:"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1)+ " is greatest")
else:
   print(str(f2)+ " is greastest")


## mark sheet 
sub1  = int(input ("enter first subject marks\n"))
sub2  = int(input ("enter first subject marks\n"))
sub3  = int(input ("enter first subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subject ")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail due to total percentge 40")
else:
    print("congatulation you paased the exam ")  


    ## spam detector program
text = input ("enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this "in text):
    spam = True
elif("suscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("this text is spam")
else:
    print("this text is not spam")                        
    