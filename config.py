from pathlib import Path

from calibre.utils.config import JSONConfig

from qt.core import QLabel, QWidget, QLineEdit, QCheckBox, QVBoxLayout, QHBoxLayout, QPushButton

from .constant import SETTINGS_KEY_DESTINATIONS, LEGACY_SETTINGS_KEY_DESTINATION, SETTINGS_KEY_AUTOMATIC, DEFAULT_BACKUP_DESTINATION
from .path_line_edit import PathLineEdit

prefs = JSONConfig('plugins/export_calibre_books')

prefs.defaults[SETTINGS_KEY_DESTINATIONS] = [DEFAULT_BACKUP_DESTINATION]
prefs.defaults[SETTINGS_KEY_AUTOMATIC] = False


def get_destinations() -> list[str]:
    '''
    The configured backup destinations.

    Settings saved before SETTINGS_KEY_DESTINATIONS existed are read from the
    legacy key instead, and are written to the new key the next time settings
    are saved. The returned list is always a copy, because JSONConfig hands out
    the stored list itself and appending to that would edit the settings - or,
    when nothing is stored yet, the defaults - behind the dialog's back.
    '''
    if SETTINGS_KEY_DESTINATIONS in prefs:
        return list(prefs[SETTINGS_KEY_DESTINATIONS])

    if LEGACY_SETTINGS_KEY_DESTINATION in prefs:
        legacy = prefs[LEGACY_SETTINGS_KEY_DESTINATION]
        # Version 1.0.0 stored a single path, later unreleased builds a list.
        return [legacy] if isinstance(legacy, str) else list(legacy)

    return list(prefs.defaults[SETTINGS_KEY_DESTINATIONS])


class ConfigWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.destinations = get_destinations()

        self.outer_layout = QVBoxLayout()
        self.setLayout(self.outer_layout)

        self.destinations_label = QLabel("Backup Destinations:")
        self.outer_layout.addWidget(self.destinations_label)

        self.destinations_layout = QVBoxLayout()

        self.build_destinations()

        self.outer_layout.addLayout(self.destinations_layout)

        self.extend_destinations_layout = QHBoxLayout()

        self.extend_destinations_button = QPushButton("+")
        self.extend_destinations_button.setToolTip("Add additional backup destinations.")
        self.extend_destinations_button.setFixedSize(20, 20)
        self.extend_destinations_button.clicked.connect(self.new_destination_requested)

        self.extend_destinations_layout.addWidget(self.extend_destinations_button)
        self.extend_destinations_layout.addStretch()
        
        self.outer_layout.addLayout(self.extend_destinations_layout)

        self.auto_layout = QHBoxLayout()

        self.auto_backup_label = QLabel("Export new books each time Calibre is closed:")
        self.auto_layout.addWidget(self.auto_backup_label)

        self.checked = QCheckBox()
        self.checked.setChecked(prefs[SETTINGS_KEY_AUTOMATIC])
        self.auto_layout.addWidget(self.checked)
        self.auto_backup_label.setBuddy(self.checked)

        self.outer_layout.addLayout(self.auto_layout)

        # Soak up any leftover height at the bottom instead of spreading it between rows.
        self.outer_layout.addStretch()

        self.resize(self.sizeHint())


    def save_settings(self):
        prefs[SETTINGS_KEY_DESTINATIONS] = self.destinations
        prefs[SETTINGS_KEY_AUTOMATIC] = self.checked.isChecked()


    def new_destination_requested(self):
        self.new_destination_field = QLineEdit()
        self.new_destination_field.setPlaceholderText("Enter additional backup destination")

        self.extend_destinations_button.setEnabled(False)

        self.add_destination_button = QPushButton("Add")
        self.add_destination_button.setToolTip("Add the new backup destination.")
        self.add_destination_button.setFixedSize(40, 20)
        self.add_destination_button.setEnabled(False)
        self.add_destination_button.clicked.connect(lambda: self.add_destination(self.new_destination_field.text()))

        self.new_destination_field.textChanged.connect(
            lambda text: self.add_destination_button.setEnabled(self.is_destination_valid(text))
        )

        self.show_new_destination_field()


    def show_new_destination_field(self):
        self.extend_destinations_layout.insertWidget(1, self.new_destination_field)
        self.extend_destinations_layout.insertWidget(2, self.add_destination_button)


    def hide_new_destination_field(self):
        self.extend_destinations_layout.removeWidget(self.new_destination_field)
        self.new_destination_field.deleteLater()
        self.extend_destinations_layout.removeWidget(self.add_destination_button)
        self.add_destination_button.deleteLater()
        self.extend_destinations_button.setEnabled(True)


    def is_destination_valid(self, destination: str) -> bool:
        destination = destination.strip()
        return destination != "" and Path(destination).is_dir() and destination not in self.destinations


    def cache_destination(self, destination: str):
        if destination and destination not in self.destinations:
            self.destinations.append(destination)


    def remove_cached_destination(self, destination: str):
        if destination in self.destinations:
            self.destinations.remove(destination)


    def remove_destination(self, destination: str, row: QHBoxLayout):
        self.remove_cached_destination(destination)
        self.destinations_layout.removeItem(row)
        for i in reversed(range(row.count())):
            widget = row.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)


    def add_destination(self, destination: str):
        destination = destination.strip()
        self.cache_destination(destination)
        self.hide_new_destination_field()
        self.destinations_layout.addLayout(self.destination_row(destination))
        self.extend_destinations_button.setEnabled(True)


    def build_destinations(self):
        for destination in self.destinations:
            self.destinations_layout.addLayout(self.destination_row(destination))


    def destination_row(self, destination: str) -> QHBoxLayout:
        row = QHBoxLayout()
        field = PathLineEdit(destination)
        remove_button = QPushButton("Remove")
        remove_button.setToolTip("Remove this backup destination.")
        remove_button.setFixedSize(60, 20)
        remove_button.clicked.connect(lambda: self.remove_destination(destination, row))
        row.addWidget(field)
        row.addWidget(remove_button)
        return row