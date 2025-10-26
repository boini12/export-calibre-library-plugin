import shutil
import sys
from pathlib import Path
from datetime import datetime

from calibre.library import db

CALIBRE_LIBRARY_LOCATION = "/Users/ibohr/Documents/Calibre"

def export_books(src: Path, dest: Path):
    date = get_current_data()
    backup_path = dest / f"calibre_backup_{date}"
    author_folder_paths = get_calibre_books()
    copy_to_backup(author_folder_paths, backup_path)


def get_calibre_books() -> list[Path]:
    calibre_db = db(CALIBRE_LIBRARY_LOCATION).new_api
    book_ids = calibre_db.all_book_ids()
    author_folder_paths = []

    for book_id in book_ids:
        relative_book_path = calibre_db.get_book_path(book_id)
        relative_path_to_author_folder = Path(*Path(relative_book_path).parts[:-1])
        abs_author_folder_path = Path(CALIBRE_LIBRARY_LOCATION) / relative_path_to_author_folder
        author_folder_paths.append(abs_author_folder_path)
    
    return author_folder_paths

def copy_to_backup(src_paths: list[Path], dest: Path):
    if not dest.exists():
       dest.mkdir(exist_ok=True)

    for src_path in src_paths:
        target_path = dest / src_path.name
        shutil.copytree(src_path, target_path, dirs_exist_ok=True)

def get_current_data() -> str:
    date = datetime.today().strftime('%Y-%m-%d')
    return date

args = sys.argv
if len(args) < 2:
    print("Please provide a destination path for the backup.")
    sys.exit(1)

export_books(Path(CALIBRE_LIBRARY_LOCATION), Path(args[1]))
