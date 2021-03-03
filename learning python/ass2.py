# ass - grade
# alot of if-else statement
# dictionary 



print ('Check Your Grade Class')
score_Code = input('Enter course code:\n')
score = int(input('Enter Your Score(Ranging from 0-100):\n'))

if score >= 70:
    print("Your Grade Class in ", score_Code, "is 'A'")
elif score >= 60:
    print("Your Grade Class in ", score_Code, " is 'B'")
elif score >= 50:
    print("Your Grade Class in ", score_Code, " is 'C'")
elif score >= 40:
    print("Your Grade Class in ", score_Code, " is 'D'")
else:
    print("Your Grade Class in ", score_Code, " is 'F'")