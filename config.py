from typing import List

from calibre.utils.config import JSONConfig

from qt.core import QLabel, QWidget, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout, QPushButton

from .constant import SETTINGS_KEY_DESTINATION, SETTINGS_KEY_AUTOMATIC, DEFAULT_BACKUP_DESTINATION

prefs = JSONConfig('plugins/export_calibre_books')

prefs.defaults[SETTINGS_KEY_DESTINATION] = DEFAULT_BACKUP_DESTINATION
prefs.defaults[SETTINGS_KEY_AUTOMATIC] = False

class ConfigWidget(QWidget):
    destinations: List[str] = []

    def __init__(self):
        QWidget.__init__(self)
        self.outer_layout = QVBoxLayout()
        self.setLayout(self.outer_layout)

        self.destination_layout = QVBoxLayout()

        self.destinations = prefs[SETTINGS_KEY_DESTINATION]
        self.build_destinations()

        self.outer_layout.addLayout(self.destination_layout)

        self.extend_destintions_layout = QHBoxLayout()

        self.extend_destinations_button = QPushButton("+")
        self.extend_destinations_button.setToolTip("Add additional backup destinations.")
        self.extend_destinations_button.setFixedSize(20, 20)
        self.extend_destinations_button.clicked.connect(self.new_destination_requested)

        self.extend_destintions_layout.addWidget(self.extend_destinations_button)
        self.extend_destintions_layout.addStretch()
        
        self.outer_layout.addLayout(self.extend_destintions_layout)

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
        prefs[SETTINGS_KEY_DESTINATION] = self.destinations
        prefs[SETTINGS_KEY_AUTOMATIC] = self.checked.isChecked()


    def new_destination_requested(self):
        new_destination_field = QLineEdit()
        new_destination_field.setPlaceholderText("Enter additional backup destination")

        self.extend_destinations_button.setEnabled(False)

        self.add_destination_button = QPushButton("Add")
        self.add_destination_button.setToolTip("Add the new backup destination.")
        self.add_destination_button.setFixedSize(40, 20)
        self.add_destination_button.clicked.connect(lambda: self.add_destination(new_destination_field.text()))

        self.extend_destintions_layout.addWidget(new_destination_field)
        self.extend_destintions_layout.addWidget(self.add_destination_button)


    def cache_destination(self, destination: str):
        if destination and destination not in self.destinations and destination != "":
            self.destinations.append(destination)


    def add_destination(self, destination: str):
        self.cache_destination(destination)
        self.destination_layout.addLayout(self.destination_row(destination))
        self.extend_destinations_button.setEnabled(True)


    def build_destinations(self):
        for destination in self.destinations:
            self.destination_layout.addLayout(self.destination_row(destination))


    def destination_row(self, destination: str) -> QHBoxLayout:
        row = QHBoxLayout()
        label = QLabel(f"Backup Destination:")
        field = QLineEdit(destination)
        label.setBuddy(field)
        row.addWidget(label)
        row.addWidget(field)
        return row