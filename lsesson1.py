print("hello world")
print("welcome to python programing")
print("welcome", "to python" , "programing")
print("addition of to nos", 5+6)
print("welcome \n to python \n programing")
print("elcome to \t python programing")
print("this is a cat")
print("this is a \"cat\"")
print('this is a dog')
#name = input("enter your name: ")
#print("hello" , name , "welcome to python programing")
x = 5
y = 2
print("addition of two nos",x+y)
print("subtraction of two nos",x-y)
print("multiplication of two nos",x*y)
print("division of two nos",x/y)
print("power of two nos", x**y)
word= "my name is"
name= "james bond"
identity= word + " " + name
print(identity)
z = 32
q = 3.143
print(z, "is an integer and the data type is: =", type(z))
print(q, "is an folat and the data type is: =", type(q))
print("tseting for true in boolean", 10>9)
print("tseting for false in boolean",3<1)
c = True
d = False
print("start engine",d)
print("the memory location of x in my processor is:",id(x))
print("the memory location of y in my processor is:",id(y))
e = "a"
vowels = ("a" , "e" , "o" , "u" , "i")
print(vowels, "what is data type", type(vowels))
mylist = ["book" , "pen" , True , False , 28 , -34.56]
print("this is my list" , mylist , type(mylist))
myset = (1,1,2,2,3,3)
print(myset , "tha data type is my " , type(myset))
car = {
    "make" : "bmw" , 
    "model" : 320,
    "year" : 2026,
    "trans" : "auto" , 
    "4wd" : True
}
print("my dictionary is" , car , type(car))
print(car.keys())
print(car.values())
#literal method
a_list = [2,3,7,None]
print("third item at index2 is :" , a_list[2])
co_list = list(vowels)
print("the constructor list" , co_list)
legends = ["groucho" , "chico" , "harpo" , "carlin" , "pryo"]
print(legends[0:2])
legends.append("mr ben")
print("our new refreshed list" , legends)
legends.remove("chico")
print("our list after deletion" , legends)
games = ["atari", "nintendo" , "gameboy" , "sega"]
print("the created games list",games)
games.insert(1,"playstation")
print("the new game list" , games)

orderitem = [1,"jeff","computer",75.50,True]
print("list created:", orderitem)
orderitem.remove("jeff")
orderitem.remove(75.50)
print("orderlist after deletion", orderitem)
# sort = sorts item in list in ascending
#pop= removes an item from the list
#reverse= reverses the prder of the items in the list
numbers = [9 , 5 , 3 ,1 ]
print("nmber list created:" , numbers)
numbers.sort()
print(numbers)
eng2esp = {"one":"unoe", "tow":"duo", "three":"tres"}
countries = {}
countries["UK"] = "europe"
countries["china"]="asia"
countries["namibia"] = "africa"
print(eng2esp , "\n" , countries)
apps = dict(twitter="usa" , tiktok="china" , faceapp="russia")
print(apps)
list_items = [["sky","blue"] , ["cloud","rain"] , ["sun","hot"] ]
print("dictionary created from list", dict(list_items))
avengers = {
    "joshbroslin":"thanos", 
    "robertdj":"ironman",
    "chrisevans":"capt america"
    }
print("at the time of creation", avengers)
others = {"loki":"tom hidelston" , "spiderman": "tom hplland"}
print("joshbroslin" in avengers)
print("loki" in avengers)
avengers.update(others)
print("the new updte avengers dictionary:" , avengers)
print(avengers["loki"])
print(avengers.get("spiderman"))
del avengers["joshbroslin"]
print("after deletnih thanos", avengers)
marvel = avengers.copy()
print("a marvel production:", marvel)
power = {"thor":"thor ddinson","hulk":"bruce banner","blackpanther":"tchalla"}
avengers.update(power)
print("the new updte avengers dictionary:" , avengers)
newtuple = tuple(legends)
print("my new ", newtuple)
set2 = {"red", "green","blue"}
set3 = set("LETTERS")
print(myset,set2,set3)
k={1,2,3,4,5}
l={3,4,5,6,7,8}
m= k.union(l)
print("the union of k amd i sets:",m)
print("items in common", k&l)
print("all items sets",k|l)