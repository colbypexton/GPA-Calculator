
course_name = []
grades = []
class_credits = []
converted_grades = []
qualitypoints = []
qptotal = 0.0
credittotal = 0.0
pctoken = 0
semestercount = 0


def qpcollection():
    total = 0.0
    for i in qualitypoints:
        total += i
    return total


def creditcollection():
    total = 0.0
    for i in class_credits:
        total += i
    return total


def convertgrade():
    for grade in grades:
        if grade == 'A':
            converted_grades.append(4.00)
        elif grade == 'A-':
            converted_grades.append(3.70)
        elif grade == 'B+':
            converted_grades.append(3.30)
        elif grade == 'B':
            converted_grades.append(3.00)
        elif grade == 'B-':
            converted_grades.append(2.70)
        elif grade == 'C+':
            converted_grades.append(2.30)
        elif grade == 'C':
            converted_grades.append(2.00)
        elif grade == 'C-':
            converted_grades.append(1.70)
        elif grade == 'D+':
            converted_grades.append(1.30)
        elif grade == 'D':
            converted_grades.append(1.00)
        elif grade == 'F':
            converted_grades.append(0.00)
        else:
            converted_grades.append(0.00)


def gpacalc():
    qpcount = 0.0
    creditcount = 0.0
    for i in qualitypoints:
        qpcount += i
    for j in class_credits:
        creditcount += j
    semgpa = qpcount / creditcount
    return semgpa


print('Welcome to the GPA calculator.')

decision = input('Would you like to calculate a semester?').upper()[0]
while decision == 'Y':
    pctoken = 1
    semestercount += 1
    num_classes = int(input('How many courses did you take in the semester?'))
    for i in range(num_classes):
        course = input(f'Name of Course {i + 1}:')
        course_name.append(course)
        grade_recieved = input('Grade Recieved:').upper()
        grades.append(grade_recieved)
        numberofcredits = float(input('Credits associated with class:'))
        class_credits.append(numberofcredits)

    convertgrade()

    for i in range(len(converted_grades)):
        qualitypoints.append(converted_grades[i] * class_credits[i])

    print('Course', '\t', 'Credits', '\t', 'Grade', '\t', 'Quality Points')
    for i in range(len(course_name)):
        print(course_name[i], '\t', round(class_credits[i]),
              '\t', '\t', grades[i], '\t', '{0:.1f}'.format(qualitypoints[i]))

    gpa = gpacalc()
    total_credits = 0.0
    for i in class_credits:
        total_credits += i

    print(f'Your semester credits earned: {round(total_credits)}')
    print(f'Your semsester GPA: {round(gpa, 2)}')
    decision = input(
        'Would you like to calculate another semester?').upper()[0]

    qptotal += qpcollection()
    credittotal += creditcollection()

    course_name = []
    grades = []
    class_credits = []
    converted_grades = []
    qualitypoints = []


if pctoken == 1 and semestercount > 1:
    print('')
    print('')
    print(f'Semesters calculated: {semestercount}')
    print(f'Your overall GPA: {round(qptotal/credittotal, 2)}')
    print(f'Your total amount of credits: {round(credittotal)}')
    print('Thank you for using the sowftware!')
else:
    print('Thank you for using the software!')
