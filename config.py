from calibre.utils.config import JSONConfig

from qt.core import QLabel, QWidget, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout

from .constant import SETTINGS_KEY_DESTINATION, SETTINGS_KEY_AUTOMATIC, DEFAULT_BACKUP_DESTINATION

prefs = JSONConfig('plugins/export_calibre_books')

prefs.defaults[SETTINGS_KEY_DESTINATION] = DEFAULT_BACKUP_DESTINATION
prefs.defaults[SETTINGS_KEY_AUTOMATIC] = False

class ConfigWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.outer_layout = QVBoxLayout()
        self.setLayout(self.outer_layout)

        self.destination_layout = QHBoxLayout()

        self.label_destination = QLabel("Backup Destination:")
        self.destination_layout.addWidget(self.label_destination)

        self.msg = QLineEdit()
        self.msg.setText(prefs[SETTINGS_KEY_DESTINATION])
        self.destination_layout.addWidget(self.msg)
        self.label_destination.setBuddy(self.msg)

        self.outer_layout.addLayout(self.destination_layout)

        self.auto_layout = QHBoxLayout()

        self.auto_backup_label = QLabel("Export new books each time Calibre is closed:")
        self.auto_layout.addWidget(self.auto_backup_label)

        self.checked = QCheckBox()
        self.checked.setChecked(prefs[SETTINGS_KEY_AUTOMATIC])
        self.auto_layout.addWidget(self.checked)
        self.auto_backup_label.setBuddy(self.checked)

        self.outer_layout.addLayout(self.auto_layout)

        self.resize(self.sizeHint())


    def save_settings(self):
        prefs[SETTINGS_KEY_DESTINATION] = self.msg.text()
        prefs[SETTINGS_KEY_AUTOMATIC] = self.checked.isChecked()