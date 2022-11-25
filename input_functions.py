courses = {}

print('This is the list of courses before adding a student')
print(courses)

student = {
    'name' : 'Sam',
    'course_name' : 'Business IT',
    'Year_of_study' : 1,
    'Grades_obtained' : [60, 90, 30]
}

courses.update({'11011' : student})

print('Course list after adding a student:')
print(courses)

            