import sys
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Robot import Robot

from gui import Ui_MainWindow
from about import Ui_Dialog as About_Ui_Dialog


import serial_port_finder as spf

import serial, time

from PyQt5.QtCore import QPointF, QRect, QRectF, Qt, QTimer
from PyQt5.QtGui import (QBrush, QColor, QFont, QLinearGradient, QPainter,
        QPen, QSurfaceFormat)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QOpenGLWidget,
        QWidget)


# import numpy as np
# from OpenGL import GL

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
# import pyqtgraph.opengl as gl

# import STLparser


s0 = serial.Serial()

############### SERIAL READ THREAD CLASS ###############
class SerialThreadClass(QtCore.QThread):
    elapsedTime = time.time()
    serialSignal = pyqtSignal(str)
    def __init__(self, parent=None):
         super(SerialThreadClass,self).__init__(parent)
    def run(self):
        while True:
            lastLineRead=""
            if s0.isOpen():
                try:
                    s0.inWaiting()
                except:
                    self.serialSignal.emit("SERIAL-DISCONNECTED")
                    print ("Lost Serial connection!")

                try:
                    if time.time()-self.elapsedTime>0.01:
                        self.elapsedTime=time.time()
                        s0.write("?\n".encode('UTF-8'))
                    # s0.write("?\n".encode('UTF-8'))
                    dataRead = str(s0.readline())
                    dataCropped=dataRead[2:][:-5]
                    if dataCropped!="" and lastLineRead!=dataCropped:
                        lastLineRead=dataCropped
                        self.serialSignal.emit(dataCropped)

                except Exception as e:
                    print ("Something failed: " + str(e))
###############  SERIAL READ THREAD CLASS ###############


class AboutDialog(About_Ui_Dialog):
    def __init__(self, dialog):
        About_Ui_Dialog.__init__(self)
        self.setupUi(dialog)


class AsgardGUI(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        self.getSerialPorts()

        self.SerialThreadClass = SerialThreadClass()
        self.SerialThreadClass.serialSignal.connect(self.updateConsole)

        self.Viewer3Dinit = False

        self.actionAbout.triggered.connect(self.launchAboutWindow)
        self.actionExit.triggered.connect(self.close_application)

        self.CollapseButtonConnection.clicked.connect(self.collapseConnectionMenu)
        self.CollapseButtonState.clicked.connect(self.collapseStateMenu)
        self.CollapseButtonQAB.clicked.connect(self.collapseQABMenu)

        self.HomeButton.pressed.connect(self.sendHomingCycleCommand)
        self.ZeroPositionButton.pressed.connect(self.sendZeroPositionCommand)
        self.KillAlarmLockButton.pressed.connect(self.TestIK)

        self.G0MoveRadioButton.clicked.connect(self.FeedRateBoxHide)
        self.G1MoveRadioButton.clicked.connect(self.FeedRateBoxHide)

        self.FKGoButtonArt1.pressed.connect(self.FKMoveArt1)
        self.FKSliderArt1.valueChanged.connect(self.FKSliderUpdateArt1)
        self.SpinBoxArt1.valueChanged.connect(self.FKSpinBoxUpdateArt1)
        self.FKDec10ButtonArt1.pressed.connect(self.FKDec10Art1)
        self.FKDec1ButtonArt1.pressed.connect(self.FKDec1Art1)
        self.FKDec0_1ButtonArt1.pressed.connect(self.FKDec0_1Art1)
        self.FKInc0_1ButtonArt1.pressed.connect(self.FKInc0_1Art1)
        self.FKInc1ButtonArt1.pressed.connect(self.FKInc1Art1)
        self.FKInc10ButtonArt1.pressed.connect(self.FKInc10Art1)

        self.FKGoButtonArt2.pressed.connect(self.FKMoveArt2)
        self.FKSliderArt2.valueChanged.connect(self.FKSliderUpdateArt2)
        self.SpinBoxArt2.valueChanged.connect(self.FKSpinBoxUpdateArt2)
        self.FKDec10ButtonArt2.pressed.connect(self.FKDec10Art2)
        self.FKDec1ButtonArt2.pressed.connect(self.FKDec1Art2)
        self.FKDec0_1ButtonArt2.pressed.connect(self.FKDec0_1Art2)
        self.FKInc0_1ButtonArt2.pressed.connect(self.FKInc0_1Art2)
        self.FKInc1ButtonArt2.pressed.connect(self.FKInc1Art2)
        self.FKInc10ButtonArt2.pressed.connect(self.FKInc10Art2)

        self.FKGoButtonArt3.pressed.connect(self.FKMoveArt3)
        self.FKSliderArt3.valueChanged.connect(self.FKSliderUpdateArt3)
        self.SpinBoxArt3.valueChanged.connect(self.FKSpinBoxUpdateArt3)
        self.FKDec10ButtonArt3.pressed.connect(self.FKDec10Art3)
        self.FKDec1ButtonArt3.pressed.connect(self.FKDec1Art3)
        self.FKDec0_1ButtonArt3.pressed.connect(self.FKDec0_1Art3)
        self.FKInc0_1ButtonArt3.pressed.connect(self.FKInc0_1Art3)
        self.FKInc1ButtonArt3.pressed.connect(self.FKInc1Art3)
        self.FKInc10ButtonArt3.pressed.connect(self.FKInc10Art3)

        self.FKGoButtonArt4.pressed.connect(self.FKMoveArt4)
        self.FKSliderArt4.valueChanged.connect(self.FKSliderUpdateArt4)
        self.SpinBoxArt4.valueChanged.connect(self.FKSpinBoxUpdateArt4)
        self.FKDec10ButtonArt4.pressed.connect(self.FKDec10Art4)
        self.FKDec1ButtonArt4.pressed.connect(self.FKDec1Art4)
        self.FKDec0_1ButtonArt4.pressed.connect(self.FKDec0_1Art4)
        self.FKInc0_1ButtonArt4.pressed.connect(self.FKInc0_1Art4)
        self.FKInc1ButtonArt4.pressed.connect(self.FKInc1Art4)
        self.FKInc10ButtonArt4.pressed.connect(self.FKInc10Art4)

        self.FKGoButtonArt5.pressed.connect(self.FKMoveArt5)
        self.FKSliderArt5.valueChanged.connect(self.FKSliderUpdateArt5)
        self.SpinBoxArt5.valueChanged.connect(self.FKSpinBoxUpdateArt5)
        self.FKDec10ButtonArt5.pressed.connect(self.FKDec10Art5)
        self.FKDec1ButtonArt5.pressed.connect(self.FKDec1Art5)
        self.FKDec0_1ButtonArt5.pressed.connect(self.FKDec0_1Art5)
        self.FKInc0_1ButtonArt5.pressed.connect(self.FKInc0_1Art5)
        self.FKInc1ButtonArt5.pressed.connect(self.FKInc1Art5)
        self.FKInc10ButtonArt5.pressed.connect(self.FKInc10Art5)

        self.FKGoButtonArt6.pressed.connect(self.FKMoveArt6)
        self.FKSliderArt6.valueChanged.connect(self.FKSliderUpdateArt6)
        self.SpinBoxArt6.valueChanged.connect(self.FKSpinBoxUpdateArt6)
        self.FKDec10ButtonArt6.pressed.connect(self.FKDec10Art6)
        self.FKDec1ButtonArt6.pressed.connect(self.FKDec1Art6)
        self.FKDec0_1ButtonArt6.pressed.connect(self.FKDec0_1Art6)
        self.FKInc0_1ButtonArt6.pressed.connect(self.FKInc0_1Art6)
        self.FKInc1ButtonArt6.pressed.connect(self.FKInc1Art6)
        self.FKInc10ButtonArt6.pressed.connect(self.FKInc10Art6)

        self.FKGoAllButton.pressed.connect(self.FKMoveAll)

        self.IKLocSliderX.valueChanged.connect(self.IKUpdate)
        self.IKInputLocSpinBoxX.valueChanged.connect(self.IKInputLocSpinBoxXUpdate)
        self.IKLocSliderY.valueChanged.connect(self.IKUpdate)
        self.IKInputLocSpinBoxY.valueChanged.connect(self.IKInputLocSpinBoxYUpdate)
        self.IKLocSliderZ.valueChanged.connect(self.IKUpdate)
        self.IKInputLocSpinBoxZ.valueChanged.connect(self.IKInputLocSpinBoxZUpdate)

        self.GoButtonGripper.pressed.connect(self.MoveGripper)
        self.SliderGripper.valueChanged.connect(self.SliderUpdateGripper)
        self.SpinBoxGripper.valueChanged.connect(self.SpinBoxUpdateGripper)
        self.Dec10ButtonGripper.pressed.connect(self.Dec10Gripper)
        self.Dec1ButtonGripper.pressed.connect(self.Dec1Gripper)
        self.Inc1ButtonGripper.pressed.connect(self.Inc1Gripper)
        self.Inc10ButtonGripper.pressed.connect(self.Inc10Gripper)

        self.SerialPortRefreshButton.pressed.connect(self.getSerialPorts)
        self.ConnectButton.pressed.connect(self.connectSerial)

        self.ConsoleButtonSend.pressed.connect(self.sendSerialCommand)
        self.ConsoleInput.returnPressed.connect(self.sendSerialCommand)

        self.TabWidget.currentChanged.connect(self.start3D)

        self.SettingsSaveCurrentButton.clicked.connect(self.saveCurrentSettings)
        self.SettingsShowCurrent.stateChanged.connect(self.settingsDisable3DCurrent)
        self.SettingsShowNext.stateChanged.connect(self.settingsDisable3DNext)
        self.SettingsSetColorButtonCurrent.pressed.connect(self.settingsUpdateColorCurrent)
        self.SettingsSetColorButtonNext.pressed.connect(self.settingsUpdateColorNext)
        self.SettingsApplyCurrentButton.pressed.connect(self.applyCurrentSettings)

        self.loadSettings("conf/saved_configuration.json")



    def close_application(self):
        sys.exit()

    def launchAboutWindow(self):
        self.dialogAbout = QtWidgets.QDialog()
        self.ui = AboutDialog(self.dialogAbout)
        self.dialogAbout.exec_()

    def collapseConnectionMenu(self):
        if self.ConnectionMenuBot.isHidden():
            self.ConnectionMenuBot.show()
            self.CollapseButtonConnection.setText("▼")
        else:
            self.ConnectionMenuBot.hide()
            self.CollapseButtonConnection.setText("▶")

    def collapseStateMenu(self):
        if self.StateMenuBot.isHidden():
            self.StateMenuBot.show()
            self.CollapseButtonState.setText("▼")
        else:
            self.StateMenuBot.hide()
            self.CollapseButtonState.setText("▶")

    def collapseQABMenu(self):
        if self.QABMenuBot.isHidden():
            self.QABMenuBot.show()
            self.CollapseButtonQAB.setText("▼")
        else:
            self.QABMenuBot.hide()
            self.CollapseButtonQAB.setText("▶")

    def sendHomingCycleCommand(self):
        if s0.isOpen():
            messageToSend="$H"
            messageToConsole=">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def sendZeroPositionCommand(self):
        if s0.isOpen():
            messageToSend="G0 A0 B0 C0 D0 X0 Y0 Z0"
            messageToConsole=">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def sendKillAlarmCommand(self):
        if s0.isOpen():
            messageToSend="$X"
            messageToConsole=">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def FeedRateBoxHide(self):
        if self.G1MoveRadioButton.isChecked():
            self.FeedRateLabel.setEnabled(True)
            self.FeedRateInput.setEnabled(True)
        else:
            self.FeedRateLabel.setEnabled(False)
            self.FeedRateInput.setEnabled(False)


#FK Art1 Functions
    def FKMoveArt1(self):
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "A" + str(self.SpinBoxArt1.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt1(self):
        val=self.FKSliderArt1.value()/10
        self.SpinBoxArt1.setValue(val)
    def FKSpinBoxUpdateArt1(self):
        val=int(self.SpinBoxArt1.value()*10)
        self.FKSliderArt1.setValue(val)
        self.moveNext3D()
    def FKDec10Art1(self):
        val=self.SpinBoxArt1.value()-10
        self.SpinBoxArt1.setValue(val)
    def FKDec1Art1(self):
        val=self.SpinBoxArt1.value()-1
        self.SpinBoxArt1.setValue(val)
    def FKDec0_1Art1(self):
        val=self.SpinBoxArt1.value()-0.1
        self.SpinBoxArt1.setValue(val)
    def FKInc0_1Art1(self):
        val=self.SpinBoxArt1.value()+0.1
        self.SpinBoxArt1.setValue(val)
    def FKInc1Art1(self):
        val=self.SpinBoxArt1.value()+1
        self.SpinBoxArt1.setValue(val)
    def FKInc10Art1(self):
        val=self.SpinBoxArt1.value()+10
        self.SpinBoxArt1.setValue(val)

#FK Art2 Functions
    def FKMoveArt2(self):
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "B" + str(self.SpinBoxArt2.value()) + " C" + str(self.SpinBoxArt2.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt2(self):
        val=self.FKSliderArt2.value()/10
        self.SpinBoxArt2.setValue(val)
    def FKSpinBoxUpdateArt2(self):
        val=int(self.SpinBoxArt2.value()*10)
        self.FKSliderArt2.setValue(val)
        self.moveNext3D()
    def FKDec10Art2(self):
        val=self.SpinBoxArt2.value()-10
        self.SpinBoxArt2.setValue(val)
    def FKDec1Art2(self):
        val=self.SpinBoxArt2.value()-1
        self.SpinBoxArt2.setValue(val)
    def FKDec0_1Art2(self):
        val=self.SpinBoxArt2.value()-0.1
        self.SpinBoxArt2.setValue(val)
    def FKInc0_1Art2(self):
        val=self.SpinBoxArt2.value()+0.1
        self.SpinBoxArt2.setValue(val)
    def FKInc1Art2(self):
        val=self.SpinBoxArt2.value()+1
        self.SpinBoxArt2.setValue(val)
    def FKInc10Art2(self):
        val=self.SpinBoxArt2.value()+10
        self.SpinBoxArt2.setValue(val)

#FK Art3 Functions
    def FKMoveArt3(self):
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "D" + str(self.SpinBoxArt3.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt3(self):
        val=self.FKSliderArt3.value()/10
        self.SpinBoxArt3.setValue(val)
    def FKSpinBoxUpdateArt3(self):
        val=int(self.SpinBoxArt3.value()*10)
        self.FKSliderArt3.setValue(val)
        self.moveNext3D()
    def FKDec10Art3(self):
        val=self.SpinBoxArt3.value()-10
        self.SpinBoxArt3.setValue(val)
    def FKDec1Art3(self):
        val=self.SpinBoxArt3.value()-1
        self.SpinBoxArt3.setValue(val)
    def FKDec0_1Art3(self):
        val=self.SpinBoxArt3.value()-0.1
        self.SpinBoxArt3.setValue(val)
    def FKInc0_1Art3(self):
        val=self.SpinBoxArt3.value()+0.1
        self.SpinBoxArt3.setValue(val)
    def FKInc1Art3(self):
        val=self.SpinBoxArt3.value()+1
        self.SpinBoxArt3.setValue(val)
    def FKInc10Art3(self):
        val=self.SpinBoxArt3.value()+10
        self.SpinBoxArt3.setValue(val)

#FK Art4 Functions
    def FKMoveArt4(self):
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "X" + str(self.SpinBoxArt4.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt4(self):
        val=self.FKSliderArt4.value()/10
        self.SpinBoxArt4.setValue(val)
    def FKSpinBoxUpdateArt4(self):
        val=int(self.SpinBoxArt4.value()*10)
        self.FKSliderArt4.setValue(val)
        self.moveNext3D()
    def FKDec10Art4(self):
        val=self.SpinBoxArt4.value()-10
        self.SpinBoxArt4.setValue(val)
    def FKDec1Art4(self):
        val=self.SpinBoxArt4.value()-1
        self.SpinBoxArt4.setValue(val)
    def FKDec0_1Art4(self):
        val=self.SpinBoxArt4.value()-0.1
        self.SpinBoxArt4.setValue(val)
    def FKInc0_1Art4(self):
        val=self.SpinBoxArt4.value()+0.1
        self.SpinBoxArt4.setValue(val)
    def FKInc1Art4(self):
        val=self.SpinBoxArt4.value()+1
        self.SpinBoxArt4.setValue(val)
    def FKInc10Art4(self):
        val=self.SpinBoxArt4.value()+10
        self.SpinBoxArt4.setValue(val)

#FK Art5 Functions
    def FKMoveArt5(self): # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "Y" + str(self.SpinBoxArt5.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt5(self):
        val=self.FKSliderArt5.value()/10
        self.SpinBoxArt5.setValue(val)
    def FKSpinBoxUpdateArt5(self):
        val=int(self.SpinBoxArt5.value()*10)
        self.FKSliderArt5.setValue(val)
        self.moveNext3D()
    def FKDec10Art5(self):
        val=self.SpinBoxArt5.value()-10
        self.SpinBoxArt5.setValue(val)
    def FKDec1Art5(self):
        val=self.SpinBoxArt5.value()-1
        self.SpinBoxArt5.setValue(val)
    def FKDec0_1Art5(self):
        val=self.SpinBoxArt5.value()-0.1
        self.SpinBoxArt5.setValue(val)
    def FKInc0_1Art5(self):
        val=self.SpinBoxArt5.value()+0.1
        self.SpinBoxArt5.setValue(val)
    def FKInc1Art5(self):
        val=self.SpinBoxArt5.value()+1
        self.SpinBoxArt5.setValue(val)
    def FKInc10Art5(self):
        val=self.SpinBoxArt5.value()+10
        self.SpinBoxArt5.setValue(val)

#FK Art6 Functions
    def FKMoveArt6(self): # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "Z" + str(self.SpinBoxArt6.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()
    def FKSliderUpdateArt6(self):
        val=self.FKSliderArt6.value()/10
        self.SpinBoxArt6.setValue(val)
    def FKSpinBoxUpdateArt6(self):
        val=int(self.SpinBoxArt6.value()*10)
        self.FKSliderArt6.setValue(val)
        self.moveNext3D()
    def FKDec10Art6(self):
        val=self.SpinBoxArt6.value()-10
        self.SpinBoxArt6.setValue(val)
    def FKDec1Art6(self):
        val=self.SpinBoxArt6.value()-1
        self.SpinBoxArt6.setValue(val)
    def FKDec0_1Art6(self):
        val=self.SpinBoxArt6.value()-0.1
        self.SpinBoxArt6.setValue(val)
    def FKInc0_1Art6(self):
        val=self.SpinBoxArt6.value()+0.1
        self.SpinBoxArt6.setValue(val)
    def FKInc1Art6(self):
        val=self.SpinBoxArt6.value()+1
        self.SpinBoxArt6.setValue(val)
    def FKInc10Art6(self):
        val=self.SpinBoxArt6.value()+10
        self.SpinBoxArt6.setValue(val)

#FK Every Articulation Functions
    def FKMoveAll(self): # En realidad esto no va así, hay que calcular el movimiento acoplado de los dos ultimos grados de libertad. Proximamente.
        if s0.isOpen():
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement="G1 "
                feedRate=" F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement="G0 "
                feedRate=""
            message=typeOfMovement + "A" + str(self.SpinBoxArt1.value()) + " B" + str(self.SpinBoxArt2.value()) + " C" + str(self.SpinBoxArt2.value()) + " D" + str(self.SpinBoxArt3.value()) + " X" + str(self.SpinBoxArt4.value()) + " Y" + str(self.SpinBoxArt5.value()) + " Z" + str(self.SpinBoxArt6.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

# IK Functions
    def IKInputLocSpinBoxXUpdate(self):
        self.IKLocSliderX.setValue(self.IKInputLocSpinBoxX.value())
    def IKInputLocSpinBoxYUpdate(self):
        self.IKLocSliderY.setValue(self.IKInputLocSpinBoxY.value())
    def IKInputLocSpinBoxZUpdate(self):
        self.IKLocSliderZ.setValue(self.IKInputLocSpinBoxZ.value())

    def IKUpdate(self):
        IKX=self.IKLocSliderX.value()
        IKY=self.IKLocSliderY.value()
        IKZ=self.IKLocSliderZ.value()
        self.IKInputLocSpinBoxX.setValue(IKX)
        self.IKInputLocSpinBoxY.setValue(IKY)
        self.IKInputLocSpinBoxZ.setValue(IKZ)

        if self.Viewer3Dinit:
            EOATpos=[IKX,IKY,IKZ]
            print(EOATpos)
            self.thor3d.moveEOAT(EOATpos)

    def TestIK(self):
        #self.sendKillAlarmCommand es la buena

        noaMatrix=[
            [1,0,0],
            [0,0,1],
            [0,1,0]
        ]
        # EOATpos=[0,422.15,202]
        EOATpos=[self.IKLocSliderX.value(),self.IKLocSliderY.value(),self.IKLocSliderZ.value()]
        orientationAngles=[self.IKInputAngleSpinBoxX.value(),self.IKInputAngleSpinBoxY.value(),self.IKInputAngleSpinBoxZ.value()]
        self.thor3d.IK(EOATpos, orientationAngles)



# Gripper Functions
    def MoveGripper(self): # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
        if s0.isOpen():
            message="M3 S" + str((255/100)*self.SpinBoxGripper.value())
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def SliderUpdateGripper(self):
        val=self.SliderGripper.value()
        self.SpinBoxGripper.setValue(val)
    def SpinBoxUpdateGripper(self):
        val=int(self.SpinBoxGripper.value())
        self.SliderGripper.setValue(val)
    def Dec10Gripper(self):
        val=self.SpinBoxGripper.value()-10
        self.SpinBoxGripper.setValue(val)
    def Dec1Gripper(self):
        val=self.SpinBoxGripper.value()-1
        self.SpinBoxGripper.setValue(val)
    def Inc1Gripper(self):
        val=self.SpinBoxGripper.value()+1
        self.SpinBoxGripper.setValue(val)
    def Inc10Gripper(self):
        val=self.SpinBoxGripper.value()+10
        self.SpinBoxGripper.setValue(val)

# Serial Connection functions
    def getSerialPorts(self):
        self.SerialPortComboBox.clear()
        self.SerialPortComboBox.addItems(spf.serial_ports())

    def connectSerial(self):
        serialPort = self.SerialPortComboBox.currentText()
        baudrate = self.BaudRateComboBox.currentText()
        if serialPort != "":
            if baudrate!="":
                s0.port = serialPort
                s0.baudrate = baudrate
                s0.timeout = 1
                try:
                    s0.close()
                    s0.open()
                    self.SerialThreadClass.start()
                except Exception as e:
                    print ("error opening serial port: " + str(e))
            else:
                self.blankBaudRate()
        else:
            self.blankSerialPort()

    def serialDisconnected(self):
        self.RobotStateDisplay.setStyleSheet('background-color: rgb(255, 0, 0)')
        self.RobotStateDisplay.setText("Disconnected")

    def updateConsole(self, dataRead):
        verboseShow=self.ConsoleShowVerbosecheckBox.isChecked()
        okShow=self.ConsoleShowOkRespcheckBox.isChecked()
        isDataReadVerbose = "MPos" in dataRead
        isDataOkResponse = "ok" in dataRead

        if dataRead=="SERIAL-DISCONNECTED":
            s0.close()
            self.serialDisconnected()
            print ("Serial Connection Lost")

        else:
            if not isDataReadVerbose and not isDataOkResponse:
                self.ConsoleOutput.appendPlainText(dataRead)
            elif isDataOkResponse and okShow:
                self.ConsoleOutput.appendPlainText(dataRead)
            elif isDataReadVerbose:
                self.updateFKPosDisplay(dataRead)
                if verboseShow:
                    self.ConsoleOutput.appendPlainText(dataRead)

    def sendSerialCommand(self):
        messageToSent=self.ConsoleInput.text()+"\n"
        messageToConsole= ">>> "+self.ConsoleInput.text()
        if s0.isOpen():
            if messageToSent!="":
                s0.write(messageToSent.encode('UTF-8'))
                self.ConsoleOutput.appendPlainText(messageToConsole)
                self.ConsoleInput.clear()
        else:
            self.noSerialConnection()

    def updateFKPosDisplay(self,dataRead):
        data=dataRead[1:][:-1].split(",")
        self.updateCurrentState(data[0])
        a1=data[1][5:][:-2]
        a2=data[2][:-2]
        a3=data[4][:-2]
        a4=data[5][:-2]
        a5=data[6][:-2]
        a6=data[7][:-2]
        self.FKCurrentPosValueArt1.setText(a1+"º")
        self.FKCurrentPosValueArt2.setText(a2+"º")
        self.FKCurrentPosValueArt3.setText(a3+"º")
        self.FKCurrentPosValueArt4.setText(a4+"º")
        self.FKCurrentPosValueArt5.setText(a5+"º")
        self.FKCurrentPosValueArt6.setText(a6+"º")

        if self.Viewer3Dinit:
            self.thor3d.rotateCurrentArm(float(a1),float(a2),float(a3),float(a4),float(a5),float(a6))

    def updateCurrentState(self, state):
        self.RobotStateDisplay.setText(state)
        if state=="Idle" or state=="Run":
            self.RobotStateDisplay.setStyleSheet('background-color: rgb(0, 255, 0)')
        elif state=="Home":
            self.RobotStateDisplay.setStyleSheet('background-color: rgb(85, 255, 255)')
        elif state=="Alarm":
            self.RobotStateDisplay.setStyleSheet('background-color: rgb(255, 255, 0)')
        elif state=="Hold":
            self.RobotStateDisplay.setStyleSheet('background-color: rgb(255, 0, 0)')
        else:
            self.RobotStateDisplay.setStyleSheet('background-color: rgb(255, 255, 255)')


    def blankSerialPort(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("There is not Serial Port value indicated to establish the connection.\nPlease check it and try to connect again.")
        msgBox.exec_()

    def blankBaudRate(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("There is not Baud Rate value indicated to establish the connection.\nPlease check it and try to connect again.")
        msgBox.exec_()

    def noSerialConnection(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setText("The connection has not been established yet. Please establish the connection before trying to control.")
        msgBox.exec_()

########## 3D ##############

    def start3D(self):
        if self.TabWidget.currentIndex()==1 and self.Viewer3Dinit==False:
            self.thor3d=Robot(self.SettingsShowCurrent.isChecked(), self.SettingsShowNext.isChecked(), self.CurrentColor, self.NextColor)
            self.gridLayout_5.addWidget(self.thor3d.w,0,0)
            self.Viewer3Dinit=True

    def moveNext3D(self):
        a1=self.SpinBoxArt1.value()
        a2=self.SpinBoxArt2.value()
        a3=self.SpinBoxArt3.value()
        a4=self.SpinBoxArt4.value()
        a5=self.SpinBoxArt5.value()
        a6=self.SpinBoxArt6.value()
        self.thor3d.rotateNextArm(a1,a2,a3,a4,a5,a6)


### settings


    def loadSettings(self, path):
        with open(path, "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()


        self.CurrentColor=QColor(data["3dviewer"]["currentmodel"]["color"]["r"],data["3dviewer"]["currentmodel"]["color"]["g"],data["3dviewer"]["currentmodel"]["color"]["b"],int(data["3dviewer"]["currentmodel"]["opacity"]*2.55))
        self.SettingsSetOpacityCurrent.setValue(data["3dviewer"]["currentmodel"]["opacity"])
        self.SettingsColorPreviewCurrent.setStyleSheet('background-color: rgba' + str(self.CurrentColor.getRgb()))
        self.SettingsShowCurrent.setChecked(data["3dviewer"]["currentmodel"]["show"])

        self.NextColor=QColor(data["3dviewer"]["nextmodel"]["color"]["r"],data["3dviewer"]["nextmodel"]["color"]["g"],data["3dviewer"]["nextmodel"]["color"]["b"],int(data["3dviewer"]["nextmodel"]["opacity"]*2.55))
        self.SettingsSetOpacityNext.setValue(data["3dviewer"]["nextmodel"]["opacity"])
        self.SettingsColorPreviewNext.setStyleSheet('background-color: rgba' + str(self.NextColor.getRgb()))
        self.SettingsShowNext.setChecked(data["3dviewer"]["nextmodel"]["show"])


    def saveCurrentSettings(self):
        with open("conf/saved_configuration.json", "r") as jsonFile:
                temp = json.load(jsonFile)
                jsonFile.close()

        temp["3dviewer"]["currentmodel"]["color"]["r"]=self.CurrentColor.red()
        temp["3dviewer"]["currentmodel"]["color"]["g"]=self.CurrentColor.green()
        temp["3dviewer"]["currentmodel"]["color"]["b"]=self.CurrentColor.blue()
        temp["3dviewer"]["currentmodel"]["opacity"]=self.SettingsSetOpacityCurrent.value()
        temp["3dviewer"]["currentmodel"]["show"]=self.SettingsShowCurrent.isChecked()
        temp["3dviewer"]["nextmodel"]["color"]["r"]=self.NextColor.red()
        temp["3dviewer"]["nextmodel"]["color"]["g"]=self.NextColor.green()
        temp["3dviewer"]["nextmodel"]["color"]["b"]=self.NextColor.blue()
        temp["3dviewer"]["nextmodel"]["opacity"]=self.SettingsSetOpacityNext.value()
        temp["3dviewer"]["nextmodel"]["show"]=self.SettingsShowNext.isChecked()

        with open("conf/saved_configuration.json", "w") as jsonFile:
            json.dump(temp, jsonFile)
            jsonFile.close()




    def applyCurrentSettings(self):
        if self.Viewer3Dinit:
            self.CurrentColor.setAlpha(int(self.SettingsSetOpacityCurrent.value()*2.55))
            self.NextColor.setAlpha(int(self.SettingsSetOpacityNext.value()*2.55))
            self.thor3d.setColorCurrent(self.CurrentColor)
            self.thor3d.setColorNext(self.NextColor)
            self.thor3d.showModels(self.SettingsShowCurrent.isChecked(),self.SettingsShowNext.isChecked())

    def settingsDisable3DCurrent(self):
        if self.SettingsShowCurrent.isChecked():
            self.SettingsColorLabelCurrent.setEnabled(True)
            self.SettingsColorPreviewCurrent.setEnabled(True)
            self.SettingsSetColorButtonCurrent.setEnabled(True)
            self.SettingsOpacityLabelCurrent.setEnabled(True)
            self.SettingsSetOpacityCurrent.setEnabled(True)
        else:
            self.SettingsColorLabelCurrent.setEnabled(False)
            self.SettingsColorPreviewCurrent.setEnabled(False)
            self.SettingsSetColorButtonCurrent.setEnabled(False)
            self.SettingsOpacityLabelCurrent.setEnabled(False)
            self.SettingsSetOpacityCurrent.setEnabled(False)

    def settingsDisable3DNext(self):
        if self.SettingsShowNext.isChecked():
            self.SettingsColorLabelNext.setEnabled(True)
            self.SettingsColorPreviewNext.setEnabled(True)
            self.SettingsSetColorButtonNext.setEnabled(True)
            self.SettingsOpacityLabelNext.setEnabled(True)
            self.SettingsSetOpacityNext.setEnabled(True)
        else:
            self.SettingsColorLabelNext.setEnabled(False)
            self.SettingsColorPreviewNext.setEnabled(False)
            self.SettingsSetColorButtonNext.setEnabled(False)
            self.SettingsOpacityLabelNext.setEnabled(False)
            self.SettingsSetOpacityNext.setEnabled(False)

    def settingsUpdateColorCurrent(self):
        self.CurrentColor = QtWidgets.QColorDialog.getColor(self.CurrentColor)
        self.SettingsColorPreviewCurrent.setStyleSheet('background-color: rgba' + str(self.CurrentColor.getRgb()))

    def settingsUpdateColorNext(self):
        self.NextColor = QtWidgets.QColorDialog.getColor(self.NextColor)
        self.SettingsColorPreviewNext.setStyleSheet('background-color: rgba' + str(self.NextColor.getRgb()))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    mwindow = QtWidgets.QMainWindow()

    prog = AsgardGUI(mwindow)

    mwindow.show()
    sys.exit(app.exec_())
