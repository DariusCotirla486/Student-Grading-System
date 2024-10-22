
class Discipline:

    def __init__(self, discipline_id, name):
        self._discipline_id = discipline_id
        self._name = name

    def get_discipline_id(self):
        return self._discipline_id

    def get_discipline_name(self):
        return self._name

    def to_string(self):
        return f"---ID: {self._discipline_id}, Name: {self._name} ---"


class Student:

    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name

    def get_student_id(self):
        return self._student_id

    def get_student_name(self):
        return self._name

    def to_string(self):
        return f"---ID: {self._student_id}, Name: {self._name} ---"


class Grade:

    def __init__(self, student_id, discipline_id, value):
        self._discipline_id = discipline_id
        self._student_id = student_id
        self._grade_value = value

    def get_grade_value(self):
        return self._grade_value

    def get_graded_student_id(self):
        return self._student_id

    def get_graded_discipline_id(self):
        return self._discipline_id

    def to_string(self):
        return f"---Student ID: {self._student_id}, Discipline ID: {self._discipline_id}, Grade: {self._grade_value}---"
