"""
   File: serial_read_thread_class.py
   Description: This file contains the class for the serial read thread.
   The serial read thread is used to read data from the serial port.
"""
import time
from PySide6 import QtCore
from PySide6.QtCore import Signal as Signal


class SerialThreadClass(QtCore.QThread):
    # Initialize a class variable to store the elapsed time
    elapsedTime = time.time()

    # Define a signal that will emit a string
    serialSignal = Signal(str)

# ---------------------------- INIT -------------------------------------- #
    def __init__(self, s0, parent=None):
        # Call the parent class (QThread) constructor
        super(SerialThreadClass, self).__init__(parent)

        # Store the incoming serial port object as an object variable
        self.s0 = s0

# ---------------------------- RUN --------------------------------------- #
    def run(self):
        # This method will run in a separate thread
        while True:
            # Check if the serial port is open
            if self.s0.isOpen():
                try:
                    # Check if there is data waiting in the serial buffer
                    self.s0.inWaiting()
                except:
                    # If an error occurs, emit a signal indicating
                    # the serial connection is lost
                    self.serialSignal.emit("SERIAL-DISCONNECTED")
                    print("Lost Serial connection!")

                try:
                    # Check if more than 0.1 seconds have passed
                    # since the last time check
                    if time.time() - self.elapsedTime > 0.1:
                        # Update the elapsed time
                        self.elapsedTime = time.time()

                        # Write a command to the serial port
                        self.s0.write("?\n".encode('UTF-8'))

                    # Read a line of data from the serial port
                    dataRead = str(self.s0.readline())

                    # Crop the data to remove unwanted characters
                    dataCropped = dataRead[2:][:-5]

                    # If the cropped data is not empty, emit it as a signal
                    if dataCropped != "":
                        self.serialSignal.emit(dataCropped)

                except Exception as e:
                    # If an error occurs, print the error message
                    print(f"Something failed: {e}")
