from src.services.UndoRedoService import UndoService
from src.services.Services import Service
from src.repository.RepoError import RepositoryError
from src.repository.UndoRedoError import UndoRedoError


class UI:

    def __init__(self):
        self.undo_service = UndoService()
        self.__service = Service(self.undo_service)

    def add_student_ui(self):
        student_id = int(input("Student ID: "))
        self.__service.check_if_student_exists_already(student_id)
        student_name = input("Student name: ")
        self.__service.add_student_to_repository(student_id, student_name)

    def remove_student_ui(self):
        student_id_removed = int(input("ID of the Student removed: "))
        self.__service.check_if_student_doesnt_exist(student_id_removed)
        self.__service.remove_student_from_repository(student_id_removed)
        self.__service.remove_grades_of_student_removed(student_id_removed)

    def add_discipline_ui(self):
        discipline_id = int(input("Discipline ID: "))
        self.__service.check_if_discipline_exists_already(discipline_id)
        discipline_name = input("Discipline name: ")
        self.__service.add_discipline_to_repository(discipline_id, discipline_name)

    def remove_discipline_ui(self):
        discipline_id_removed = int(input("ID of the Discipline removed: "))
        self.__service.check_if_discipline_doesnt_exist(discipline_id_removed)
        self.__service.remove_discipline_from_repository(discipline_id_removed)
        self.__service.remove_grades_of_discipline_removed(discipline_id_removed)

    def grade_student_ui(self):
        id_of_student_graded = int(input("ID of Student graded: "))
        id_of_discipline = int(input("ID of Discipline: "))
        self.__service.check_if_discipline_doesnt_exist(id_of_discipline)
        self.__service.check_if_student_doesnt_exist(id_of_student_graded)
        grade = int(input("Grade: "))
        self.__service.grade_student(id_of_student_graded, id_of_discipline, grade)

    def search_students_ui(self):
        name_or_id_searched = input("Enter name or ID of Student (ID must be int): ")
        returned_list_of_students = self.__service.search_students(name_or_id_searched)
        if returned_list_of_students:
            for student in returned_list_of_students:
                print(student.to_string())
        else:
            raise RepositoryError("No student found.")

    def search_disciplines_ui(self):
        name_or_id_searched = input("Enter name or ID of Discipline (ID must be int): ")
        returned_list_of_disciplines = self.__service.search_disciplines(name_or_id_searched)
        if returned_list_of_disciplines:
            for discipline in returned_list_of_disciplines:
                print(discipline.to_string())
        else:
            raise RepositoryError("No discipline found.")

    def show_failing_students_ui(self):
        failing_students = self.__service.failing_students()
        if failing_students:
            for student in failing_students:
                print(f"{student.get_student_name()} - ID: {student.get_student_id()}")
        else:
            raise RepositoryError("No students are failing.")

    def show_disciplines_with_1_or_more_grades_ui(self):
        name_of_discipline, id_of_discipline, average_grade_of_discipline = 0, 1, 2
        disciplines_with_grades = self.__service.graded_disciplines()
        if disciplines_with_grades:
            for index in range(len(disciplines_with_grades)):
                for another_index in range(index, len(disciplines_with_grades)):
                    if disciplines_with_grades[index][average_grade_of_discipline] < disciplines_with_grades[another_index][average_grade_of_discipline]:
                        copy_of_discipline = disciplines_with_grades[index]
                        disciplines_with_grades[index] = disciplines_with_grades[another_index]
                        disciplines_with_grades[another_index] = copy_of_discipline
            for discipline in disciplines_with_grades:
                print(f"{discipline[name_of_discipline]}, ID: {discipline[id_of_discipline]}, Average Grade: {discipline[average_grade_of_discipline]}")
        else:
            raise RepositoryError("No discipline has 1 or more grades.")

    def show_best_situation_ui(self):
        student_name, student_id, student_average = 0, 1, 2
        situations_of_students = self.__service.students_with_the_best_situations()
        for index in range(len(situations_of_students)):
            for another_index in range(index, len(situations_of_students)):
                if situations_of_students[index][student_average] < situations_of_students[another_index][student_average]:
                    copy_of_student = situations_of_students[index]
                    situations_of_students[index] = situations_of_students[another_index]
                    situations_of_students[another_index] = copy_of_student
        place = 1
        for student in situations_of_students:
            print(f"Place {place} - Student {student[student_name]} with an average grade of: {student[student_average]}")
            place += 1
            if place == 6:
                break

    def list_students(self):
        students_list = self.__service.get_all_students()
        for student in students_list:
            print(student.to_string())

    def list_disciplines(self):
        disciplines_list = self.__service.get_all_disciplines()
        for discipline in disciplines_list:
            print(discipline.to_string())

    def list_grades(self):
        grades_list = self.__service.get_all_grades()
        for grade in grades_list:
            print(grade.to_string())

    def print_student_management(self):
        print("\n"
              "1. Add a student \n"
              "2. Remove a student \n"
              "3. List all students \n"
              "4. Search students by ID \n"
              "5. List failing students \n")

    def print_grades_management(self):
        print("\n"
              "1. Grade a student \n"
              "2. List all grades \n"
              "3. List the students with the best school situation \n")

    def print_disciplines_management(self):
        print("\n"
              "1. Add a discipline \n"
              "2. Remove a discipline \n"
              "3. List all disciplines \n"
              "4. Search discipline by ID \n"
              "5. List disciplines with 1 or more grades \n")

    def print_options(self):
        print("\n"
              "1. Manage students \n"
              "2. Manage disciplines \n"
              "3. Manage grades \n")

    def start_ui(self):

        manage_students, manage_disciplines, manage_grades = "1", "2", "3"
        add_student, add_discipline, grade_student = "1", "1", "1"
        remove_student, remove_discipline = "2", "2"
        list_students, list_disciplines, list_grades = "3", "3", "2"
        search_students, search_disciplines = "4", "4"
        show_failing_students, show_disciplines_with_1_or_more_grades, show_best_situation = "5", "5", "3"
        exit_program, undo, redo = "exit", "undo", "redo"
        self.__service.generate_20_random_disciplines()
        self.__service.generate_20_random_students()
        self.__service.generate_20_random_grades()
        while True:
            try:

                self.print_options()
                chosen_option = input(">> ")
                if chosen_option == manage_students:
                    self.print_student_management()
                    option_for_students = input(">> ")
                    if option_for_students == add_student:
                        self.add_student_ui()
                    elif option_for_students == remove_student:
                        self.remove_student_ui()
                    elif option_for_students == list_students:
                        self.list_students()
                    elif option_for_students == search_students:
                        self.search_students_ui()
                    elif option_for_students == show_failing_students:
                        self.show_failing_students_ui()

                elif chosen_option == manage_disciplines:
                    self.print_disciplines_management()
                    option_for_disciplines = input(">> ")
                    if option_for_disciplines == add_discipline:
                        self.add_discipline_ui()
                    elif option_for_disciplines == remove_discipline:
                        self.remove_discipline_ui()
                    elif option_for_disciplines == list_disciplines:
                        self.list_disciplines()
                    elif option_for_disciplines == search_disciplines:
                        self.search_disciplines_ui()
                    elif option_for_disciplines == show_disciplines_with_1_or_more_grades:
                        self.show_disciplines_with_1_or_more_grades_ui()

                elif chosen_option == manage_grades:
                    self.print_grades_management()
                    option_for_grades = input(">> ")
                    if option_for_grades == grade_student:
                        self.grade_student_ui()
                    elif option_for_grades == list_grades:
                        self.list_grades()
                    elif option_for_grades == show_best_situation:
                        self.show_best_situation_ui()

                elif chosen_option == exit_program:
                    exit()
                try:
                    if chosen_option == undo:
                        self.undo_service.undo()
                    elif chosen_option == redo:
                        self.undo_service.redo()
                except UndoRedoError as error:
                    print(error)

            except RepositoryError as error:
                print(error)
