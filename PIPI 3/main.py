import math
#Exercitiu 1 Write a program to unpack a tuple in several variables
x = (1, 2, 3, 4, 5, 6, 7, 8, 9, "maine", False, None)
#x1, x2, x3, x4 = x Aci depinde de numaru de obiecte din tupel
#print(x1)
#print(x2)

#Exercitiu 2 #Write a program to add an item based on user input
y = int(input())
x += (y, )
print(x)
print(hash(x))

#Exercitiu 3 #Write a program to change a tuple in to a string
z = str(x)
print(type(z))
print(z)

#Exercitiu 4 #Write a program to get the 4th and the last 4th item in a tupel
print(x[4])
print(x[-4])
#Exercitiu 5 #Write a program to convert a list to a tuple
z = str(list(x))
print("aci ii o lista" + str(type(z)))
z = tuple(x)
print("Aci ii un tuple" + str(type(z)))
#Exercitiu 6 #Write a program to slice a tuple
a = x[0:4]
b = x[4:11]
print(a)
print()
print(b)
#Exercitiu 7 #Write a program to find the index of an item of tuple
h = z.index(1)
j = z.index(6)
print(h)
print(j)
#Exercitiu 8 #Write a program to find the length of a tuple
length = len(x)
print(length)
#Exercitiu 9 #Write a program to convert a tuple to a dictionary 
dictionar = dict(x)
print(type(dictionar))

