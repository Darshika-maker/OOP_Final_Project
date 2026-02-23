class TranscriptService:

    def calculate_gpa(self, student):
        total_points = 0
        total_credits = 0

        # Only finished courses count toward GPA
        for c in student.get_courses():
            if c.get_status() == "finished":
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

        # Only finished courses are displayed
        finished_courses = [c for c in student.get_courses() if c.get_status() == "finished"]
        if not finished_courses:
            print("No finished courses yet.")
        else:
            for c in finished_courses:
                print(c)

        print("-" * 50)
        total_credits = sum(c.get_credits() for c in finished_courses)
        print(f"Total Credits: {total_credits}")
        print(f"GPA: {gpa:.2f}")
        print("=" * 50 + "\n")
