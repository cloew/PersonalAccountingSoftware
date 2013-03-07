from db.database import Database
from Qt.GUI.main_window_controller import MainWindowController

def main():
    """ Generate the Database """
    controller = MainWindowController()
    controller.run()
    Database.clearSession()

if __name__ == "__main__":
    main()