from datetime import datetime
from pathlib import Path
import shutil

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

        self.conf_button = QPushButton("Configure Backup Settings", self)
        self.conf_button.clicked.connect(self.config)
        self.l.addWidget(self.conf_button)

        self.export_button = QPushButton("Export Books Now", self)
        self.export_button.clicked.connect(self.export_books)
        self.l.addWidget(self.export_button)

        self.resize(self.sizeHint())


    def export_books(self):
        date = self._get_current_date()
        backup_destination = Path(prefs['backup_destination']) / f"calibre_backup_{date}"
        author_folder_paths = self.get_author_folder_paths()
        self._copy_to_backup(author_folder_paths, backup_destination)

    def config(self):
        self.do_user_config(parent=self)
        self.label.setText(prefs['backup_destination'])


    def _get_current_dat(self) -> str:
        date = datetime.today().strftime('%Y-%m-%d')
        return date

    def get_author_folder_paths(self) -> list[Path]:
        book_ids = self.db.all_book_ids()
        author_folder_paths = []

        for book_id in book_ids:
            relative_book_path = self.db.get_book_path(book_id)
            relative_path_to_author_folder = Path(*Path(relative_book_path).parts[:-1])
            abs_author_folder_path = Path(self.db.library_path) / relative_path_to_author_folder
            author_folder_paths.append(abs_author_folder_path)
        
        return author_folder_paths

    def _copy_to_backup(self, src_paths: list[Path], dest: Path):
        if not dest.exists():
            dest.mkdir(exist_ok=True)

        for src_path in src_paths:
            target_path = dest / src_path.name
            shutil.copytree(src_path, target_path, dirs_exist_ok=True)

   