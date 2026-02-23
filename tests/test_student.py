import unittest
from models.student import Student
from models.course import Course
from services.transcript_service import TranscriptService


class TestStudentSystem(unittest.TestCase):

    def test_gpa_calculation(self):
        student = Student("Test", "S999", "pass")
        student.add_course(Course("Python", 5, 5))
        student.add_course(Course("Math", 5, 3))

        service = TranscriptService()
        gpa = service.calculate_gpa(student)

        self.assertEqual(gpa, 4.0)


if __name__ == "__main__":
    unittest.main()