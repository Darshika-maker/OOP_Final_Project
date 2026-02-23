class Course:
    def __init__(self, name: str, credits: int, grade: float = 0, status: str = "finished"):
        self._name = name
        self._credits = credits
        self._grade = grade
        self._status = status  # "finished" or "upcoming"

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits

    def get_grade(self):
        return self._grade
    
    def get_status(self):
        return self._status

    def __str__(self):
        if self._status == "upcoming":
            return f"{self._name} | Credits: {self._credits} | [UPCOMING]"
        return f"{self._name} | Credits: {self._credits} | Grade: {self._grade}"
