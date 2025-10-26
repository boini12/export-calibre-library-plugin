import shutil
import os

from pathlib import Path
from datetime import datetime

from .constant import EXPORT_PREFIX, SETTINGS_KEY_AUTOMATIC, SETTINGS_KEY_DESTINATION, DEFAULT_BACKUP_DESTINATION

from calibre_plugins.export_calibre_books.config import prefs

def export_books(db, current_db):
        if prefs[SETTINGS_KEY_AUTOMATIC] is False:
            return
        
        destination = prefs[SETTINGS_KEY_DESTINATION]

        if destination == DEFAULT_BACKUP_DESTINATION:
            return        
             
        backup_dirs = [d for d in os.listdir(destination) 
                      if d.startswith(EXPORT_PREFIX)]
        
        if backup_dirs:
            latest_backup = sorted(backup_dirs)[-1]
            backup_destination = Path(destination) / latest_backup
        else:
            backup_destination = Path(destination) / f"{EXPORT_PREFIX}{_get_current_date()}"

        if not backup_destination.exists():
            backup_destination.mkdir(exist_ok=True)
            _export_whole_library(db, current_db, backup_destination)

        else:
            new_dest = backup_destination.parent / (EXPORT_PREFIX + _get_current_date())
            backup_destination.rename(Path(backup_destination.parent) / new_dest)
            backup_destination = new_dest
            _export_updated_books(db, current_db, backup_destination)
       

def _export_whole_library(db, current_db, backup_destination):
    author_folder_paths = _get_author_folder_paths(db=db, current_db=current_db)
    _copy_to_backup(author_folder_paths, backup_destination, True)

def _export_updated_books(db, current_db, backup_destination):
    relative_book_paths = _get_book_paths(db=db)
    new_books = _get_new_books(current_db, relative_book_paths, backup_destination)
    _copy_to_backup(new_books, backup_destination, False)

def _get_current_date() -> str:
    date = datetime.today().strftime('%Y-%m-%d')
    return date

def _get_author_folder_paths(db, current_db) -> list[Path]:
    book_ids = db.all_book_ids()
    author_folder_paths = []

    for book_id in book_ids:
        relative_book_path = db.get_book_path(book_id)
        relative_path_to_author_folder = Path(*Path(relative_book_path).parts[:-1])
        abs_author_folder_path = Path(current_db.library_path) / relative_path_to_author_folder
        author_folder_paths.append(abs_author_folder_path)
    
    return author_folder_paths

def _get_book_paths(db) -> list[Path]:
    book_ids = db.all_book_ids()
    relative_book_paths = []

    for book_id in book_ids:
        relative_book_path = Path(db.get_book_path(book_id))
        relative_book_paths.append(relative_book_path)
    
    return relative_book_paths

def _get_new_books(current_db, relative_book_paths, backup_destination) -> list[Path]:
    new_books = []

    for relative_book_path in relative_book_paths:
        exported_path = backup_destination / relative_book_path
        if not exported_path.exists():
            absolute_book_path =  Path(current_db.library_path) / relative_book_path
            new_books.append(absolute_book_path)

    return new_books

def _copy_to_backup(src_paths: list[Path], dest: Path, full_export):
    if not full_export:
        print(len(src_paths), "book[s] to export.")

    for src_path in src_paths:
        target_path = ""
        if full_export:
            target_path = dest / src_path.name
        else:
            target_path = dest / src_path.parent.name / src_path.name

        print(f"Exporting {src_path} to {target_path}")

        shutil.copytree(src_path, target_path, dirs_exist_ok=True)