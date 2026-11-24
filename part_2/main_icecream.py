import os
import sys
from pathlib import Path
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

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

        self.chart_fig = Figure()
        self.chart_ax = self.chart_fig.add_subplot(111)
        self.chart_canvas = FigureCanvasQTAgg(self.chart_fig)
        self.chart_canvas.setParent(self)
        self.chart_canvas.setGeometry(20, 110, 860, 580)

        self.chart_canvas = FigureCanvasQTAgg(self.chart_fig)
        self.chart_canvas.setParent(self)

        self.pick_file_btn = QPushButton("Open CSV", self)
        self.pick_file_btn.setGeometry(20, 20, 140, 35)
        self.pick_file_btn.clicked.connect(self.load_csv_file)

    def load_csv_file(self):
        selected_file, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)")
        if not selected_file:
            return
        self.x_val_temp = []
        self.y_val_profits = []

        with open(selected_file, "r", encoding="utf-8") as csv_file:
            rows = csv_file.readlines()
        for row in rows[1:]:
            columns = row.strip().split(",")
            if len(columns) >= 2:
                self.x_val_temp.append(float(columns[0]))
                self.y_val_profits.append(float(columns[1]))
        

if __name__ == "__main__":
    qt_app = QApplication(sys.argv)
    main_window = IceCreamAnalyzerWindow()
    main_window.show()
    sys.exit(qt_app.exec())
