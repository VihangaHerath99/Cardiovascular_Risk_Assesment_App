import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import winsound

class RealTimeBloodPressure(QtWidgets.QMainWindow):
    averageValueUpdated = QtCore.pyqtSignal(float)
    
    def __init__(self, *args, **kwargs):
        super(RealTimeBloodPressure, self).__init__(*args, **kwargs)

        self.setWindowTitle("Blood Pressure Meter")
        
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        
        self.x = np.arange(100)
        self.y = np.full(100, 150)
        
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pg.mkPen('r', width=1), name='data_line')

        # Average line and text item for displaying average value
        self.avg_line = pg.InfiniteLine(angle=0, pen=pg.mkPen('g', style=QtCore.Qt.DashLine))
        self.graphWidget.addItem(self.avg_line)
        self.avg_text = pg.TextItem(anchor=(1, 1))
        self.graphWidget.addItem(self.avg_text)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)  # 500 ms update interval
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.graphWidget.setLabel('left', 'Blood Pressure (mmHg)')
        self.graphWidget.setLabel('bottom', 'Time (s)')
        self.graphWidget.showGrid(x=True, y=True)
        
    def update_plot_data(self):
        self.y = np.roll(self.y, -1)
        self.y[-1] = np.random.normal(loc=160, scale=40)
        
        self.data_line.setData(self.x, self.y)

        # Calculate the average and update the average line and text
        avg_value = np.mean(self.y)
        self.avg_line.setPos(avg_value)
        self.avg_text.setText(f'Avg: {avg_value:.2f} mmHg')
        self.avg_text.setPos(99, avg_value)  # Position the text at the end of the plot

        # emit the averageValueUpdated signal
        self.averageValueUpdated.emit(avg_value)

        # Frequency: 1000 Hz, Duration: 100 ms
        winsound.Beep(1000, 100) 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = RealTimeBloodPressure()
    window.show()
    sys.exit(app.exec_())