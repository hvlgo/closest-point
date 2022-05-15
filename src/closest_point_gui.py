import sys
from PyQt5.QtWidgets import QApplication, QWidget
import Ui_untitled
import MyWidget

def main():
    app = QApplication(sys.argv)
    widget = MyWidget.MyWidget()
    ui = Ui_untitled.Ui_Form()
    ui.setupUi(widget)
    widget.show()

    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
