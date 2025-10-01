import unreal
import sys
from functools import partial 
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class UnrealToolWindow(QWidget):
    def __init__(self, parent = None):

        # Runt the Init of Qwidget <--- Parent
        super(UnrealToolWindow, self).__init__(parent)

        # Setting up the properties of my UnrealToolWindow
        self.main_window = QMainWindow()
        self.main_window.setParent(self)
        self.main_window.setFixedSize(QSize(400, 300))

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        # Create a Click Event that when the button is clicked it will call the function
        # ButtonClicked()
        self.button.clicked.connect(self.buttonClicked)

        self.main_window.setCentralWidget(self.button)
    
    def buttonClicked(self):
        pass


def launchWindow():
    if QApplication.instance():
        for win in (QApplication.allWindows()):
            if 'toolWindow' in win.objectName():
                win.destroy()
    else:
        app = QApplication(sys.argv)

    UnrealToolWindow.window = UnrealToolWindow()
    UnrealToolWindow.window.setObjectName("toolWindow")
    UnrealToolWindow.window.setWindowTitle("Tool Title")
    UnrealToolWindow.window.show()
    unreal.parent_external_window_to_slate(UnrealToolWindow.window.winId())

launchWindow()