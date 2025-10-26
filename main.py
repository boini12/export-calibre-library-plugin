from calibre_plugins.export_calibre_books.config import prefs

from qt.core import QDialog, QLabel, QMessageBox, QPushButton, QVBoxLayout

class ExportDialog(QDialog):
    def __init__(self, gui, icon, do_user_config):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.do_user_config = do_user_config

        self.db = gui.current_db.new_api
        self.l = QVBoxLayout()
        self.setLayout(self.l)

        self.label = QLabel("Export Calibre Books Plugin")
        self.l.addWidget(self.label)
        
        self.setWindowTitle("Export Calibre Books")
        self.setWindowIcon(icon)

        self.resize(self.sizeHint())