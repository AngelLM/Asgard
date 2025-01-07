"""
    File: asgard.py
    Description: Main application code for the Thor Asgard GUI.
"""
import sys
import os

# pip install PyQt6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import *
from PySide6.QtCore import *

# Save settings from preferences dialog
import configparser

from gui import Ui_MainWindow
from about import Ui_Dialog as About_Ui_Dialog
from preferences_dialog import PreferencesDialog

# Import the application icons
from img.thor_icon import icon_32, icon_16

import serial_port_finder as spf
from serial_read_thread_class import SerialThreadClass

# pip install pyserial
import serial

# Create a serial object
s0 = serial.Serial()


class AsgardGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Call the QMainWindow __init__ method
        super(AsgardGUI, self).__init__()

        # Call the Ui_MainWindow setupUi method to create the GUI
        self.setupUi(self)

        # Set the icon of the application
        self.setIcon()

        # Load settings from settings.ini file
        self.loadSettings()

        # Get the available serial ports
        self.getSerialPorts()

        self.SerialThreadClass = SerialThreadClass(s0)

        # Connect methods to the GUI elements
        self.connect_methods()

 # -------------------------- CONNECT METHODS ------------------------------ #
    def connect_methods(self):
        """Connect methods to GUI elements."""
        self.SerialThreadClass.serialSignal.connect(self.updateConsole)

        # Menu bar actions
        self.actionAbout.triggered.connect(self.launchAboutWindow)
        self.actionPreferences.triggered.connect(self.launchPreferencesWindow)
        self.actionExit.triggered.connect(self.close_application)

        self.HomeButton.pressed.connect(self.sendHomingCycleCommand)
        self.ZeroPositionButton.pressed.connect(self.sendZeroPositionCommand)
        self.KillAlarmLockButton.pressed.connect(self.sendKillAlarmCommand)

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

    def close_application(self):
        sys.exit()

    def launchAboutWindow(self):
        self.dialogAbout = QtWidgets.QDialog()
        self.ui = AboutDialog(self.dialogAbout)
        self.dialogAbout.exec()

    def sendHomingCycleCommand(self):
        if s0.is_open:
            messageToSend = "$H"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def sendZeroPositionCommand(self):
        if s0.is_open:
            messageToSend = "G0 A0 B0 C0 D0 X0 Y0 Z0"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def sendKillAlarmCommand(self):
        if s0.is_open:
            messageToSend = "$X"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)

    def FeedRateBoxHide(self):
        if self.G1MoveRadioButton.isChecked():
            self.FeedRateLabel.setEnabled(True)
            self.FeedRateInput.setEnabled(True)
        else:
            self.FeedRateLabel.setEnabled(False)
            self.FeedRateInput.setEnabled(False)

    # FK Art1 Functions
    def FKMoveArt1(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = typeOfMovement + "A" + \
                str(self.SpinBoxArt1.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt1(self):
        val = self.FKSliderArt1.value() / 10
        self.SpinBoxArt1.setValue(val)

    def FKSpinBoxUpdateArt1(self):
        val = int(self.SpinBoxArt1.value() * 10)
        self.FKSliderArt1.setValue(val)

    def FKDec10Art1(self):
        val = self.SpinBoxArt1.value() - 10
        self.SpinBoxArt1.setValue(val)

    def FKDec1Art1(self):
        val = self.SpinBoxArt1.value() - 1
        self.SpinBoxArt1.setValue(val)

    def FKDec0_1Art1(self):
        val = self.SpinBoxArt1.value() - 0.1
        self.SpinBoxArt1.setValue(val)

    def FKInc0_1Art1(self):
        val = self.SpinBoxArt1.value() + 0.1
        self.SpinBoxArt1.setValue(val)

    def FKInc1Art1(self):
        val = self.SpinBoxArt1.value() + 1
        self.SpinBoxArt1.setValue(val)

    def FKInc10Art1(self):
        val = self.SpinBoxArt1.value() + 10
        self.SpinBoxArt1.setValue(val)

    # FK Art2 Functions
    def FKMoveArt2(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = (
                typeOfMovement
                + "B"
                + str(self.SpinBoxArt2.value())
                + " C"
                + str(self.SpinBoxArt2.value())
                + feedRate
            )
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt2(self):
        val = self.FKSliderArt2.value() / 10
        self.SpinBoxArt2.setValue(val)

    def FKSpinBoxUpdateArt2(self):
        val = int(self.SpinBoxArt2.value() * 10)
        self.FKSliderArt2.setValue(val)

    def FKDec10Art2(self):
        val = self.SpinBoxArt2.value() - 10
        self.SpinBoxArt2.setValue(val)

    def FKDec1Art2(self):
        val = self.SpinBoxArt2.value() - 1
        self.SpinBoxArt2.setValue(val)

    def FKDec0_1Art2(self):
        val = self.SpinBoxArt2.value() - 0.1
        self.SpinBoxArt2.setValue(val)

    def FKInc0_1Art2(self):
        val = self.SpinBoxArt2.value() + 0.1
        self.SpinBoxArt2.setValue(val)

    def FKInc1Art2(self):
        val = self.SpinBoxArt2.value() + 1
        self.SpinBoxArt2.setValue(val)

    def FKInc10Art2(self):
        val = self.SpinBoxArt2.value() + 10
        self.SpinBoxArt2.setValue(val)

    # FK Art3 Functions
    def FKMoveArt3(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = typeOfMovement + "D" + \
                str(self.SpinBoxArt3.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt3(self):
        val = self.FKSliderArt3.value() / 10
        self.SpinBoxArt3.setValue(val)

    def FKSpinBoxUpdateArt3(self):
        val = int(self.SpinBoxArt3.value() * 10)
        self.FKSliderArt3.setValue(val)

    def FKDec10Art3(self):
        val = self.SpinBoxArt3.value() - 10
        self.SpinBoxArt3.setValue(val)

    def FKDec1Art3(self):
        val = self.SpinBoxArt3.value() - 1
        self.SpinBoxArt3.setValue(val)

    def FKDec0_1Art3(self):
        val = self.SpinBoxArt3.value() - 0.1
        self.SpinBoxArt3.setValue(val)

    def FKInc0_1Art3(self):
        val = self.SpinBoxArt3.value() + 0.1
        self.SpinBoxArt3.setValue(val)

    def FKInc1Art3(self):
        val = self.SpinBoxArt3.value() + 1
        self.SpinBoxArt3.setValue(val)

    def FKInc10Art3(self):
        val = self.SpinBoxArt3.value() + 10
        self.SpinBoxArt3.setValue(val)

    # FK Art4 Functions
    def FKMoveArt4(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = typeOfMovement + "X" + \
                str(self.SpinBoxArt4.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt4(self):
        val = self.FKSliderArt4.value() / 10
        self.SpinBoxArt4.setValue(val)

    def FKSpinBoxUpdateArt4(self):
        val = int(self.SpinBoxArt4.value() * 10)
        self.FKSliderArt4.setValue(val)

    def FKDec10Art4(self):
        val = self.SpinBoxArt4.value() - 10
        self.SpinBoxArt4.setValue(val)

    def FKDec1Art4(self):
        val = self.SpinBoxArt4.value() - 1
        self.SpinBoxArt4.setValue(val)

    def FKDec0_1Art4(self):
        val = self.SpinBoxArt4.value() - 0.1
        self.SpinBoxArt4.setValue(val)

    def FKInc0_1Art4(self):
        val = self.SpinBoxArt4.value() + 0.1
        self.SpinBoxArt4.setValue(val)

    def FKInc1Art4(self):
        val = self.SpinBoxArt4.value() + 1
        self.SpinBoxArt4.setValue(val)

    def FKInc10Art4(self):
        val = self.SpinBoxArt4.value() + 10
        self.SpinBoxArt4.setValue(val)

    # FK Art5 Functions
    # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
    def FKMoveArt5(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = typeOfMovement + "Y" + \
                str(self.SpinBoxArt5.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt5(self):
        val = self.FKSliderArt5.value() / 10
        self.SpinBoxArt5.setValue(val)

    def FKSpinBoxUpdateArt5(self):
        val = int(self.SpinBoxArt5.value() * 10)
        self.FKSliderArt5.setValue(val)

    def FKDec10Art5(self):
        val = self.SpinBoxArt5.value() - 10
        self.SpinBoxArt5.setValue(val)

    def FKDec1Art5(self):
        val = self.SpinBoxArt5.value() - 1
        self.SpinBoxArt5.setValue(val)

    def FKDec0_1Art5(self):
        val = self.SpinBoxArt5.value() - 0.1
        self.SpinBoxArt5.setValue(val)

    def FKInc0_1Art5(self):
        val = self.SpinBoxArt5.value() + 0.1
        self.SpinBoxArt5.setValue(val)

    def FKInc1Art5(self):
        val = self.SpinBoxArt5.value() + 1
        self.SpinBoxArt5.setValue(val)

    def FKInc10Art5(self):
        val = self.SpinBoxArt5.value() + 10
        self.SpinBoxArt5.setValue(val)

    # FK Art6 Functions
    # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
    def FKMoveArt6(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = typeOfMovement + "Z" + \
                str(self.SpinBoxArt6.value()) + feedRate
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def FKSliderUpdateArt6(self):
        val = self.FKSliderArt6.value() / 10
        self.SpinBoxArt6.setValue(val)

    def FKSpinBoxUpdateArt6(self):
        val = int(self.SpinBoxArt6.value() * 10)
        self.FKSliderArt6.setValue(val)

    def FKDec10Art6(self):
        val = self.SpinBoxArt6.value() - 10
        self.SpinBoxArt6.setValue(val)

    def FKDec1Art6(self):
        val = self.SpinBoxArt6.value() - 1
        self.SpinBoxArt6.setValue(val)

    def FKDec0_1Art6(self):
        val = self.SpinBoxArt6.value() - 0.1
        self.SpinBoxArt6.setValue(val)

    def FKInc0_1Art6(self):
        val = self.SpinBoxArt6.value() + 0.1
        self.SpinBoxArt6.setValue(val)

    def FKInc1Art6(self):
        val = self.SpinBoxArt6.value() + 1
        self.SpinBoxArt6.setValue(val)

    def FKInc10Art6(self):
        val = self.SpinBoxArt6.value() + 10
        self.SpinBoxArt6.setValue(val)

    # FK Every Articulation Functions
    # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
    def FKMoveAll(self):
        if s0.is_open:
            if self.G1MoveRadioButton.isChecked():
                typeOfMovement = "G1 "
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                typeOfMovement = "G0 "
                feedRate = ""
            message = (
                typeOfMovement
                + "A"
                + str(self.SpinBoxArt1.value())
                + " B"
                + str(self.SpinBoxArt2.value())
                + " C"
                + str(self.SpinBoxArt2.value())
                + " D"
                + str(self.SpinBoxArt3.value())
                + " X"
                + str(self.SpinBoxArt4.value())
                + " Y"
                + str(self.SpinBoxArt5.value())
                + " Z"
                + str(self.SpinBoxArt6.value())
                + feedRate
            )
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    # Gripper Functions
    # En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
    def MoveGripper(self):
        if s0.is_open:
            message = "M3 S" + str(
                (self.gripperUpperRange / 100) * self.SpinBoxGripper.value()
            )
            messageToSend = message + "\n"
            messageToConsole = ">>> " + message
            s0.write(messageToSend.encode("UTF-8"))
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            self.noSerialConnection()

    def SliderUpdateGripper(self):
        val = self.SliderGripper.value()
        self.SpinBoxGripper.setValue(val)

    def SpinBoxUpdateGripper(self):
        val = int(self.SpinBoxGripper.value())
        self.SliderGripper.setValue(val)

    def Dec10Gripper(self):
        val = self.SpinBoxGripper.value() - 10
        self.SpinBoxGripper.setValue(val)

    def Dec1Gripper(self):
        val = self.SpinBoxGripper.value() - 1
        self.SpinBoxGripper.setValue(val)

    def Inc1Gripper(self):
        val = self.SpinBoxGripper.value() + 1
        self.SpinBoxGripper.setValue(val)

    def Inc10Gripper(self):
        val = self.SpinBoxGripper.value() + 10
        self.SpinBoxGripper.setValue(val)

    # Serial Connection functions
    def getSerialPorts(self):
        self.SerialPortComboBox.clear()
        self.SerialPortComboBox.addItems(spf.serial_ports())

    def connectSerial(self):
        serialPort = self.SerialPortComboBox.currentText()
        baudrate = self.BaudRateComboBox.currentText()
        if serialPort != "":
            if baudrate != "":
                s0.port = serialPort
                s0.baudrate = int(baudrate)
                s0.timeout = 1
                try:
                    s0.close()
                    s0.open()
                    self.SerialThreadClass.start()
                except Exception as e:
                    print("error opening serial port: " + str(e))
            else:
                self.blankBaudRate()
        else:
            self.blankSerialPort()

    def serialDisconnected(self):
        self.RobotStateDisplay.setStyleSheet(
            "background-color: rgb(255, 0, 0)")
        self.RobotStateDisplay.setText("Disconnected")

    def updateConsole(self, dataRead):
        verboseShow = self.ConsoleShowVerbosecheckBox.isChecked()
        okShow = self.ConsoleShowOkRespcheckBox.isChecked()
        isDataReadVerbose = "MPos" in dataRead
        isDataOkResponse = "ok" in dataRead

        if dataRead == "SERIAL-DISCONNECTED":
            s0.close()
            self.serialDisconnected()
            print("Serial Connection Lost")

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
        messageToSent = self.ConsoleInput.text() + "\n"
        messageToConsole = ">>> " + self.ConsoleInput.text()
        if s0.is_open:
            if messageToSent != "":
                s0.write(messageToSent.encode("UTF-8"))
                self.ConsoleOutput.appendPlainText(messageToConsole)
                self.ConsoleInput.clear()
        else:
            self.noSerialConnection()

    def updateFKPosDisplay(self, dataRead):
        data = dataRead[1:][:-1].split(",")
        self.updateCurrentState(data[0])
        self.FKCurrentPosValueArt1.setText(data[1][5:][:-2] + "º")
        self.FKCurrentPosValueArt2.setText(data[2][:-2] + "º")
        self.FKCurrentPosValueArt3.setText(data[4][:-2] + "º")
        self.FKCurrentPosValueArt4.setText(data[5][:-2] + "º")
        self.FKCurrentPosValueArt5.setText(data[6][:-2] + "º")
        self.FKCurrentPosValueArt6.setText(data[7][:-2] + "º")

    def updateCurrentState(self, state):
        self.RobotStateDisplay.setText(state)
        if state == "Idle" or state == "Run":
            self.RobotStateDisplay.setStyleSheet(
                "background-color: rgb(0, 255, 0)")
        elif state == "Home":
            self.RobotStateDisplay.setStyleSheet(
                "background-color: rgb(85, 255, 255)")
        elif state == "Alarm":
            self.RobotStateDisplay.setStyleSheet(
                "background-color: rgb(255, 255, 0)")
        elif state == "Hold":
            self.RobotStateDisplay.setStyleSheet(
                "background-color: rgb(255, 0, 0)")
        else:
            self.RobotStateDisplay.setStyleSheet(
                "background-color: rgb(255, 255, 255)")

    def blankSerialPort(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setText(
            "There is not Serial Port value indicated to establish the connection.\nPlease check it and try to connect again."
        )
        msgBox.exec()

    def blankBaudRate(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setText(
            "There is not Baud Rate value indicated to establish the connection.\nPlease check it and try to connect again."
        )
        msgBox.exec()

    def noSerialConnection(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgBox.setText(
            "The connection has not been established yet. Please establish the connection before trying to control."
        )
        msgBox.exec()

# ------------------- LAUNCH PREFERENCES WINDOW ---------------------------- #
    def launchPreferencesWindow(self):
        dialog = PreferencesDialog(self.gripperUpperRange)
        result = dialog.exec()
        # print(f"Dialog result: {result}")  # Debugging print statement
        if result:
            # print("Dialog accepted")  # Debugging print statement
            # Update the variable with the new value from dialog
            self.gripperUpperRange = dialog.gripperUpperRange
            # Return value
            self.getGripperUpperRange()

    def getGripperUpperRange(self):
        self.saveSettings()
        return self.gripperUpperRange

# ---------------------------- SAVE SETTINGS --------------------------------#
    def saveSettings(self):
        """Save program settings for RotationAngle"""
        # Create a ConfigParser object to handle configuration file
        config = configparser.ConfigParser()

        # Define the 'Settings' section
        # set 'gripperUpperRange' key with the value as a string
        config["Settings"] = {"gripperUpperRange": str(self.gripperUpperRange)}

        # Open the settings.ini file in write mode
        with open("settings.ini", "w") as configfile:
            # print(self.gripperUpperRange) # Debugging print statement
            # Write the configuration data into the settings.ini file
            config.write(configfile)

# --------------------------- LOAD SETTINGS -------------------------------- #
    def loadSettings(self):
        """Load program prefences from settings.ini file"""
        # Check if the settings file exists
        if os.path.exists("settings.ini"):
            # Create a ConfigParser object to handle configuration file
            config = configparser.ConfigParser()

            # Read the content of the settings file
            config.read("settings.ini")

            # Check if the 'Settings' section exists in the configuration
            if "Settings" in config:
                # Get the 'gripperRange' value from the 'Settings' section
                gripperUpperRange = config["Settings"].get(
                    "gripperUpperRange", "0")

                # Convert the obtained value to an integer
                # and assign it to the gripperUpperRange variable
                self.gripperUpperRange = int(gripperUpperRange)

# ---------------------------- SET ICON ------------------------------------ #
    def setIcon(self):
        # Convert base64 to bytes
        image_32 = QByteArray.fromBase64(icon_32.encode())

        # Create QPixmap from bytes
        pixmap_32 = QPixmap()
        pixmap_32.loadFromData(image_32)

        # Convert base64 to bytes
        image_16 = QByteArray.fromBase64(icon_16.encode())

        # Create QPixmap from bytes
        pixmap_16 = QPixmap()
        pixmap_16.loadFromData(image_16)

        # Create and set icon
        icon = QIcon()
        icon.addPixmap(pixmap_32, QIcon.Mode.Normal, QIcon.State.Off)
        icon.addPixmap(pixmap_16, QIcon.Mode.Normal, QIcon.State.On)

        self.setWindowIcon(icon)


# ---------------------- ABOUT DIALOG CLASS -------------------------------- #
class AboutDialog(About_Ui_Dialog):
    def __init__(self, dialog):
        About_Ui_Dialog.__init__(self)
        self.setupUi(dialog)


def main():
    # Create the main application
    app = QtWidgets.QApplication(sys.argv)

    # Set the style of the application
    app.setStyle("Fusion")

    # Create the main window
    window = AsgardGUI()

    # Show the main window
    window.show()

    # Execute the program, setup clean exit of program
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
