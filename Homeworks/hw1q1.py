#Elif Roza Seyidoğlu

#Create a List and swap the second half of the list with the first half of
#the list and print this list on the screen

list = [13, 10, 27, 50, 22, 98] #a list has created
l = len(list)  # length of the list is assigned as l

# list is seperated as first half(rightside) and second half(leftside)
rightside = list[0:int(l/2):1]
leftside = list[int(l/2):int(l):1]

#swapped list created as combination of both half sides in asked order
swapList = leftside + rightside
print(swapList)
