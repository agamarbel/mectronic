import os
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow

if sys.platform == "darwin":
    qt_platform_plugins = (Path(__file__).resolve().parent.parent.parent / "qtplugins" / "platforms")
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)
class IceCreamAnalyzerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ice Cream Sales Profit Analysis")
        self.resize(920, 720)



if __name__ == "__main__":
    qt_app = QApplication(sys.argv)
    main_window = IceCreamAnalyzerWindow()
    main_window.show()
    sys.exit(qt_app.exec())
