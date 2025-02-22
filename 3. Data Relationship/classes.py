# Description: A simple program that simulates a University where students can enroll for
# courses and courses can have students enrolled for them.

class University:
    """
    A class to represent a University. students can enroll for courses and courses can have students enrolled for them.
    """
    def enroll(self, student: 'Student', course: 'Course'):
        """
        Enroll a student for a course.
        """
        student.enroll_Course(course)

    def get_student_courses(self, student: 'Student'):
        """
        Returns a list of courses the student is enrolled for.
        """
        return student.get_enrolled_courses()


    def get_course_students(self, course: "Course"):
        """
        Returns a list of students enrolled for the course.
        """
        return course.get_students()
    def drop(self, student: 'Student', course: 'Course'):
        """
        Drop a course for a student.
        """
        student.drop_course(course)



####################################################################################################

class Course:
    def __init__(self, name: str):
        self.name = name
        self.students =[]

    def get_students(self):
        """
        Returns a list of students enrolled for the course.

        """
        return self.students or []
    def __repr__(self):
        return self.name
####################################################################################################
class Student:
    def __init__(self,  name:str):
        self.name = name
        self.courses = []

    def enroll_Course(self, course: Course):
        """
        Enroll a student for a course only if the student is not already enrolled for the course.
        """
        if course not in self.courses:
            self.courses.append(course) # add new course to list of enrolled courses
            course.students.append(self) # add new student to list of enrolled student for the specified course
        else:
            raise ValueError(f"You have already enrolled for {course.name}")

    def get_enrolled_courses(self):
        """
        Returns a list of courses the student is enrolled for.
        """
        #Returns courses if there are any, otherwise return an empty list
        return self.courses or []

    def drop_course(self, course: Course):
        """
        Drop a course for a student.
        """
        if course in self.courses:
            self.courses.remove(course) # remove course from list of enrolled courses
            course.students.remove(self) # remove student from list of enrolled students for the specified course
        else:
            raise ValueError(f"You are not enrolled for {course.name}")

    def __repr__(self):
        return self.name