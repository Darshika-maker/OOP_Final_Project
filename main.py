from repositories.memory_repository import InMemoryStudentRepository
from services.transcript_service import TranscriptService
from services.academic_service import AcademicService


def main():
    repository = InMemoryStudentRepository()
    t_service = TranscriptService()
    a_service = AcademicService()

    print("\n--- KARELIA UNIVERSITY LOGIN ---")

    student_id = input("Enter Student ID: ").strip()
    student = repository.find_by_id(student_id)

    if not student:
        print("Error: Student ID not found.")
        return

    # Allow 3 password attempts
    attempts = 3

    while attempts > 0:
        password = input("Enter Password: ").strip()

        if student.get_password() == password:
            print("\nLogin successful!")

            # MENU LOOP
            while True:
                print(f"\nWelcome, {student.get_name()}!")
                print("1. View Transcript (Finished Courses)")
                print("2. View Upcoming Courses")
                print("3. Exit")

                choice = input("\nWhat would you like to view? (1-3): ")

                if choice == "1":
                    t_service.display_transcript(student)
                elif choice == "2":
                    a_service.display_upcoming(student)
                elif choice == "3":
                    print("Goodbye!")
                    return
                else:
                    print("Invalid selection. Please try again.")
            return

        else:
            attempts -= 1
            print(f"Incorrect password. Attempts left: {attempts}")

    print("Too many failed attempts. Program closed.")


if __name__ == "__main__":
    main()
