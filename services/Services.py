import random
from src.propertiesparser import PropertiesParser
from src.repository.MemoryRepo import *
from src.domain.CallableCommands import *


def average_grade(grades_list):
    return sum(grades_list)/len(grades_list)


class Service:

    def __init__(self, undo_redo_service):
        self.__student_repository = PropertiesParser.get_students_repository()
        self.__discipline_repository = PropertiesParser.get_disciplines_repository()
        self.__grades_repository = PropertiesParser.get_grades_repository()
        self.UndoRedoService = undo_redo_service

    def add_student_to_repository(self, student_id, student_name):
        new_student = Student(student_id, student_name)
        self.__student_repository.add_student(new_student)
        undo_command = CommandThatCanBeCalled(self.__student_repository.remove_student, student_id)
        redo_command = CommandThatCanBeCalled(self.__student_repository.add_student, new_student)
        undo_redo_command = [Operation(undo_command, redo_command)]
        self.UndoRedoService.register_operation(OperationThatCascades(undo_redo_command))

    def remove_student_from_repository(self, id_of_student_removed):
        student_name = self.__student_repository.get_name_of_student(id_of_student_removed)
        self.__student_repository.remove_student(id_of_student_removed)
        student_removed = Student(id_of_student_removed, student_name)
        undo_command = CommandThatCanBeCalled(self.__student_repository.add_student, student_removed)
        redo_command = CommandThatCanBeCalled(self.__student_repository.remove_student, id_of_student_removed)
        undo_redo_command = [Operation(undo_command, redo_command)]
        self.UndoRedoService.register_operation(OperationThatCascades(undo_redo_command))

    def add_discipline_to_repository(self, discipline_id, discipline_name):
        new_discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.add_discipline(new_discipline)
        redo_command = CommandThatCanBeCalled(self.__discipline_repository.add_discipline, new_discipline)
        undo_command = CommandThatCanBeCalled(self.__discipline_repository.remove_discipline_from_disciplines_list, discipline_id)
        undo_redo_command = [Operation(undo_command, redo_command)]
        self.UndoRedoService.register_operation(OperationThatCascades(undo_redo_command))

    def remove_discipline_from_repository(self, id_of_discipline_removed):
        discipline_name = self.__discipline_repository.get_name_of_discipline(id_of_discipline_removed)
        self.__discipline_repository.remove_discipline_from_disciplines_list(id_of_discipline_removed)
        discipline_removed = Discipline(id_of_discipline_removed, discipline_name)
        undo_command = CommandThatCanBeCalled(self.__discipline_repository.add_discipline, discipline_removed)
        redo_command = CommandThatCanBeCalled(self.__discipline_repository.remove_discipline_from_disciplines_list, id_of_discipline_removed)
        undo_redo_command = [Operation(undo_command, redo_command)]
        self.UndoRedoService.register_operation(OperationThatCascades(undo_redo_command))

    def get_all_students(self):
        return self.__student_repository.students()

    def get_all_disciplines(self):
        return self.__discipline_repository.disciplines()

    def get_all_grades(self):
        return self.__grades_repository.grades()

    def check_if_student_exists_already(self, checked_id):
        checked_id = int(checked_id)
        self.__student_repository.check_if_student_already_exists(checked_id)

    def check_if_discipline_exists_already(self, checked_id):
        checked_id = int(checked_id)
        self.__discipline_repository.check_if_discipline_already_exists(checked_id)

    def check_if_student_doesnt_exist(self, checked_id):
        checked_id = int(checked_id)
        self.__student_repository.check_if_student_does_not_exist(checked_id)

    def check_if_discipline_doesnt_exist(self, checked_id):
        checked_id = int(checked_id)
        self.__discipline_repository.check_if_discipline_does_not_exist(checked_id)

    def grade_student(self, graded_student_id, graded_discipline_id, grade):
        new_grade = Grade(int(graded_student_id), int(graded_discipline_id), grade)
        self.__grades_repository.add_grade(new_grade)
        redo_command = CommandThatCanBeCalled(self.__grades_repository.add_grade, new_grade)
        undo_command = CommandThatCanBeCalled(self.__grades_repository.remove_grade, *(graded_student_id, graded_discipline_id))
        undo_redo_command = [Operation(undo_command, redo_command)]
        self.UndoRedoService.register_operation(OperationThatCascades(undo_redo_command))

    def remove_grades_of_student_removed(self, removed_student_id):
        list_of_commands = []
        initial_grades_list = self.__grades_repository.grades()
        for grade in initial_grades_list:
            if grade.get_graded_student_id() == removed_student_id:
                undo_command = CommandThatCanBeCalled(self.__grades_repository.add_grade, grade)
                redo_command = CommandThatCanBeCalled(self.__grades_repository.remove_grade,
                                                      *(grade.get_graded_student_id(),
                                                        grade.get_graded_discipline_id()))
                undo_redo_command = Operation(undo_command, redo_command)
                list_of_commands.append(undo_redo_command)
                self.__grades_repository.remove_grade(grade.get_graded_student_id(), grade.get_graded_discipline_id())

        self.UndoRedoService.register_operation(OperationThatCascades(list_of_commands))

    def remove_grades_of_discipline_removed(self, removed_discipline_id):
        initial_grades_list = self.__grades_repository.grades()
        list_of_commands = []
        for grade in initial_grades_list:
            if grade.get_graded_discipline_id() == removed_discipline_id:
                undo_command = CommandThatCanBeCalled(self.__grades_repository.add_grade, grade)
                redo_command = CommandThatCanBeCalled(self.__grades_repository.remove_grade,
                                                      *(grade.get_graded_student_id(),
                                                        grade.get_graded_discipline_id()))
                undo_redo_command = Operation(undo_command, redo_command)
                list_of_commands.append(undo_redo_command)
                self.__grades_repository.remove_grade(grade.get_graded_student_id(), grade.get_graded_discipline_id())

        self.UndoRedoService.register_operation(OperationThatCascades(list_of_commands))

    def generate_20_random_students(self):
        student_id = 0
        student_names = ["Darius", "Bogdan", "Marius", "Raul", "Vlad", "Paul", "Cezar", "Aurel"]
        for _ in range(20):
            student_id += 1
            new_student = Student(student_id, random.choice(student_names))
            self.__student_repository.add_student(new_student)

    def generate_20_random_disciplines(self):
        discipline_id = 1
        discipline_names = ["","Matematica", "Informatica", "Biologie", "Chimie", "Romana", "Engleza", "Sport",
                            "Engleza-2", "Matematica-2", "Informatica-2", "Chimie-2", "Biologie-2", "Sport-2",
                            "Romana-2", "Informatica-ASC", "Informatica-Engleza", "Informatica-Romana",
                            "Romana-3", "Engleza-3", "Informatica-3"]
        for _ in range(20):
            new_discipline = Discipline(discipline_id, discipline_names[discipline_id])
            self.__discipline_repository.add_discipline(new_discipline)
            discipline_id += 1

    def generate_20_random_grades(self):
        for _ in range(20):
            discipline_id = random.randint(1, 20)
            student_id = random.randint(1, 20)
            grade = random.randint(1, 10)
            new_grade = Grade(student_id, discipline_id, grade)
            self.__grades_repository.add_grade(new_grade)

    def search_students(self, search_parameter: str):
        id_searched = -1
        name_searched = ""
        list_of_searched_students = []
        if search_parameter.isdigit():
            id_searched = int(search_parameter)
        else:
            name_searched = search_parameter
        if id_searched != -1:
            for student in self.__student_repository.students():
                id_of_student = student.get_student_id()
                if id_of_student == id_searched:
                    list_of_searched_students.append(student)
        elif name_searched != "":
            for student in self.__student_repository.students():
                name_of_student = student.get_student_name()
                if name_searched in name_of_student:
                    list_of_searched_students.append(student)
        return list_of_searched_students

    def search_disciplines(self, search_parameter):
        id_searched = -1
        name_searched = ""
        list_of_searched_disciplines = []
        if search_parameter.isdigit():
            id_searched = int(search_parameter)
        else:
            name_searched = search_parameter
        if id_searched != -1:
            for discipline in self.__discipline_repository.disciplines():
                id_of_discipline = discipline.get_discipline_id()
                if id_of_discipline == id_searched:
                    list_of_searched_disciplines.append(discipline)
        elif name_searched != "":
            for discipline in self.__discipline_repository.disciplines():
                name_of_discipline = discipline.get_discipline_name()
                if name_searched in name_of_discipline:
                    list_of_searched_disciplines.append(discipline)
        return list_of_searched_disciplines

    def failing_students(self):
        list_of_failing_students = []
        for student in self.__student_repository.students():
            student_id = student.get_student_id()
            student_name = student.get_student_name()
            failed = False
            for discipline in self.__discipline_repository.disciplines():
                discipline_id = discipline.get_discipline_id()
                grades_of_student_for_discipline = []
                for grade in self.__grades_repository.grades():
                    if discipline_id == grade.get_graded_discipline_id() and student_id == grade.get_graded_student_id():
                        grades_of_student_for_discipline.append(grade.get_grade_value())
                if grades_of_student_for_discipline:
                    if average_grade(grades_of_student_for_discipline) < 5:
                        failed = True
            if failed:
                list_of_failing_students.append(student)
        return list_of_failing_students

    def graded_disciplines(self):
        list_of_graded_disciplines = []
        for discipline in self.__discipline_repository.disciplines():
            discipline_id = discipline.get_discipline_id()
            discipline_name = discipline.get_discipline_name()
            graded = False
            grades_of_discipline = []
            for grade in self.__grades_repository.grades():
                if grade.get_graded_discipline_id() == discipline_id:
                    grades_of_discipline.append(grade.get_grade_value())
                    graded = True
            if graded:
                average_grade_at_discipline = average_grade(grades_of_discipline)
                discipline_with_average_grade = [discipline_name, discipline_id, average_grade_at_discipline]
                list_of_graded_disciplines.append(discipline_with_average_grade)
        return list_of_graded_disciplines

    def students_with_the_best_situations(self):
        situations_of_students = []
        for student in self.__student_repository.students():
            student_id = student.get_student_id()
            student_name = student.get_student_name()
            average_grades_of_student_at_disciplines = []
            for discipline in self.__discipline_repository.disciplines():
                discipline_id = discipline.get_discipline_id()
                grades_of_student_for_discipline = []
                for grade in self.__grades_repository.grades():
                    if grade.get_graded_discipline_id() == discipline_id and grade.get_graded_student_id() == student_id:
                        grades_of_student_for_discipline.append(grade.get_grade_value())
                if grades_of_student_for_discipline:
                    average_grade_at_discipline = average_grade(grades_of_student_for_discipline)
                    average_grades_of_student_at_disciplines.append(average_grade_at_discipline)
            if average_grades_of_student_at_disciplines:
                average_grade_of_student = average_grade(average_grades_of_student_at_disciplines)
                situations_of_students.append([student_name, student_id, average_grade_of_student])
        return situations_of_students
