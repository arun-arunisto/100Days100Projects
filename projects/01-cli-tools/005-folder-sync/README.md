# Folder Sync CLI

A command-line tool to synchronize files and folders from a source to a destination directory.

---

## 🚀 Features

* 📁 Sync entire folders recursively
* 📄 Sync individual files
* 🔄 Smart update detection (only copies newer files)
* ✨ Creates destination directories automatically
* 🕐 Preserves file metadata (timestamps, permissions)
* 📊 Clear status output for each file action

---

## 🛠 Usage

### Sync a folder

```bash
python main.py /path/to/source /path/to/destination
```

### Sync a single file

```bash
python main.py /path/to/file.txt /path/to/destination/
```

---

## 📊 Example Output

```
              ._   .  .         
 __  .._  _.  |, _ | _| _ ._. __
_) \_|[ )(_.  | (_)|(_](/,[  _) 
   ._|     created by: arunisto                  

[NEW] /home/user/source/document.pdf
[UPDATED] /home/user/source/notes.txt
[COPIED] /home/user/source/image.png
```

### Status Labels

| Label       | Description                              |
|-------------|------------------------------------------|
| `[NEW]`     | File copied (didn't exist in destination)|
| `[UPDATED]` | File updated (source was newer)          |
| `[COPIED]`  | Single file copied to destination        |
| `[SKIPPED]` | File skipped (already up to date)        |

---

## 📁 Project Structure

```
005-folder-sync/
├── main.py          # Entry point with CLI argument parsing
├── utilities.py     # Core sync logic
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

---

## 🔧 Requirements

* Python 3.x
* No external dependencies (uses standard library only)

---

## 📝 How It Works

1. **Folder sync**: Recursively walks through the source directory
2. **File comparison**: Checks if destination file exists
3. **Timestamp check**: Compares modification times
4. **Smart copy**: Only copies new or updated files using `shutil.copy2()` to preserve metadata

---

## 💡 Use Cases

* Backup important folders
* Sync project files to external drives
* Mirror directories across locations
* Quick file deployment

---

## 👤 Author

Created by **arunisto**
