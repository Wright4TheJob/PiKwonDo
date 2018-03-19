#!/bin/env/python
# David Wright
# Copyright 2017
# Written for Python 3.5.2


#Import
import sys
from PyQt5.QtWidgets import (QWidget, QTreeView, QMessageBox, QHBoxLayout,
							 QFileDialog, QLabel, QSlider, QCheckBox,
							 QLineEdit, QVBoxLayout, QApplication, QPushButton,
							 QTableWidget, QTableWidgetItem,QSizePolicy,
							 QGridLayout,QGroupBox, QMainWindow,QAction)
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QThread
from PyQt5 import QtCore, QtGui
import MainUI
from scipy import stats
from sympy import *
import numpy as np
import os
import cmath
import math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.mlab as mlab
import csv


class MainWindow(QMainWindow, MainUI.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		#self.startButton.clicked.connect(self.startOptimization)
		# Initialize variables

		self.programLoaded = True

	def load_data(self):
		#Write this function
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,
			"QFileDialog.getOpenFileName()",
			"","All Files (*);;Text Files (*.txt)",
			options=options)
		if fileName:
			self.initialNodeArray = []
			self.initialBeamArray = []
			with open(fileName, 'r') as fin:
				reader = csv.reader(fin, delimiter=',')
				for line in reader:
					#print(line)
					if len(line) == 8:
						self.initialNodeArray.append([float(line[0]),float(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),float(line[6]),float(line[7])])
					elif len(line) == 5:
						self.initialBeamArray.append([int(line[0]),int(line[1]),float(line[2]),float(line[3]),float(line[4])])
					else:
						print('Unexpected line length')
			self.redrawInputTables()
			self.graph_canvas.plotTruss(self.initialNodeArray,self.initialBeamArray)

	#def saveRoundData(self):
		# Save out the point totals and times


	def redrawUI(self):
		# Beam Table
		pass


def main():
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
