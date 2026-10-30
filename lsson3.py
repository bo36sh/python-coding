# print("this is week 3")
# class car:
#     #attributes
#     make = "mercedes"
#     model = "c-class"
#     year = 2019
#     manual = False
#     colour = "blue"

# mycar = car()   #instNCE OF CLASS CAR
# print(mycar.make,mycar.model,mycar.year,mycar.manual,mycar.colour)
# print("is the car manual:",mycar.manual)

# class vehicle(object):
#     def __init__(self,make,model,year,manual,colour,speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.manual = manual
#         self.colour = colour
#         self.speed = speed
 
#     def accelerate(self):
#             print("the car is accelerating at",self.speed,"mph")
#             self.speed = self.speed + 30
#             print("the car is moving at",self.speed,"mph")
#     def stop(self):
#          print("applying breaks")
#          self.speed = self.speed - 15
#          print("the car is moving at",self.speed,"mph")
#     def turnright(self):
#          print("the car is turning right")
#     def getspeed(self):
#          print("the current speed:",self.speed,"mph")
#     def getcolour(self):
#          print("the colour of the car:",self.colour)
#     def settrans(self,trs):
#          self.manual=trs
#          print("transmission of the car",self.manual)
#     def setyear(self,yr):
#          self.year=yr
#          print("year:",self.year)
#     def carsound(self):
#          print("sound of car {} at full speed".format("vroom vroom"))
#     def carmodel(slef,model="a6"):
         
#          print("{}is then ew model".format(model))


# firstcar = vehicle("audi","a3",2020,True,"red",0)
# secondcar = vehicle("bmw",320,2021,True,"black",0)
# print("make:",firstcar.make,"model:",firstcar.model,"year:",firstcar.year,"manual:",firstcar.manual,"colour:",firstcar.colour)

# firstcar.accelerate()
# firstcar.stop()
# firstcar.turnright()
# firstcar.getspeed()
# firstcar.getcolour()
# firstcar.settrans("automatic") 
# firstcar.setyear(2026)
# firstcar.carmodel
# firstcar.carsound()
# print("my name is {},iam{}years old".format("john",21))

##=========afernoon======##

print("session3afternoon")

class employee(object):
    companyname = "github"

    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def show(self):
        print("my name is :", self.name,"with id:",self.id,"and salary",self.salary)

    @staticmethod
    def department(dpt):
        print("the empoloyees department is",dpt)

    @classmethod
    def placeofwork(cls,name):
        print("this is the name of company is", employee.companyname)
        employee.companyname = name
        print("my new place of work is", employee.companyname)
    def setdetails(self,id,salary):
        print("current salary",self.salary,"current id",self.id)
        self.id = id
        self.salary = salary
        print("new:","current salary",self.salary,"currentid",self.id)
    def printemail(self):
        print("employee email:", self.name+"@microsoft.com")

# class tv:
#     def __init__(self,brand,size,model):
#         self.brand = brand
#         self.size = size
#         self.model = model
#     @staticmethod
#     def print_model():
#         print("tv model: samsung qled")

        
        
        

emp1 = employee("jhondoe","ab555",1500)
emp1.show()
print("accessing salary from outside",emp1.salary)
emp1.department("accouting")
emp1.placeofwork("microsoft")
emp1.setdetails("zz222",2000)
emp1.printemail()
#tv.print_model()

class circle(object):
    def __init__(self,area,size):
        self.area = area 
        self.size = size

    def __add__(self, other):
        return self.area + other.area, self.size + other.size
    def __sub__(self, other):
        return self.area - other.area
    def __truediv__(self, other):
        return self.area / other.area
    def __lt__(self, other):
        return self.area < other.area    

c1 = circle(4,"small")
c2 = circle(10,"large")

print("area c1:",c1.area , "area c2:",c2.area)
print("addition of two circle areas",c1 + c2)
print("subtraction of two circle areas",c1 - c2)
print("division of two circle areas",c1 / c2)
print(" two circle comparison", c1 < c2)


class shark(object):
    def swim(self):
        print("the shark is swimming")
    def swimbackwards(self):
        print("cant swim backwards but can sink backward")
    def skeleton(self):
        print("the sharks skeleton is made of cartilage")

class eelfish(object):
    def swim(self):
        print("the eelfish is swimming")
    def swimbackwards(self):
        print("the eelfish can swim backwards")
    def skeleton(self):
        print("the eelfish skeleton is made up of bones")

s1 = shark()
e1 = eelfish()
for fish in (s1,e1):
    fish.swim()
    fish.swimbackwards()
    fish.skeleton()

class nigeria(object):
    def capital(self):
        print("abuja is the ccapital of nigeria")
    def language(self):
        print("english is the primary language of nigeria")
    def continent(self):
        print("nigeria is in africa")

class france(object):
    def capital(self):
        print("paris is the ccapital of nigeria")
    def language(self):
        print("french is the primary language of nigeria")
    def continent(self):
        print("france is in europe")

coun1 = nigeria()
coun2 = france()


for country in (coun1,coun2):
    country.capital()
    country.language()
    country.continent()
    
    
    
class pigeon(object):
    def fly(self):
        print(" pigeon can fly")
    def eat(self):
        print("pigeon can eat")
    def run(self):
        print("pigeon cant run")

class sparrow(object):
    def fly(self):
        print("sparrow can fly")
    def eat(self):
        print("sparrow can eat")
    def run(self):
        print("sparrow can run")

bird1 = pigeon()
bird2 = sparrow()


for bird in (bird1,bird2):
   bird.fly()
   bird.eat()
   bird.run()
