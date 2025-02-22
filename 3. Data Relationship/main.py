from classes import University, Student, Course



#Script to create a university and manades student and courses enrollments.
if __name__ == "__main__":
    # Create a University object
    university = University()

    # Create a student object
    student1 = Student("John Doe")
    student2 = Student("Jane Doe")

    # Create a course object
    course1 = Course("Python")
    course2 = Course("Java")

    # Enroll student1 for course1
    university.enroll(student1, course1)

    # Enroll student1 for course2
    university.enroll(student1, course2)

    # Enroll student2 for course1
    university.enroll(student2, course1)

    # Get courses student1 is enrolled for
    print(f"{student1.name} is enrolled for: {[course for course in university.get_student_courses(student1)]}")

    # Get students enrolled for course1
    print(f"{course1.name} has students: {[student for student in university.get_course_students(course1)]}")

    # Drop course1 for student1
    university.drop(student1, course1)

    # Get courses student1 is enrolled for
    print(f"{student1.name} is enrolled for: {[course for course in university.get_student_courses(student1)]}")

    # Get students enrolled for course1
    print(f"{course1.name} has students: {[student for student in university.get_course_students(course1)]}")