# print("====session 4 =====")

# class bird(object):
#     msg2 = "global variable of birdsclass"
#     def fly(self):
#         message = "the bird is flying"   #local variable
#         return message

# sparrow = bird()
# #sparrow.message
# print(sparrow.msg2)

# class aircraft(object):
#     def __init__(self,name,model,capacity,speed,engine):
#         self.name = name
#         self.model = model
#         self.capacity = capacity
#         self.speed = speed
#         self.engine = engine

#     def fly(self):
#         print("the created aircraft can fly")
#     def info(self):
#         print("make{} and model {}".format(self.name,self.model))
#         print("the created aircraft has {} passengers".format(self.capacity))
#         print("engine type {} and speed {}".format(self.engine,self.speed))

# class civilian(aircraft):
#     def __init__(self, name, model, capacity, speed, engine,wings):
#         super().__init__(name, model, capacity, speed, engine)
#         self.wings = wings
#     def passengerseat(self):
#         print("there are more seats in civilian aircraft")
#         print("wingspan is {}".format(self.wings))
#     def runwaylength(self,length):
#         print("the runway length for {} {} is {}".format(self.name,self.model,length))

# airbus=civilian("airbus","A380",800,"1000km/h","rolls-royce","80m")
# airbus.fly()
# airbus.passengerseat()
# airbus.info()
# airbus.runwaylength(7250)
# class fighterjet(aircraft):

#     def runwaylength(self,length):
#         print("the runway length for {} {} is {}".format(self.name,self.model,length))
#     def stealthmode(self):
#         print("the {} {} can operate in stealth mode".format(self.name,self.model))

# f16=fighterjet("f16","x34r",2,"2414km/h","turbo")
# f16.runwaylength(2250)
# f16.info()
# f16.stealthmode()

# class animal(object):
#     def __init__(self,name,legs):
#         self.name = name
#         self.lega = legs
#     def walk(self):
#         print("all animals can walk")

# #class dog(animal):
#     #def __init__(self, name, legs,eyes):
#         #super().__init__(name, legs)
#       #  self.eyes = eyes

# #dog = dog("popy",4,2)
# #dog.walk()

# class radio(object):
#     def __init__(self,make,model,channel):
#         self.make = make
#         self.model = model
#         self.channel = channel

#     def tunechannel(self):
#          print("tunong my radio to bbc")

# class camera(object):
#     def __init__(self,name,lens,pixel):
#         self.name = name
#         self.lens = lens
#         self.pixel = pixel

#     def snapmethod(self):
#         print("parent method for snapping")

# class cellphone(radio,camera):
#     def __init__(self, make, model, channel,name,lens,pixel,year):
#         radio.__init__(self,make, model, channel)
#         camera.__init__(self,name,lens,pixel)
#         self.year = year

#     def info(self):
#         print("a childclass of radio and camera")
#         print("phone make {},model {},channle:{},camera name {}".format(self.make,self.model,self.channel,self.name))
#         print("the lens {},the pixel:{} and the year {}".format(self.lens,self.pixel,self.year))

# phone1 = cellphone("apple","18 pro",76.5,"sony","qled","4k",2026)

# phone1.snapmethod()
# phone1.tunechannel()
# phone1.info()


                                                  ####===session2===####




print("session 4 afternoon friday")

horses = 33
print(horses/12, "&&" , type(horses//12))
print((1+3)**(5-2),(59*100)/60)

a = 1 
b = 2
c = a+b
c = c+ 2
c += 2
print("testing +=",c)
c-= 2 
print("testing -=",c)
c/= 2
print("testing c/=",c)
c*= 2
print("testing *=",c)
c**= 2
print("testing c**",c)

print("is a greater than b:",a>b)
print("is a less than b:",a<b )
print("a not equal to b:",a !=b)
print("is a graeter than or equal to b:",a >=b)
print("is a less than or equal b:",a<=b )
print("is a equal to b in value and type:",a == b)

a =2  
b= 4
if (a>0) or (b>0):
    print(a*b)
else:
    print("some thing is off")
    print(10 and 20)


k = 10
m = 20
numlist = [1,2,3,4,5,20]

if (k in numlist):
    print(k,"is contained in the list")
else:
    print("not contained")
    x = 10
    y = 11
    z = 10
    print("x position in cpu memory",id(x))
    print("z position in cpu memory",id(z))
    print("checking of is",x is y)
    print("chicknig for x&z", x is z)
    print("checking of is not",x is not y)
    print("checking of is not",x is not z)

data1 =[10,20,30,40,50]
data2 = [17,22,43,40,1]
data3 = [10,20,30,40,50]
print(data1 == data3)
print(data2 == data3)

k = 5
m = 2
print(k&m)
print(k|m)
print( k^m)
y = 10
z = 20
mylist = [ 10,3,4,5,2]
if y in mylist and z in mylist:
    print("both y and z are in my list ")

else:
    print( "both not in my list")

if y in mylist or z in mylist:
    print("at least oe of y or z in my list")
else:
    print("none of them are in my list")