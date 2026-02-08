# <img src="images/icon.png" alt="drawing" width="35"/> Calibre Export Plugin

A Calibre plugin that allows you to easily export your Calibre library — either manually or automatically when Calibre closes.

## ✨ Features

- 🧰 **Toolbar Button for Configuration and manual execution**  
  The plugin adds a button to the Calibre toolbar.  
  Click it to open either the plugin settings or manually execute an export.

- 📁 **Set Export Destination Path**  
  You **must** specify a destination path in the settings.  
  This is the folder where your Calibre library will be exported to.

- 🔁 **Auto-Export on Close (Optional)**  
  When enabled, Calibre will automatically export your library every time it closes:
  - If a previous export already exists at the destination path:  
    ➤ Only newly added books are exported.  
  - If no previous export exists:  
    ➤ The entire library is exported.

## 🗂️ Export Structure

When exported, the files are organized like this:
``` text
<destination_path>/
calibre_backup_{date of export}/
├── Author Name/
│ ├── Book Title/
│ │ ├── book.epub
│ │ ├── cover.jpg
│ │ └── metadata.opf
│ └── Another Book/
└── Another Author/
```

Each export is stored in a date-stamped folder (e.g., `calibre_backup_2025-10-26`).

## ⚙️ Usage

1. **Install the plugin** in Calibre.
2. **Click the plugin’s toolbar icon** to open settings.
3. **Set your destination path** — where backups will be saved.
4. (Optional) Enable **Auto Export on Close**.
5. Close Calibre or trigger the export manually.

## :rocket: Running the Project
1. Clone the repository
2. Have Calibre installed
3. Open repository in your preferred IDE, e.g., VS Code
4. Run calibre-debug -g to start Calibre in debug mode

## 🧠 Notes

- Ensure that the destination path has sufficient storage space.
- Auto-export only triggers when Calibre is properly closed (not if it crashes).
