from src.repository.MemoryRepo import *


class TextStudentsRepository(StudentRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._save_file()

    def __to_string(self):
        string_that_contains_students = ""
        for student in self._student_list:

            string_that_contains_students += (str(student.get_student_id()) + '|' +
                                              str(student.get_student_name()) + "\n")
        return string_that_contains_students

    def _save_file(self):
        with open(self.__file_name, "w") as file:
            file.truncate(0)
            file.write(self.__to_string())

    def _read_from_file(self):
        student_id_index = 0
        student_name_index = 1
        with open(self.__file_name, "r") as file:
            for line in file:

                line = line.strip()
                if line == "":
                    continue

                elements_of_line = line.split('|')
                student_id = elements_of_line[student_id_index]
                student_name = elements_of_line[student_name_index]
                read_student = Student(student_id, student_name)
                self._student_list.append(read_student)


class TextDisciplinesRepository(DisciplineRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._save_file()

    def __to_string(self):
        string_that_contains_disciplines = ""
        for discipline in self._discipline_list:

            string_that_contains_disciplines += (str(discipline.get_discipline_id()) +
                                                 '|' + str(discipline.get_discipline_name()) + "\n")
        return string_that_contains_disciplines

    def _save_file(self):
        with open(self.__file_name, "w") as file:
            file.truncate(0)
            file.write(self.__to_string())

    def _read_from_file(self):
        discipline_id_index = 0
        discipline_name_index = 1
        with open(self.__file_name, "r") as file:
            for line in file:

                line = line.strip()
                if line == "":
                    continue

                elements_of_line = line.split('|')
                discipline_id = elements_of_line[discipline_id_index]
                discipline_name = elements_of_line[discipline_name_index]
                read_discipline = Discipline(discipline_id, discipline_name)
                self._discipline_list.append(read_discipline)


class TextGradesRepository(GradesRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._save_file()

    def __to_string(self):
        string_that_contains_grades = ""
        for grade in self._grades_list:

            string_that_contains_grades += (str(grade.get_graded_student_id()) + '|' +
                                            str(grade.get_graded_discipline_id() + '|' +
                                            str(grade.get_grade_value()) + "\n"))
        return string_that_contains_grades

    def _save_file(self):
        with open(self.__file_name, "w") as file:
            file.truncate(0)
            file.write(self.__to_string())

    def _read_from_file(self):
        graded_student_id_index = 0
        graded_discipline_id_index = 1
        grade_value_index = 2
        with open(self.__file_name, "r") as file:
            for line in file:

                line = line.strip()
                if line == "":
                    continue

                elements_of_line = line.split('|')
                graded_student_id = elements_of_line[graded_student_id_index]
                graded_discipline_id = elements_of_line[graded_discipline_id_index]
                grade_value = elements_of_line[grade_value_index]
                read_grade = Grade(graded_student_id, graded_discipline_id, grade_value)
                self._grades_list.append(read_grade)