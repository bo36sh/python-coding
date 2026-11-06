import os
print("the current folder of my python code :", os.getcwd())
print("the posix interface for intercom:", os.name)
print("print list of files in the folder:", os.listdir())
print("print list of files in the folder:", os.listdir('/'))
print("the current process id:", os.getpid())
#print("creatning a new folder: " , os.mkdir("C:/Users/aws.admin/Documents/python3003/lesson8"))
print("====maths polt section===")


import matplotlib.pyplot as plt

department = ["HR","IT","SALES","FINANCE"]
employees = [10,25,15,12]

plt.bar(department,employees,color="red")
plt.xlabel("department")
plt.ylabel("number of employees")
plt.title("employee distributin by department")
plt.show()

ages = [22, 25, 30, 30, 31, 34, 35, 36, 40, 41, 42, 45, 46, 50, 51, 52]

# Create histogram
plt.hist(ages, bins=5, color='lightgreen', edgecolor='black')

# Add labels and title
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.title('Age Distribution of Employees')

# Show chart
plt.show()


# Sample data
departments = ['HR', 'IT', 'Sales', 'Finance']
sizes = [10, 25, 15, 12]
colors = ['gold', 'skyblue', 'lightgreen', 'lightcoral']

# Create pie chart
plt.pie(sizes, labels=departments, colors=colors, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures pie is drawn as a circle
plt.axis('equal')
plt.title('Employee Percentage by Department')

# Show chart
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.subplot(2, 2, 1)
plt.bar(x, y)
plt.title("Bar Chart")
plt.subplot(2, 2, 2)
plt.hist(y)
plt.title("Histogram")


#PART 2
plt.subplot(2, 2, 3)
plt.pie(y, labels=x)
plt.title("Pie Chart")

plt.subplot(2, 2, 4)
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.tight_layout()
plt.show()


import turtle
screensize = turtle.getscreen()
Oogway = turtle.Turtle()

Oogway.right(90)
Oogway.forward(130)
Oogway.left(60)
Oogway.back(100)
Oogway.color("light green")

#Oogway.goto(100,100)
Oogway.fd(100)
Oogway.rt(90)
Oogway.fd(100)
Oogway.rt(90)
Oogway.fd(100)
Oogway.rt(90)
Oogway.fd(100)


Oogway.circle(60)
Oogway.dot(60)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        Oogway.color(c)
        Oogway.forward(steps)
        Oogway.right(30)

for i in range(50):
    Oogway.forward(50)
    Oogway.right(144)


colors = ['red', 'purple', 'blue', 'green', 'darkolivegreen', 'darksalmon']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)



turtle.mainloop()