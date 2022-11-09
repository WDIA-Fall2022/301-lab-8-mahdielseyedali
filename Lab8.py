

#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. 
#Returns the number of Tests
def getNumberOfTests():
    while True:
        user_input = int(input("The number of tests you have written: "))
        try:
            if user_input < 0 or user_input > 100:
                print("Invalid entry entered for number of tests written")
            else:
                print(f"The number of tests you have written: {user_input}")
                return user_input
        except ValueError:
            print("The number you entered is invalid")


#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    assignmentsVar = True
    while assignmentsVar:
        try:
            weight = float(input("The weight of your assignments: "))
            if weight < 0 or weight > 1:
                print("Weight has to be between 0 and 1")

            return weight
        except ValueError:
            print("The value is invalid")



#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    midtermVar = True
    while midtermVar:
        try:
            weight = float(input("The weight of your midterms: "))
            if weight < 0 or weight > 1:
                print("Weight has to be between 0 and 1")
            return weight

        except ValueError:
            print("The value is invalid")


#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    finalVar = True
    while finalVar:
        try:
            weight = float(input("The weight of your final: "))
            if weight < 0 or weight > 1:
                print("Weight has to be between 0 and 1")
            return weight
        except ValueError:
            print("The value is invalid")



#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign,wMidTerm,wFinal):
    return wAssign + wMidTerm + wFinal == 1


#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal):
    return AvgAssignments * wOfAssign + AvgTests * wOfMidTerms + final * wFinal

#convert the numeric grade to a letter according to the conversion table 
#in the course outline
def calculateLetterGrade(numericGrade):
    numericGrade = float(input("What is your score?: "))
    if numericGrade >= 97.0:
        return 'A+'
    elif numericGrade >= 93.0:
        return 'A'
    elif numericGrade >= 90.0:
        return 'A-'
    elif numericGrade >= 87.0:
        return 'B+'
    elif numericGrade >= 83.0:
        return 'B'
    elif numericGrade >= 80.0:
        return 'B-'
    elif numericGrade >= 77.0:
        return 'C+'
    elif numericGrade >= 73.0:
        return 'C'
    elif numericGrade >= 70.0:
        return 'C-'
    elif numericGrade >= 67.0:
        return 'D+'
    elif numericGrade >= 65.0:
        return 'D'
    else:
        return 'F'

#Get the weight value of the assignments (call the appropriate function)
#Get the weight value of tests (call the appropriate function)
#Get the weight value of the final (call the appropriate function)
#Check the sum of weight values is 1 (call the appropriate function)
#Repeat the last four lines if not equal to 1
done = False
w_assignments = None
w_tests = None
w_final = None
while not done:
    w_assignments = getWeightOfAssignments()
    w_tests = getWeightOfMidTerms()
    w_final = getWeightOfFinal()

    if checkWeights(w_assignments, w_tests, w_final):
        done = True
    else:
        print("The weights you entered do not add up to 1")

#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100

while True:
    try:
        averageAssignments = float(input("What is the average for your assignments: "))

        if averageAssignments < 0 or averageAssignments > 100:
            print("Enter a number between 0 and 100")
        else:
            print(f"Average of assignments:  {averageAssignments}")
            break
    except ValueError:
            print("Please try again with a number")



#Get the number of tests (call the appropriate function)
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.

num_tests = getNumberOfTests()
total = 0
print('Enter the grade for each of the tests taken. Grades must be between 0 and 100')
for i in range(num_tests):
    try:
        t_grade = float(input("Enter the grade for your test: "))
    except ValueError:
        print("Enter a number")
    else:
        if 0 > t_grade or t_grade > 100:
            print("Number must be between 0 and 100")
        else:
            total += t_grade
averageOfTests = total / num_tests

#Prompt and get the final grade
#Validate the input as a float between 0 and 100

while True:
    try:
        finalGrade = float(input("What was your final grade: "))
        break
    except ValueError:
        print("Enter a number between 0 and 100")


#Calculate and display the final numeric grade (call the appropriate function)

numericGrade = calculateNumericGrade(averageAssignments, averageOfTests, finalGrade, w_assignments, w_tests, w_final)

print(f'Your numerical grade is: {numericGrade}')

#Calculate and display the final alphabetical grade (call the appropriate function)

alphabeticalGrade = calculateLetterGrade(numericGrade)

print(f'Your alphabetical grade is: {alphabeticalGrade}')
