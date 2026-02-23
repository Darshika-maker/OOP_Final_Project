class AcademicService:
    def display_upcoming(self, student):
        print(f"\n--- Upcoming Courses for {student.get_name()} ---")
        upcoming = [c for c in student.get_courses() if c.get_status() == "upcoming"]
        
        if not upcoming:
            print("No upcoming courses found.")
        else:
            for c in upcoming:
                print(c)
        print("-" * 30)