from calibre.utils.config import JSONConfig

from qt.core import QHBoxLayout, QLabel, QWidget, QLineEdit

prefs = JSONConfig('plugins/export_calibre_books')

prefs.defaults['backup_destination'] = '/path/to/backup/location'

class ConfigWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.l = QHBoxLayout()
        self.setLayout(self.l)

        self.label = QLabel("Backup Destination:")
        self.l.addWidget(self.label)

        self.msg = QlineEdit()
        self.msg.setText(prefs['backup_destination'])
        self.l.addWidget(self.msg)
        self.label.setBuddy(self.msg)

    def save_settings(self):
        prefs['backup_destination'] = self.msg.text()