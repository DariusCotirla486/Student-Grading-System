from jproperties import Properties
from src.repository.TextFileRepo import *
from src.repository.BinaryFileRepo import *


def get_grades_repository():
    configs = Properties()
    with open("settings.properties", "rb") as configs_file:

        configs.load(configs_file)
        repository_in_use = configs.get("REPOSITORY").data
        location_of_repository = configs.get("GRADE").data

        if repository_in_use == "MemoryRepositories":
            return GradesRepository()
        elif repository_in_use == "TextFileRepositories":
            return TextGradesRepository(location_of_repository)
        elif repository_in_use == "BinaryFileRepositories":
            return BinaryGradeRepository(location_of_repository)


def get_students_repository():
    configs = Properties()
    with open("settings.properties", "rb") as configs_file:

        configs.load(configs_file)
        repository_in_use = configs.get("REPOSITORY").data
        location_of_repository = configs.get("STUDENT").data

        if repository_in_use == "MemoryRepositories":
            return StudentRepository()
        elif repository_in_use == "TextFileRepositories":
            return TextStudentsRepository(location_of_repository)
        elif repository_in_use == "BinaryFileRepositories":
            return BinaryStudentRepository(location_of_repository)


def get_disciplines_repository():
    configs = Properties()
    with open("settings.properties", "rb") as configs_file:

        configs.load(configs_file)
        repository_in_use = configs.get("REPOSITORY").data
        location_of_repository = configs.get("DISCIPLINE").data

        if repository_in_use == "MemoryRepositories":
            return DisciplineRepository()
        elif repository_in_use == "TextFileRepositories":
            return TextDisciplinesRepository(location_of_repository)
        elif repository_in_use == "BinaryFileRepositories":
            return BinaryDisciplineRepository(location_of_repository)
