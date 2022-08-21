import sys
from PyQt5 import QtWidgets
from View.InterfaceLogin import InterfaceLogin


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    interface_login = InterfaceLogin()
    interface_login.show()

    sys.exit(app.exec_())
