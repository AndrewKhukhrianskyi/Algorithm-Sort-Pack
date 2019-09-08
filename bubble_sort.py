import random

value = int(input(" Введите кол-во цифр, введенных в массив: "))
mass = []

for i in range(value):
        count = random.randint(1,100)
        mass.append(count)

print(" Массив чисел ", mass)
	
	

for i in range(len(mass)):

        for j in range(value-i-1):

                if mass[j] > mass[j+1]:

                        mass[j], mass[j+1] = mass[j+1], mass[j]

print(" Отсортированный массив: ", mass)
                
                        


		
			


		

