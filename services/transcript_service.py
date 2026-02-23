class TranscriptService:

    def calculate_gpa(self, student):
        total_points = 0
        total_credits = 0

        for c in student.get_courses():
            total_points += c.get_grade() * c.get_credits()
            total_credits += c.get_credits()

        if total_credits == 0:
            return 0.0

        return total_points / total_credits

    def display_transcript(self, student):
        gpa = self.calculate_gpa(student)

        print("\n" + "=" * 50)
        print("KARELIA University of Applied Sciences")
        print("=" * 50)

        print(f"Student Name: {student.get_name()}")
        print(f"Student ID:   {student.get_student_id()}")
        print("-" * 50)

        for c in student.get_courses():
            print(c)

        print("-" * 50)
        print(f"Total Credits: {sum(c.get_credits() for c in student.get_courses())}")
        print(f"GPA: {gpa:.2f}")
        print("=" * 50 + "\n")