class Student:
    def __init__(self, name: str, student_id: str, password: str):
        self._name = name
        self._student_id = student_id
        self._password = password
        self._courses = []

    def add_course(self, course):
        self._courses.append(course)

    def get_courses(self):
        return self._courses

    def get_name(self):
        return self._name

    def get_student_id(self):
        return self._student_id

    def get_password(self):
        return self._password