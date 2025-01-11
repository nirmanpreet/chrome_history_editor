

# Chrome History Editor

## **Overview**
Chrome History Editor is a Python-based graphical user interface (GUI) application that allows users to edit the browsing history stored in the **History** SQLite database of Google Chrome. The tool provides functionality to modify URL titles, visit times, and other browsing-related data.

**Warning**: Modifying the browser history can have unintended consequences. Please ensure that you know what you're doing and **backup** your Chrome history file before making any changes.

---

## **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [Installation Instructions](#installation-instructions)
3. [Running the Program](#running-the-program)
4. [How to Use the Program](#how-to-use-the-program)
5. [Backup & Precautions](#backup--precautions)
6. [Important Notes](#important-notes)
7. [Conclusion](#conclusion)

---

## **Prerequisites**

To use the Chrome History Editor, you need to have **Python** installed along with a few required libraries.

### **Required Software**:
1. **Python** (version 3.x or above)  
2. **pip** (Python package installer)  

---

## **Installation Instructions**

### **Step 1: Install Python**

#### **For Windows**:
1. Download Python from the official Python website: [Download Python](https://www.python.org/downloads/).
2. Run the installer and **ensure the option "Add Python to PATH" is checked**.
3. Follow the installation prompts, then click "Install Now".
4. Verify that Python is installed correctly by opening the Command Prompt and typing the following command:

   ```bash
   python --version
   ```

   This should output the installed Python version (e.g., `Python 3.x.x`).

---

### **Step 2: Install Required Libraries**

The program requires a few external libraries. Install them by running the following commands in your command prompt:

1. **tkinter** (for GUI interface)  
2. **sqlite3** (for working with SQLite database)

Run the following command:

```bash
pip install tkinter sqlite3
```

---

### **Step 3: Download or Clone the Program**

You can either download the ZIP file or clone the repository.

1. **Download the program:**
   - Visit the official GitHub repository: [Chrome History Editor GitHub](https://github.com/nirmanpreet/chromehistoryeditor).
   - Download the ZIP file, extract it, and place it in a directory.

2. **Clone the repository** (if you have Git installed):

   ```bash
   git clone https://github.com/nirmanpreet/chromehistoryeditor
   cd chrome-history-editor
   ```

---

### **Step 4: Prepare the History File**

1. **Find Your Chrome History File**:
   - The Chrome History file is stored in your user data directory at:

     ```
     C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default\History
     ```

   Replace `YourUsername` with your actual username on the computer.

2. **Copy the History File**:
   - Make a copy of the `History` file and **place it in the same directory** as the `chrome_history_editor.py` script.

---

## **Running the Program**

### **Step 1: Open Command Prompt**

1. Open the **Command Prompt** on your system.

2. **Navigate to the folder** where you saved the `chrome_history_editor.py` script. Use the `cd` command:

   ```bash
   cd path\to\your\script\folder
   ```

### **Step 2: Run the Script**

Run the following command to start the Chrome History Editor:

```bash
python chrome_history_editor.py
```

This will launch the program, and you should see the graphical interface.

---

## **How to Use the Program**

1. **Load Data**: Click the **Load Data** button. This loads your Chrome history from the `History` SQLite database.

2. **View and Edit Data**: You can view the URL, title, and last visit time in a table. You can double-click on the `Last Visit Time` field to edit it.

3. **Edit URL and Title**: You can modify the URL and Title for each entry directly in the table. After making changes, click **Save Changes** to store them back in the database.

4. **Change Visit Time**: You can modify the visit time and the program will convert it back to Chrome's epoch format (microseconds since January 1, 1601).

5. **Delete Row**: Select a row and click the **Delete Row** button to remove that entry from the database.

6. **Refresh Data**: Click **Refresh** to reload the current data from the database after making changes.

---

## **Backup & Precautions**

### **Backup Your Data**
Before making any changes, **back up your History file** to avoid losing important data:

1. Copy the `History` file from the following location:

   ```
   C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default\History
   ```

2. Place the backup in a safe location on your computer.

3. To restore the backup, simply replace the edited `History` file with your backup file.

---

## **Important Notes**

1. **Close Google Chrome** before running this program. The program modifies the `History` file, and Chrome should not be running while this happens to avoid file corruption.

2. **Ensure you have a backup** of your History file before editing it.

3. **Be cautious when modifying the history**. Editing the history can affect your Chrome browsing data and syncing across devices.

---

## **Conclusion**

You have now successfully set up the Chrome History Editor and can use it to modify your browsing history in Google Chrome. Always remember to back up your data before making any changes, and use this program responsibly.

Feel free to explore and customize the program to suit your needs. For any issues or suggestions, you can reach out via the GitHub repository or contact the author.

---

### **Author**
Nirmanpreet Singh
