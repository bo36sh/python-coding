x = 10
if(x>0):
    print("x is a positive integer")
else:
    print("x is 0 or less than 0 , a negative n0")
    
passing_Score= 40
my_Score= 67

if(my_Score >= passing_Score):
    print("ihave passed the module with grade" , my_Score)

if "python" in ["java","c","kotlin","python"]:
    print("python in the list")

#print("even",2%2,"odd with remainder",3%2)
#def checkEvenOdd(x):
   # if(x)




y=22

if(y>30):
    print("stay home")
else:
    print("iam out and about")

a=14
b=14
if(a>b):
    print("a is the bigger number")
elif(a<b):
    print("b is bigger than a")
else:
    print("a and b are equal")
temp=10
if( temp <10):
    print("it is cold")
elif( temp> 10 and temp <20):
    print("a bit cold")

elif(temp > 20 and temp <30):
    print("its warm")
elif(temp > 31 and temp < 40):
    print("it is hot")
else:
    print("do not come out")

u=15
if 0<x:
    if x<16:
        print("numbers between o and 16")

num= float(input("enter a number"))

if num>=0:
    if num ==0:
        print("zero")
    else:
        print("positive number")
else:
    print("negative")

def cube(x):
    r=x**3
    return r
print(cube(5))
x=10
def printResult(X):
    if x<=0:
        print("positive numbers only,please")
        return
    result = x+2
    print("this is the result",result)
    printResult(13)

def countdwon(n):
    if n ==0:
        print("happy new year!!!")
    else:
        print(n)
        countdwon(n-1)

countdwon(10)

#mylist=["pen","book","class",,"school"]
#print(mylist[0],mylist[1],mylist[2],mylist[3],)
#for itmes

genre=["pop","rock","jazz"]
for music in range(len(genre)):
    print("i like",genre[music])

number=[6,5,3,8]
sum=0
for val in number:
    sum= sum+val
    print("the sum total is",sum)
for number in range(20):
    if(number%2==0):
        print(number,"is even")

count=0 
while count<=5:
    print(count)
    count = count + 1

for val in "strimg":
    if val == "i":
        break
    print(val)