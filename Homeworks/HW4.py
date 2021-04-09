students = {}

#float_input function asks user for a float type input
#If entered value is invalid, asks for user to type valid input.

def float_input(text):
        while True:
                try:
                        i = int(input(text))
                        return i
                except:
                        print("Please enter a valid number")

#Asking students and details to user
for _ in range(5):
        name = input("Student Name:")
        midterm = float_input("MidTerm grade:")
        project = float_input("Project grade:")
        final = float_input("Final Grade:")
        passing = midterm * (0.3) + project * (0.3) + final * (0.4)
        #Sub Dictionary to define students grades
        grades = {"midterm":midterm,"project":project,"final":final,"passing":passing}

        #Adding student to dictionary
        students[name] = grades

#Sorting Students
copied = students.copy()
sorted_students_list = []
while (len(copied)>0):
        max_point = 0
        max_name = ""
        for name,grades in copied.items():
                if grades["passing"]>max_point:
                        max_name = name
                        max_point = grades["passing"]
        copied.pop(max_name)
        sorted_students_list.append((max_name,students[max_name]))

print("Sorting Students:")
for i in sorted_students_list:
	print(i[0]+":")
	print("    MidTerm Grade:",i[1]["midterm"])
	print("    Project Grade:",i[1]["project"])
	print("    Final Grade:",i[1]["final"])
	print("    Passing Grade:",i[1]["passing"])
