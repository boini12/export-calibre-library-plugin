from calibre.utils.config import JSONConfig

from qt.core import QHBoxLayout, QLabel, QWidget, QLineEdit, QCheckBox

prefs = JSONConfig('plugins/export_calibre_books')

prefs.defaults['backup_destination'] = '/path/to/backup/location'
prefs.defaults['backup_automatically'] = False

class ConfigWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.l = QHBoxLayout()
        self.setLayout(self.l)

        self.label_destination = QLabel("Backup Destination:")
        self.l.addWidget(self.label_destination)

        self.msg = QLineEdit()
        self.msg.setText(prefs['backup_destination'])
        self.l.addWidget(self.msg)
        self.label_destination.setBuddy(self.msg)

        self.auto_backup_label = QLabel(" (Export new books each time Calibre is closed)")
        self.l.addWidget(self.auto_backup_label)

        self.checked = QCheckBox()
        self.checked.setChecked(prefs['backup_automatically'])
        self.l.addWidget(self.checked)
        self.auto_backup_label.setBuddy(self.checked)

    def save_settings(self):
        prefs['backup_destination'] = self.msg.text()
        prefs['backup_automatically'] = self.checked.isChecked()