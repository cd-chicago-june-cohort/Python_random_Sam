import random 

#print random.randint(50,100)

def give_grades():
    print "Scores and Grades"
    for i in range(11):
        score = random.randint(60,101)
        if score >= 60 and score < 70:
            grade = 'D'
        elif score >= 70 and score < 80:
            grade = 'C'
        elif score >= 80 and score < 90:
            grade = 'B'
        else:
            grade = 'A'
        print "Score: " + str(score) + "; Your grade is " + grade
    print "End of program. Bye!"

give_grades()
