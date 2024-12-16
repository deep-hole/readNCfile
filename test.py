import sys
import os
from PySide6.QtWidgets import QWidget,QApplication,QMainWindow,QFileDialog,QVBoxLayout,QMessageBox
from PySide6.QtCore import Slot
from ui.Ui_test import Ui_MainWindow
from Scripts.readNC import readNC
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("牛逼NC读取器")
        self.initUI()
        
        
    
    def initUI(self):
        
        self.plot_index = 0
        self.plot_num = 0
        self.canvas = None
        
        self.Prev_plot.setVisible(False)
        self.Next_plot.setVisible(False)
        self.close_plot.setVisible(False)
        
        self.click_print.clicked.connect(self.readFile)
        self.vars_box.currentIndexChanged.connect(self.showVar)
        self.draw.clicked.connect(self.drawPlot)
        self.close_plot.clicked.connect(self.closePlot)
        self.Prev_plot.clicked.connect(self.prevPlot)
        self.Next_plot.clicked.connect(self.nextPlot)
        
    
    @Slot()
    def readFile(self):
        self.plot_index = 0
        self.plot_num = 0
        self.Prev_plot.setVisible(False)
        self.Next_plot.setVisible(False)
        self.close_plot.setVisible(False)
        if self.canvas:
            self.canvas.setVisible(False)
        self.fileProperties.setVisible(True)
        
        self.filename_line.clear()
        self.fileProperties.clear()
        # self.plot.clear()
        self.vars_box.clear()
        
        dialog = QFileDialog(self)
        filename = dialog.getOpenFileName(self, 
                                        "Open File",
                                        dir="/",
                                        filter="*.nc"
                                        )[0]
        self.filename_line.setPlaceholderText(filename)
        self.data = readNC(filename).data
        self.data_vars = [var for var in self.data.variables]
        self.vars_box.addItems(self.data_vars)
        
    
    @Slot()
    def showVar(self, var_index):
        # print(var)
        var = self.data_vars[var_index]
        if var_index != -1:
            data_details = ''
            var_detail = '\n '+ self.data_vars[var_index] + ': ' + str(self.data[var]) + ' \n'
            data_details += var_detail
            self.fileProperties.setText(data_details)

    @Slot()
    def drawPlot(self):
        cur_index = self.vars_box.currentIndex()
        self.fileProperties.setVisible(False)
        
        
        if cur_index != -1:
            if not self.plot.layout():
                self.layout = QVBoxLayout(self.plot)
            self.drawSeriesPlot(cur_index, self.plot_index)
        else:
            QMessageBox.warning(self, "警告", "请先选择变量")

    @Slot()
    def drawSeriesPlot(self,cur_index,plot_index):
        plt.close()
        
        var = self.data_vars[cur_index]
        fig = plt.figure(figsize=(self.plot.width()/100, self.plot.height()/100))
        self.canvas = FigureCanvasQTAgg(fig)
        if self.layout.count() > 0:
            self.layout.takeAt(0).widget().deleteLater()
        
        ax = fig.add_subplot(111)
        if self.data[var].ndim == 2:
            self.close_plot.setVisible(True)
            ax.clear()
            self.data[var].plot.contourf(ax=ax)
            fig.tight_layout()
            self.canvas.draw()
            self.layout.addWidget(self.canvas)
        elif self.data[var].ndim == 3:
            self.Prev_plot.setVisible(True)
            self.Next_plot.setVisible(True)
            self.close_plot.setVisible(True)
            self.plot_num = self.data[var].shape[0]
            ax.clear()
            self.data[var][plot_index].plot.contourf(ax=ax)
            fig.tight_layout()
            self.canvas.draw()
            self.layout.addWidget(self.canvas)
            
        else:
            QMessageBox.warning(self, "警告", "该变量维度超过2维或不是变量，无法绘制")
        
    
    @Slot()
    def closePlot(self):
        plt.close()
        self.plot_index = 0
        self.plot_num = 0
        self.canvas.setVisible(False)
        self.fileProperties.setVisible(True)
        self.close_plot.setVisible(False)
        self.Prev_plot.setVisible(False)
        self.Next_plot.setVisible(False)
    
    @Slot()
    def nextPlot(self):
        if self.plot_index < self.plot_num-1:
            self.plot_index += 1
            self.drawSeriesPlot(self.vars_box.currentIndex(), self.plot_index)
        else:
            QMessageBox.warning(self, "警告", "已经是最后一张图")
        # self.drawPlot()

    @Slot()
    def prevPlot(self):
        if self.plot_index>=1:
            self.plot_index -= 1
            self.drawSeriesPlot(self.vars_box.currentIndex(), self.plot_index)
        else:
            QMessageBox.warning(self, "警告", "已经是第一张图")
        # self.drawPlot()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec())
