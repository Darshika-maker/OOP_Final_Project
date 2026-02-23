from models.student import Student
from models.course import Course
from repositories.student_repository import StudentRepository


class InMemoryStudentRepository(StudentRepository):

    def __init__(self):
        self._students = self._create_students()

    def _create_students(self):
        s1 = Student("James Bond", "S001", "James1")
        s1.add_course(Course("ICT Business", 5, 4))
        s1.add_course(Course("Data Management Systems", 5, 4))
        s1.add_course(Course("A1", 5, 0, "upcoming"))

        s2 = Student("Elon Musk", "S002", "Elon2")
        s2.add_course(Course("Programming", 5, 5))
        s2.add_course(Course("AI", 5, 4))
        s2.add_course(Course("A2", 5, 0, "upcoming"))

        s3 = Student("Anna Brown", "S003", "Anna3")
        s3.add_course(Course("Networks", 5, 3))
        s3.add_course(Course("Security", 5, 4))
        s3.add_course(Course("A3", 5, 0, "upcoming"))

        s4 = Student("Maria Garcia", "S004", "Maria4")
        s4.add_course(Course("Math", 5, 4))
        s4.add_course(Course("Databases", 5, 5))
        s4.add_course(Course("A4", 5, 0, "upcoming"))

        s5 = Student("John Smith", "S005", "John5")
        s5.add_course(Course("Cloud Computing", 5, 4))
        s5.add_course(Course("DevOps", 5, 4))

        return [s1, s2, s3, s4, s5]

    def find_by_id(self, student_id: str):
        for student in self._students:
            if student.get_student_id() == student_id:
                return student
        return None

    def get_all_students(self):
        return self._students