from src.core.CoreWindow import CoreWindow
from PyQt5 import QtWidgets



def run():
    elevate_db()
    app = QtWidgets.QApplication([])
    # TODO check for xml/yaml view configuration and pass as argument to CoreWindow which will take care of creation
    window = CoreWindow()
    window.show()
    app.exec()

# Checks if DB is present and correct version.
# If no db is available then create one.
# If db is not current version with current schema then migrate to new one
def elevate_db():
    pass
    # TODO