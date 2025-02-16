for i in range(100):
    print(i)

for i in range(1,50,2):
    print(i)

#break statement in for loops
for i in range(1,100):
    if i == 50:
        print("line break at",i)
        break
    print(i)        

#continue statement in for loops
for i in range(1,30):
    if i == 15:
        continue
    print(i)

#else statement in for loops
for i in range(1,10):
    print(i)
else:
    print("Dogesh is right")
    