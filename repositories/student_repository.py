from abc import ABC, abstractmethod


class StudentRepository(ABC):

    @abstractmethod
    def find_by_id(self, student_id: str):
        pass

    @abstractmethod
    def get_all_students(self):
        pass