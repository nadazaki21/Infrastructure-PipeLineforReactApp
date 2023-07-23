import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QTimer
import sys 

class ChartDockWidget(QDockWidget):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.x = 0  # Start from 0
        self.series = QLineSeries(self)
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(title)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.setWidget(self.chartview)


        self.timer = QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000)

    def updateData(self):
        self.x += 1
        # Simulated data generation based on mean and standard deviation
        bp_value = random.gauss(120, 10)  # Blood pressure values
        sugar_value = random.gauss(85, 15)  # Sugar index values
        heart_rate_value = random.gauss(80, 15)  # Heart rate values
        oxygen_value = random.gauss(98, 2)  # Oxygen in blood values

        # Append the simulated values to the series
        self.series.append(self.x, heart_rate_value)
        self.chart.axisX().setRange(0, self.x)
        self.chart.axisX().setTickCount(self.x + 1)  # Increase tick count to include 0
        self.chart.axisX().setLabelFormat("%d")
        self.chart.axisY().setRange(0, max([point.y() for point in self.series.pointsVector()]))


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Line")
        self.setGeometry(100, 100, 1000, 700)

        self.show()

        self.dock1 = ChartDockWidget("Blood Pressure", self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)

        self.dock2 = ChartDockWidget("Sugar Index", self)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock2)

        self.dock3 = ChartDockWidget("Heart Rate", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock3)

        self.dock4 = ChartDockWidget("Oxygen in Blood ", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock4)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
