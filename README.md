# Chrome History Editor
For those "doggy students" who didn’t finish their basement (a.k.a. homework) but still need to prove they were working on it!

## Overview

**Chrome History Editor** is your new best friend, designed to help you manage and modify your Chrome browser history. Whether you need to prove you were actually researching, downloading files, or just need to clean up your browsing records, this Python-based tool is the perfect way to get your act together. You can modify URLs, update visit times, and even adjust those tricky download timestamps. The best part? It’s easy, thanks to a user-friendly interface!

### Important:

**Backup your Chrome history file first!**  
We all know accidents happen—like deleting that file with all your research! Always make a backup before diving in.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage Instructions](#usage-instructions)
5. [Backup & Precautions](#backup-and-precautions)
6. [Notes](#notes)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Load History Database:** Access your Chrome history database in no time.
- **Edit Entries:** Change URLs, titles, and more—because you really were working on your project... right?
- **Update Timestamps:** Fix those visit times or download timestamps to match your "studious" late-night sessions.
- **Simple GUI:** A clean, easy-to-use interface powered by Tkinter—because who has time for complicated stuff?

---

## Prerequisites

Before you begin, make sure you’ve got the basics:

- Python 3.x installed (most of us have it by now, right?)

---

## Installation

### Option 1: Download the Latest Release

1. Head over to the [Releases page on GitHub](https://github.com/nirmanpreet/chrome_history_editor/releases).
2. Download the version that fits your system.
3. Run the executable or grab the ZIP file and execute the Python script.

### Option 2: Clone the Repository

1. Clone the repo using this command:

   ```bash
   git clone https://github.com/nirmanpreet/chrome_history_editor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chrome_history_editor
   ```

3. Run the program:

   ```bash
   python chrome_history_editor.py
   ```

---

## Usage Instructions

### Option 1: Using the Executable File

1. Download the `.exe` from the [Releases page](https://github.com/nirmanpreet/chrome_history_editor/releases).
2. Double-click it to launch the app. No setup needed. Simple!

### Option 2: Running the Python Script

1. **Locate Your Chrome History File:**
   - Windows: `C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\History`
   - Mac: `~/Library/Application Support/Google/Chrome/Default/History`
   - Linux: `~/.config/google-chrome/Default/History`

2. Copy the file and place it in the folder with the script.

3. Run the script:

   ```bash
   python chrome_history_editor.py
   ```

4. **Load the Database:**  
   Click the "Load Database" button and choose your copied History file.

5. **Edit History:**  
   Modify your URLs, titles, visit times, and even those downloads—yep, we see you downloading all that research at 3 AM!

6. **Save Changes:**  
   The tool will save your changes automatically back into the database. You’ll be all set to prove you were on top of things (even if it was last minute).

---

## Backup and Precautions

### Backup, Backup, Backup!

Before making any changes, create a backup. If you don’t, you might find yourself in the doghouse for real. The tool includes options to create and restore backups, but it’s always wise to manually back up first.

---

## Notes

- **Close Chrome before using the program** to avoid database conflicts (Chrome's not a fan of changes happening while it’s still open).
- Be careful with edits—one wrong move and you could be showing off more than you bargained for (like those sneaky tabs you thought you closed).

---

## Contributing

Got any ideas to make this tool even more useful? Feel free to fork the repo, make improvements, and send a pull request. If you’ve found a bug or have a feature request, open an issue on GitHub.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
