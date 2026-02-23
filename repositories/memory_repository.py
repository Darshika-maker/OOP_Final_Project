from models.student import Student
from models.course import Course
from repositories.student_repository import StudentRepository

class InMemoryStudentRepository(StudentRepository):

    def __init__(self):
        self._students = self._create_students()

    def _create_students(self):

        
        s1 = Student("James Bond", "S001", "James1")
        s1.add_course(Course("Career Planning and Development 1", 2, 3))
        s1.add_course(Course("ICT Business", 5, 3))
        s1.add_course(Course("Finnish 1", 5, 4))
        s1.add_course(Course("Data Management Systems 1",5,2))
        s1.add_course(Course("Digital Technology Essentials",5, 5))
        s1.add_course(Course("Web programming", 5, 0, "upcoming"))
        s1.add_course(Course("Finnish 2", 5, 0, "upcoming"))
        s1.add_course(Course("OOP", 5, 0, "upcoming"))

        s2 = Student("Elon Musk", "S002", "Elon2")
        s2.add_course(Course("Career Planning and Development 1", 2, 5))
        s2.add_course(Course("ICT Business", 5, 5))
        s2.add_course(Course("Finnish 1", 5, 3))
        s2.add_course(Course("Data Management Systems 1",5,5))
        s2.add_course(Course("Digital Technology Essentials",5, 4))
        s2.add_course(Course("Web programming", 5, 0, "upcoming"))
        s2.add_course(Course("Finnish 2", 5, 0, "upcoming"))
        s2.add_course(Course("OOP", 5, 0, "upcoming"))

        s3 = Student("Anura Kumara", "S003", "Anura3")
        s3.add_course(Course("Career Planning and Development 1", 2, 4))
        s3.add_course(Course("ICT Business", 5, 4))
        s3.add_course(Course("Finnish 1", 5, 4))
        s3.add_course(Course("Data Management Systems 1",5,4))
        s3.add_course(Course("Digital Technology Essentials",5, 4))
        s3.add_course(Course("Web programming", 5, 0, "upcoming"))
        s3.add_course(Course("Finnish 2", 5, 0, "upcoming"))
        s3.add_course(Course("OOP", 5, 0, "upcoming"))

        s4 = Student("Stephan Hawkin", "S004", "Stephan4")
        s4.add_course(Course("Career Planning and Development 1", 2, 3))
        s4.add_course(Course("ICT Business", 5, 3))
        s4.add_course(Course("Finnish 1", 5, 3))
        s4.add_course(Course("Data Management Systems 1",5,5))
        s4.add_course(Course("Digital Technology Essentials",5, 5))
        s4.add_course(Course("Web programming", 5, 0, "upcoming"))
        s4.add_course(Course("Finnish 2", 5, 0, "upcoming"))
        s4.add_course(Course("OOP", 5, 0, "upcoming"))

        s5 = Student("Stew Jobs", "S005", "stew5")
        s5.add_course(Course("Career Planning and Development 1", 2, 3))
        s5.add_course(Course("ICT Business", 5, 4))
        s5.add_course(Course("Finnish 1", 5, 3))
        s5.add_course(Course("Data Management Systems 1",5,5))
        s5.add_course(Course("Digital Technology Essentials",5, 5))
        s5.add_course(Course("Web programming", 5, 0, "upcoming"))
        s5.add_course(Course("Finnish 2", 5, 0, "upcoming"))
        s5.add_course(Course("OOP", 5, 0, "upcoming"))

        return [s1, s2, s3, s4, s5]

    def find_by_id(self, student_id: str):
        for student in self._students:
            if student.get_student_id() == student_id:
                return student
        return None

    def get_all_students(self):
        return self._students
