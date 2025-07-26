'''
def fun(n):
    if((n>9 and n<100) or (n<-100) and (n>-9)):
        print("Two digit number")
    else:
        print("Not an Two digit number")
n = int(input())
d=fun(n)
-----------------------------------------------
def fun(n):
    if n < 0 or n > 12:
        return "Invalid Month Number"
    elif(n == 2):
        return "28days or 29days in leap year"
    elif(n in [4,5,9,11]):
        return "30 days"
    else:
        return "31 days"
n = int(input())
print(fun(n))
------------------------------------------------

def fun(n):
    n = str(n)
    count = 0;
    for i in n:
        count += 1
    return count

n = int(input())
print(fun(n))
------------------------------------------------
import os
import time
def alarm(n):
    i = 0
    while (i<n):
        time.sleep(1)
        i +=1
        time_left = n - i
        print(f'time Left: {time_left:02d}')
    os.system("start music.mp3")

h = int(input("hours: "))
m = int(input("minites: "))
s = int(input("seconds: "))
total_sec = h*3600 + m*60+s
alarm(total_sec)
#-------------------------------------------------------

class Vcal():
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def infoMe(self):
        print(f"Name: {self.name} \nMax Speed: {self.max_speed} Mileage: {self.mileage}")



hero = Vcal("Hero Hounda",60,100)
hero.infoMe()
#---------------------------------------------------------
class Circle():
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius**2
    def circumference(self):
        return 2*3.14*self.radius
    
s1 = Circle(5)
print(s1.area())
print(s1.circumference())
#---------------------------------------------------------
class Temperatur():
    def __init__(self,celcius):
        self.celcius = celcius

    def fahrenheit(self):
        return (self.celcius*9/5)+32
    def kelvin(self):
        return self.celcius+273.15
    
    def convert_to_celcius(self,fahrenheit):
        return (fahrenheit-32)*5/9
    
    def convert_to_fahrenheit(self,celcius):
        return (celcius*9/5)+32
    
t1 = Temperatur(10)
print(t1.fahrenheit())

#-----------------------------------------------------------

def amicablenum():
    n = int(input("Enter the number: "))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == n:
                print(i, j)
                break
def is_Amicable():
    n = int(input("Enter the number: "))
    sum1 = 0
    sum2 = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum1 += i
            for j in range(1, sum1 // 2 + 1):
                if sum1 % j == 0:
                    sum2 += j
                    if sum1 == sum2 and sum1 != n:
                        print("Amicable numbers are", n, sum1)
                        break

is_Amicable()
amicablenum()

# magic number: by adding digits of a number reqrvesly if we get 1 then it is called as magic number
# method - 1
a = int(input("enter the number: "))
if(a%9 == 1):
    print("magic number")
else:
     print("not magic number")

# method - 2
a = int(input("Enter the number: "))
m = a
while m>=10:
    sum = 0
    while m >0:
        r = m % 10
        sum += r
        m = m // 10

    m = sum

if m == 1:
    print("magic number")
else:
    print("not an magic number")


# method - 3
def magic(n):
    sum = 0
    while n > 0:
        r = n % 10
        sum += r
        n = n // 10
    return sum

a = int(input('Enter the number: '))
n = a
while  not(n>=1 and n<=9):
    n = magic(n)

if n == 1:
    print("magic")
else:
    print("not magic")

# Heckerrank problem
b,n = map(int,input("Enter the b and n values: ").split())
k = list(map(int,input(f"Enter the prices:{n}").split()))
d = list(map(int,input(f'Enter prices: {n}').split()))

p = 0
for i in k:
    for j in d:
        if i+j > p and i+j <= b:
            p = i+j
            e,f = i,j
    if p == 0:
        print(-1)
    else:
        print(e,f)

# problem -1 
sum = 0
while True:
    n = int(input())
    if n == -1:
        break
    sum += n

print(sum)
#--------------------------------------
# problem - 2
n = int(input())
sum = 0
for i in range(1,n+1):
    a = int("2"*i)
    sum += a

print(sum)

#pro - 2 method-2
n = int(input())
a = 0
sum = 0
for i in range(n):
    a = (a * 10) + 2
    sum = sum +a

print(sum)
#-----------------------------------------

n = int(input())
bird = {}
for i in range(n):
    a = input()
    if a in bird:
        bird[a] += 1
    else:
        bird[a] = 1


higthFeq = 0
for key in bird.values():
    if key > higthFeq:
        higthFeq = key

finalfeq = []
for key in bird.keys():
    if bird[key] == higthFeq:
        finalfeq.append(key)

print(finalfeq[0])
#----------------------------------------------


r,c = 3,3
a = []
for i in range(3):
    t = []
    for j in range(3):
        ele = int(input(f'Enter the a{[i]}{[j]}: ele')) #b = [int(i) for i input(f'{r} ele').split()]
        t.append(ele)
    a.append(t)

print(a)
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')
    print()


# weels
v = int(input())
w = int(input())

if w<2 and v>w and w%2 != 0:
    print("Invalid input")
else:
    x = (4*v-w)/2
    y = v-x
    if x>0 and y>0:
        print(int(x),int(y))
    else:
        print("Enter valid numbers")

from tkinter import* 
expression=""                                           
def butten_press(item):
    global expression
    expression=expression+str(item)
    text.set(expression)  
def equal():
    global expression
    result=str(eval(expression))
    text.set(result)
    expression=""
def clear():
    global expression
    expression=""
    text.set("")
window=Tk()                                                    
window.title("CALCULATOR")        

text=StringVar(window)
expression=''
text.set(expression)                              
l=Label(window,textvariable=text,font=("serif",30), bg="black",fg="white",height=1,width=10)            
l.pack()                                                                                                  
                                                         
f=Frame(window)                                                                                    
f.pack()
                                                 
b1 = Button(f,text='7',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("7"))     
b1.grid(column=0,row=0)                                                                                                      
b2 = Button(f,text='8',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("8"))             
b2.grid(column=1,row=0)
b3 = Button(f,text='9',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("9"))
b3.grid(column=2,row=0)
bdel = Button(f,text='<--',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=clear)
bdel.grid(column=3,row=0)
b4= Button(f,text='4',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("4"))
b4.grid(column=0,row=1)
b5 = Button(f,text='5',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("4"))
b5.grid(column=1,row=1)
b6 = Button(f,text='6',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("6"))
b6.grid(column=2,row=1)
bplus = Button(f,text='+',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("+"))
bplus.grid(column=3,row=1)
b7= Button(f,text='1',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("1"))
b7.grid(column=0,row=2 )
b8= Button(f,text='2',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("2"))
b8.grid(column=1,row=2)
b9 = Button(f,text='3',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("3"))
b9.grid(column=2,row=2)
bmin = Button(f,text='-',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("-"))
bmin.grid(column=3,row=2)
bdiv= Button(f,text='/',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("/"))
bdiv.grid(column=0,row=3 )
b0= Button(f,text='0',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press("0"))
b0.grid(column=1,row=3)
beq= Button(f,text='=',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=equal)
beq.grid(column=2,row=3)
bmul = Button(f,text='',width="7",height='3',bg='black',fg='white',activebackground="white",activeforeground="black",command=lambda:butten_press(""))
bmul.grid(column=3,row=3)




window=mainloop()


'''
# prublem - 1 (disarium number)
def is_Disarium_Number():
    n = input()
    ans = 0
    for i in range(len(n)):
        a = int(n[i])**(i+1)
        ans = ans + a
        
    if n == str(ans):
        print("Disarium number")
    else:
        print("not disarium number")

    c = 1
    for i in n:
        a = int(i)**c
        ans = ans + a
        c = c + 1
    print(ans)

# problem - 2 (Strong number)
from math import *
def is_Strong_Number():
    n = input()
    ans = 0
    for i in n:
        ans = ans + factorial(int(i))
    if n == str(ans):
        print("Strong number")
    else:
        print("not strong number")

def is_Spy_Number():
    n = input()
    s = 0
    m = 1
    for i in n:
        s = s + int(i)
        m = m * int(i)
    if s == m:
        print("Spy number")
    else:
        print("not spy number")


def x_string():
    a = input()
    b = input()
    a = list(a)
    b = list(b)
    c = []
    for i in b:
        if i in a:
            count = a.count(i)
            for j in range(count):
                a.remove(i)

    print(''.join(a))

from itertools import *
def number_Problem():
    n = input()
    x = input()
    n = list(n)
    a = list(permutations(n))
    ans = []
    for i in a:
        m = ''.join(i)
        ans.append(int(m))
    
    for j in ans:
        if j > int(x):
            print(j)
            break
    else:
        print("no number greater than",x,"is possible")
            
def candle():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    print(a)

    h = a[0]
    for j in a:
        if j > h:
            h = j

    count= 0
    for x in a:
        if x == h:
            count += 1
    
    print(count)

x_string()