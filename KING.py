V = open("D:\Promit urgent/Twallet.txt")
print(V.read(10))

f = open("Basic Data Structures.txt","r")
print(f.readline())
print(f.readline())

j = open("Basic Data Structures.txt","r")
for x in j:
    print(x)
j.close()    

k = open("Basic Data Structures.txt","a")
k.write("i am the bad guy if yiu know ")
k.close()

k = open("Basic Data Structures.txt")
print(k.read())