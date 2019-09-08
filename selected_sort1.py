from random import randint

mass = []
count = int(input(" Iteration: "))
for j in range(count):
    mass.append(randint(1,100))
print(mass)


for i in range(len(mass)-1):
    for j in range(len(mass)-1):
        if mass[j] == min(mass):
            j+=1
        elif mass[j] > mass[j+1]:
            mass[j], mass[j+1] = mass[j+1], mass[j]
            j+=1
            
        

print(" Sorted Mass: ", mass)
