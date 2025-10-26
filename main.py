from datetime import datetime
from pathlib import Path
import shutil

from .export import export_books

from calibre_plugins.export_calibre_books.config import prefs

from qt.core import QDialog, QLabel, QPushButton, QVBoxLayout, QCheckBox

class ExportDialog(QDialog):
    def __init__(self, gui, icon, do_user_config):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.do_user_config = do_user_config

        self.db = gui.current_db.new_api
        self.current_db = gui.current_db
        self.l = QVBoxLayout()
        self.setLayout(self.l)

        self.label = QLabel("Export Calibre Books Plugin")
        self.l.addWidget(self.label)
        
        self.setWindowTitle("Export Calibre Books")
        self.setWindowIcon(icon)

        self.conf_button = QPushButton("Configure Backup Settings", self)
        self.conf_button.clicked.connect(self.config)
        self.l.addWidget(self.conf_button)

        self.export_button = QPushButton("Export Books Now", self)
        self.export_button.clicked.connect(self.export_books)
        self.l.addWidget(self.export_button)

        self.resize(self.sizeHint())


    def export_books(self):
        export_books(self.db, self.current_db)

    def config(self):
        self.do_user_config(parent=self)
        self.label.setText(prefs['backup_destination'])