# 📁 Smart File Organizer

A powerful and intuitive file organization tool that automatically categorizes and organizes files based on their extensions. Perfect for cleaning up messy directories and maintaining an organized file system.

## ✨ Features

- **🗂️ Smart Categorization**: Automatically sorts files into appropriate folders
- **🛠️ Flexible Rules**: Choose from predefined categories or create your own
- **📁 Multiple Setup Options**:
  - Use predefined category rules (Documents, Images, Videos, Music)
  - Create custom categories and extensions
  - Import rules from external files
- **🔄 Duplicate Handling**: Automatically renames duplicate files with unique names
- **📊 Progress Tracking**: Real-time feedback on organization progress
- **✅ Safety First**: Never overwrites existing files
- **📁 Directory Support**: Intelligently skips existing folders during organization

## 📋 Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## 🚀 Installation

1. **Download** the `organizer.py` file
2. **Navigate** to the directory containing the script
3. **Run** the organizer:

```bash
python organizer.py
```

📖 Usage Guide
1. Starting the Tool
Run the script and follow the interactive prompts:

```bash
python organizer.py
```
2. Category Setup Options

```bash
=== Category Setup ===
1. Use predefined category rules
2. Create your own category rules manually
3. Import category rules from a file
Option 1: Predefined Rules (Recommended for beginners)
Automatically uses these categories:

Documents: .pdf, .docx, .txt

Images: .jpg, .png, .gif

Videos: .mp4, .avi, .mkv

Music: .mp3, .flac, .wav

Other: Everything else
```
Option 2: Custom Rules

Create your own categories and file extensions:

```bash
Enter category name: WorkFiles
Add file types: .xlsx, .pptx, .doc
Option 3: Import Rules
Import rules from a text file with format:
```

3. Directory Organization
Enter the path to your messy folder:

```bash
Enter your folder path: C:/Users/Name/Downloads
```
4. Watch It Work!

The organizer will:

Create category folders

Move files to appropriate folders

Handle duplicates (e.g., file_copy1.pdf)

Skip existing folders

Provide progress updates

🎯 Example Workflow
```bash
Welcome to your File Organizer!
=== Category Setup ===
1. Use predefined category rules
2. Create your own category rules manually
3. Import category rules from a file

Enter your choice (1/2/3): 1
Enter your folder path: /home/user/Downloads

📁 Created folder: Documents
📁 Created folder: Images
📁 Created folder: Videos
📁 Created folder: Music
📁 Created folder: Other

✅ MOVED: report.pdf → Documents/
✅ MOVED: photo.jpg → Images/
🔄 RENAMED: song.mp3 → Music/song_copy1.mp3
⏭️  Skipping directory: AlreadySorted

=== Organization Summary ===
✅ Files successfully organized: 45
⏭️  Files skipped: 3
File organization completed!
```
🛠️ File Format for Import
Create a text file (e.g., rules.txt) with this format:

```bash
Documents: .pdf, .doc, .docx, .txt, .rtf
Images: .jpg, .jpeg, .png, .gif, .bmp
Code: .py, .js, .html, .css, .java
Archives: .zip, .rar, .7z, .tar
```
⚠️ Important Notes
Backup Important Files: Always backup before organizing critical directories

Case Insensitive: File extensions are matched case-insensitively


No Data Loss: The tool never deletes files, only moves them


Duplicate Protection: If a file already exists, it creates filename_copyX.ext

Folder Skipping: Existing directories are not processed

Extension Required: Files without extensions go to "Other" category

🔧 Technical Details

Pure Python: No external dependencies

Built-in Modules: Uses only os and shutil

Error Handling: Comprehensive error messages for common issues

Progress Feedback: Real-time updates during organization


📁 Example Project Structure

Before:

```bash
Downloads/
├── report.pdf
├── photo.jpg
├── video.mp4
├── song.mp3
├── notes.txt
└── setup.exe
```
After:

```bash
Downloads/
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Images/
│   └── photo.jpg
├── Videos/
│   └── video.mp4
├── Music/
│   └── song.mp3
├── Other/
│   └── setup.exe
└── organizer.py
```
🤝 Contributing
Feel free to fork and improve! Some ideas:

Add GUI interface

Support for file content-based organization

Undo functionality

Schedule automatic organization


📄 License
This project is open source and available under the MIT License.

Happy Organizing! 🎉
