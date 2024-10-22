from src.ui.UserInterface import UI
from src.Tests.Tests import Test


def main():

    unit_tests = Test()
    unit_tests.test_all()
    ui = UI()
    ui.start_ui()


main()
