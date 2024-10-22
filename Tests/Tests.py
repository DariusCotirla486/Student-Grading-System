from src.services.Services import Service
from src.repository.RepoError import RepositoryError
from src.services.UndoRedoService import UndoService


class Test:
    def __init__(self):
        self.undo_service = UndoService()
        self.__service = Service(self.undo_service)

    def test_add_student(self):
        self.__service.add_student_to_repository(100, "John")
        assert len(self.__service.get_all_students()) == 1
        self.__service.add_student_to_repository(200, "Michael")
        assert len(self.__service.get_all_students()) == 2
        try:
            self.__service.add_student_to_repository(100, "John")
            assert True
        except RepositoryError:
            assert False

    def test_remove_student(self):
        self.__service.add_student_to_repository(1000, "John")
        self.__service.add_student_to_repository(2000, "Mary")
        self.__service.remove_student_from_repository(1000)
        assert len(self.__service.get_all_students()) == 4

    def test_add_discipline(self):
        self.__service.add_discipline_to_repository(21, "Matematica")
        assert len(self.__service.get_all_disciplines()) == 1
        self.__service.add_discipline_to_repository(22, "Informatica")
        assert len(self.__service.get_all_disciplines()) == 2

    def test_remove_discipline(self):
        self.__service.add_discipline_to_repository(23, "Matematica")
        self.__service.add_discipline_to_repository(24, "Informatica")
        self.__service.remove_discipline_from_repository(23)
        assert len(self.__service.get_all_disciplines()) == 3

    def test_all(self):
        self.test_add_student()
        self.test_remove_student()
        self.test_add_discipline()
        self.test_remove_discipline()
        print("All tests passed")
