from PyQt6.QtWidgets import QDialog, QSpinBox, QDialogButtonBox
from preferences import Ui_PreferencesDialog


class PreferencesDialog(QDialog, Ui_PreferencesDialog):
    def __init__(self, gripperUpperRange, parent=None):
        super().__init__(parent)
        # Ensure the UI is set up
        self.setupUi(self)

        # Store references to UI elements
        self.spinBoxGripperUpperRange = self.findChild(QSpinBox, "spinBoxGripperUpperRange")
        self.buttonBox = self.findChild(QDialogButtonBox, "buttonBox")

        # Set initial values
        self.spinBoxGripperUpperRange.setValue(gripperUpperRange)

        # Connect the dialog buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    @property
    def gripperUpperRange(self):
        return int(self.spinBoxGripperUpperRange.value())
