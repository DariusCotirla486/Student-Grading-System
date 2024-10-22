from src.repository.MemoryRepo import *
import pickle


class BinaryStudentRepository(StudentRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._save_file()

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._student_list, file)
        file.close()

    def _read_from_file(self):
        file = open(self.__file_name, "rb")
        self._student_list = pickle.load(file)
        file.close()

    def __len__(self):
        return len(self._student_list)


class BinaryDisciplineRepository(DisciplineRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._discipline_list, file)
        file.close()

    def _read_from_file(self):
        file = open(self.__file_name, "rb")
        self._discipline_list = pickle.load(file)
        file.close()

    def __len__(self):
        return len(self._discipline_list)


class BinaryGradeRepository(GradesRepository):

    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self._grades_list, file)
        file.close()

    def _read_from_file(self):
        file = open(self.__file_name, "rb")
        self._grades_list = pickle.load(file)
        file.close()

    def __len__(self):
        return len(self._grades_list)
