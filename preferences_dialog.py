from PySide6.QtWidgets import QDialog, QDialogButtonBox, QSpinBox
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QByteArray
from preferences import Ui_PreferencesDialog
from img.thor_icon import icon_32, icon_16


class PreferencesDialog(QDialog, Ui_PreferencesDialog):
    def __init__(self, gripperUpperRange, parent=None):
        super().__init__(parent)
        # Ensure the UI is set up
        self.setupUi(self)

        # Store references to UI elements
        self.spinBoxGripperUpperRange = self.findChild(
            QSpinBox, "spinBoxGripperUpperRange")
        self.buttonBox = self.findChild(QDialogButtonBox, "buttonBox")

        # Set initial values
        self.spinBoxGripperUpperRange.setValue(gripperUpperRange)

        # Connect the dialog buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setIcon()

    @property
    def gripperUpperRange(self):
        return int(self.spinBoxGripperUpperRange.value())

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
        icon.addPixmap(pixmap_32, QIcon.Normal, QIcon.Off)
        icon.addPixmap(pixmap_16, QIcon.Normal, QIcon.On)

        self.setWindowIcon(icon)
