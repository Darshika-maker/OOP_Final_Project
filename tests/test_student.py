import unittest
from models.student import Student
from models.course import Course
from services.transcript_service import TranscriptService

class TestStudentSystem(unittest.TestCase):

    def test_gpa_calculation_only_finished(self):
        student = Student("Test Student", "S999", "pass")
        # Finished courses
        student.add_course(Course("Python", 5, 5, "finished"))
        student.add_course(Course("Math", 5, 3, "finished"))
        # Upcoming course should not count
        student.add_course(Course("AI", 5, 0, "upcoming"))

        service = TranscriptService()
        gpa = service.calculate_gpa(student)

        self.assertEqual(gpa, 4.0)

    def test_no_finished_courses_gpa(self):
        student = Student("No Finished", "S998", "pass")
        student.add_course(Course("Future Course", 5, 0, "upcoming"))

        service = TranscriptService()
        gpa = service.calculate_gpa(student)

        self.assertEqual(gpa, 0.0)

if __name__ == "__main__":
    unittest.main()
