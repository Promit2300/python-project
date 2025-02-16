class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"   
x = MyClass("Aadam",40)
print(x) 

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = myclass("tom",22)
print(p1.age)        
print(p1.name)

class nclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello this is",self.name)    
p2 = nclass("Jacob",29)
p2.myfunc()        

class rgb:
    def __init__(myobject,name,age):
        myobject.name = name
        myobject.age = age
    def jfunc(myobject):
        print("dank this works too",myobject.age)
l2 = rgb("Locas",50)
l2.age = 100
l2.jfunc()            

class Aclass:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def lfunc(self):
        print("this is how it works",self.firstname)
m2 = Aclass("max",67)
m2.lfunc()            

class bclass:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def vog(self):
        print(self.firstname,self.lastname)
class kclass(bclass):
    def __init__(self,fname,lname):
        bclass.__init__(self,fname,lname)

k2 = bclass("Mike","Tyson") 
k2.vog()     

class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def move(self):
        print("hello there it s been a long time",self.name)

class mclass(myclass):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.graduationyear = 1000

w2 = mclass("kandrick",200)
print(w2.graduationyear)


        