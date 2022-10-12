#(a+b)2 = a2 + b2 +2ab
from unittest.result import failfast


a = 10 
b = 20
sol = (a+b)*(a+b)
print(sol)

### 
a=10
b=20
sol=pow(a,2)+pow(b,2) + 2*a*b
print(sol)



#condition
a = 5
b = 3
if (b>a):
    print("a is greater than b")
elif (b<b):
    print("b is greater tahn a")    
else:
    print(" \nboth are equal\n") 


    # grade /marks
a = 80
if  a<=20:
    print("you are failed  ")
elif a>=20 and a<=60:
    print("your grade is  C")    
elif a>=60 and a<=70:
    print("your grade is b")    
elif a>=70 and a<=80:
    print("your grade is b+")
elif a>=80 and a<=90:
    print("your grade is a")
elif a>=90 and a<=100:
    print("your grade is A+")
else: 
  print("failed")           

###  using input
  
marks = int(input("enter your marks\n"))

if marks >=90:
    grade ="ex"
elif marks >=80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "c"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"  
    print('your grade is '+ grade)                  
    