#Elif Roza Seyidoğlu

# Ask the user to input a single digit integer to a variable n then, print out all of the even numbers from 0 to n

# n value assigned from user through input command
n = input("Dear user, please enter a single digit integer value : ")

#an i integer which starts from smallest even number = 0 and goes to the n value via increasing it one by one
for i in range(int(n) +1):
    # if current i integer is divisible by 2 it is an even number, so print that
    if i%2 == 0 :
        print(i)

    # if current i integer isn't divisible by 2 it is an off number, increase i by 1, then it will be even
    else:
        i+=1

