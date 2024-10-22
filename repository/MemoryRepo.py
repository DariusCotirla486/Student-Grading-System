from src.domain.Domain import *
from src.repository.RepoError import RepositoryError


class StudentRepository:

    def __init__(self):
        self._student_list = []

    def add_student(self, student: Student):
        self._student_list.append(student)

    def get_name_of_student(self, student_id):
        for student in self._student_list:
            if student.get_student_id() == student_id:
                name_of_student = student.get_student_name()
                return name_of_student

    def check_if_student_already_exists(self, checked_id):
        for student in self._student_list:
            if student.get_student_id() == checked_id:
                raise RepositoryError("Student already exists!")

    def check_if_student_does_not_exist(self, checked_id):
        exist = False
        for student in self._student_list:
            if student.get_student_id() == checked_id:
                exist = True
        if not exist:
            raise RepositoryError("Student does not exist.")

    def students(self):
        return self._student_list[:]

    def remove_student(self, id_of_student_removed):
        for student in self._student_list:
            student_id = student.get_student_id()
            if student_id == id_of_student_removed:
                self._student_list.remove(student)

    def update_student_list(self, new_student_list):
        self._student_list = new_student_list

    def empty_student_list(self):
        self._student_list.clear()


class DisciplineRepository:

    def __init__(self):
        self._discipline_list = []

    def add_discipline(self, discipline: Discipline):
        self._discipline_list.append(discipline)

    def get_name_of_discipline(self, discipline_id):
        for discipline in self._discipline_list:
            if discipline.get_discipline_id() == discipline_id:
                discipline_name = discipline.get_discipline_name()
                return discipline_name

    def disciplines(self):
        return self._discipline_list[:]

    def check_if_discipline_already_exists(self, checked_id):
        for discipline in self._discipline_list:
            if discipline.get_discipline_id() == checked_id:
                raise RepositoryError("Discipline already exists!")

    def check_if_discipline_does_not_exist(self, checked_id):
        exist = False
        for discipline in self._discipline_list:
            if discipline.get_discipline_id() == checked_id:
                exist = True
        if not exist:
            raise RepositoryError("Discipline does not exist.")

    def remove_discipline_from_disciplines_list(self, id_of_discipline_removed):
        position_of_discipline_removed = -1
        ok = 0
        for discipline in self._discipline_list:
            position_of_discipline_removed += 1
            if discipline.get_discipline_id() == id_of_discipline_removed:
                ok = 1
                break
        if ok:
            self._discipline_list.pop(position_of_discipline_removed)
        else:
            raise RepositoryError("Invalid ID!")

    def update_discipline_list(self, new_discipline_list):
        self._discipline_list = new_discipline_list

    def empty_discipline_list(self):
        self._discipline_list.clear()


class GradesRepository:

    def __init__(self):
        self._grades_list = []

    def add_grade(self, grade: Grade):
        self._grades_list.append(grade)

    def remove_grade(self, student_id, discipline_id):
        position_removed = -1
        ok = 0
        for grade in self._grades_list:
            position_removed += 1
            if grade.get_graded_student_id() == student_id and grade.get_graded_discipline_id() == discipline_id:
                ok = 1
                break
        if ok:
            self._grades_list.pop(position_removed)
        else:
            raise RepositoryError("Invalid student/discipline id!")

    def grades(self):
        return self._grades_list[:]
