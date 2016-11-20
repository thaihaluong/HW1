print("-----------2-------------")
x=int(input("Radius? "))
y = x*x*3.14
print("Area = ",y)

print("-----------3-------------")

a = int(input("Enter the temperature in Celsius? "))
b = a*9/5+32
print(a,"(C) = ",b,"(F)")

print("-----------4-------------")

x = int(input("How many B bacterias are there? "))
y = int(input("How much time will we wait? "))
m = (2**(y//2))*x

print("After",y,"minutes, we would have",m,"bacterias")

print("-----------5-------------")
x=int(input("How many months do rabbits have? "))
a = 1
b = 1
for i in range(0,x):
      t=a
      a = b
      b = a + t
      
print("The number of rabbits after",x,"months are:",b)

