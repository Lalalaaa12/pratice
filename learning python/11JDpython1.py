"""Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know."""

print ('What number are you thinking?')

user_input =int(input())

checker = user_input %2 

if checker == 0:
    print ("That's an even number! Have another?")
else :
    print("That's an odd number! Have another?")

