import os
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QMainWindow

if sys.platform == "darwin":
    qt_platform_plugins = (Path(__file__).resolve().parent.parent.parent / "qtplugins" / "platforms")
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)
class IceCreamAnalyzerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Sales Profit Analysis")
        self.resize(920, 720)


        self.x_val_temp =[]
        self.y_val_profits =[]
    
    
        self.pick_file_btn = QPushButton("Open CSV", self)
        self.pick_file_btn.setGeometry(20, 20, 140, 35)
        self.pick_file_btn.clicked.connect(self.load_csv_file)
    
            
    
        

if __name__ == "__main__":
    qt_app = QApplication(sys.argv)
    main_window = IceCreamAnalyzerWindow()
    main_window.show()
    sys.exit(qt_app.exec())
