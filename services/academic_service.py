class AcademicService:

    def display_upcoming(self, student):
        upcoming_courses = [c for c in student.get_courses() if c.get_status() == "upcoming"]
        
        print("\n" + "=" * 50)
        print("Upcoming Courses")
        print("=" * 50)
        if not upcoming_courses:
            print("No upcoming courses.")
        else:
            for c in upcoming_courses:
                print(c)
        print("=" * 50 + "\n")
