from random import randint
mass = []
count = int(input("Iteration: "))
for i in range(count):
    mass.append(randint(1,100))
print(mass)

for i in range(len(mass)):
    j = i
    while j>0 and mass[j-1] > mass[j]:
            mass[j], mass[j-1] = mass[j-1], mass[j]
            j-=1

print(mass)



    
