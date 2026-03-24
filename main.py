# Write your solution here
def add_student(students_database: dict, student_name: str):
    students_database[student_name] = []
    
def print_student(students_database: dict, student_name: str):
    
    if student_name not in students_database:
        print(f"{student_name}: no such person in the database")
        return
    else:
        current_student = students_database[student_name]
        if len(current_student) == 0:
            print(f"{student_name}:")
            print(" no completed courses")
        else:
            print(student_name + ":")
            print(f" {len(current_student)} completed courses:")
                
            sum = 0
            for course in current_student:
                print(f"  {course[0]} {course[1]}")
                sum += course[1]
                
            average_grade = sum / len(current_student)
            print(f" average grade {average_grade}")
                

def add_course(students_databse: dict, student_name: str, course: tuple):
    if student_name not in students_databse:
        add_student(students_database, student_name)
        
    current_student = students_databse[student_name]
    
    if course[1] == 0: return
    found = False
    for i in range(len(current_student)):
        if current_student[i][0] == course[0]:
            found = True
            # Only update if the NEW grade is higher
            if course[1] > current_student[i][1]:
                current_student[i] = course # Replace the whole tuple
            break # We found it, no need to keep looping
        
    if not found:
        current_student.append(course)
        
def summary(students_database: dict):
    # function to print the summary of the database
    # Needd to track the total number of students
    # Student with the most courses (and how many they have)
    # Student with the highest average grade (and what that grade is)
    total_students = len(students_database)
    print(f"students {total_students}")
    
    most_courses_count = 0
    most_courses_student = ""
    
    best_average_grade = 0
    best_average_student = ""
    
    averages_list = []
    
    #      key         value
    for student_name, courses in students_database.items():
        # 1. Check most courses
        # Use len(courses)
        if len(courses) > most_courses_count:
            most_courses_student = student_name
            most_courses_count = len(courses)        
        
        # 2. Calculate current student's average grade
        # sum of grades / len(courses)
        
        grades = []
        for course in courses:
            grades.append(course[1])
        sum_of_grades = sum(grades)
        
        average = sum_of_grades / len(grades)
        
        # 3. Calculate if this average is the best so far
        if average > best_average_grade:
            best_average_grade = average
            best_average_student = student_name
        
    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_average_grade} {best_average_student}")
            
    
    
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)   