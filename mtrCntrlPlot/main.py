import serial
import struct
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

ser = serial.Serial('COM3', 9600)

app = QtGui.QApplication([])

p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
p.setRange(QtCore.QRectF(0, -10, 5000, 20))
p.setLabel('bottom', 'Index', units='B')
curve = p.plot()


while True:
    temp = ser.readline()
    print(temp)
    if temp.decode("utf-8") == "Datas\r\n":
        print(temp)
        print("Got the code, printing data")
        while True:
            in_bin = ser.readline().strip()
            data = struct.unpack('hhf', in_bin)


