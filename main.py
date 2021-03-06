import sys


from PyQt5.QtWidgets import QApplication
from view import GUI
from model import evaluateExpression
from controller import Controller

Controller(model=model, view=view)

model = evaluateExpression
# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()


sys.exit(pycalc.exec_())
if __name__ == '__main__':
    main()