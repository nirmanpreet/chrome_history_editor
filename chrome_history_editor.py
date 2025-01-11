import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import shutil
import os

# Chrome's epoch start date: January 1, 1601
CHROME_EPOCH_START = datetime(1601, 1, 1)

class ChromeDataModifier:
    def __init__(self, root):
        """
        Initialize the ChromeDataModifier class.

        Args:
        root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.conn = None
        self.log_text = None
        self.db_path = None
        self.backup_path = None

        # Setup main application window
        self.root.title("Modify Chrome Data by Nirmanpreet Singh")
        self.root.geometry("1200x800")

        # Create a frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create buttons
        self.open_db_button = tk.Button(self.button_frame, text="Open Database", command=self.open_database_file)
        self.open_db_button.grid(row=0, column=0, padx=5)

        self.modify_downloads_button = tk.Button(self.button_frame, text="Modify Downloads", command=self.modify_downloads)
        self.modify_downloads_button.grid(row=0, column=1, padx=5)

        self.modify_history_button = tk.Button(self.button_frame, text="Modify History", command=self.modify_history)
        self.modify_history_button.grid(row=0, column=2, padx=5)

        self.backup_button = tk.Button(self.button_frame, text="Backup Database", command=self.backup_database)
        self.backup_button.grid(row=0, column=3, padx=5)

        self.restore_button = tk.Button(self.button_frame, text="Restore Database", command=self.restore_database)
        self.restore_button.grid(row=0, column=4, padx=5)

        # Create a frame for instructions
        self.instructions_frame = tk.Frame(self.root)
        self.instructions_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        instructions = (
            "Step-by-Step Instructions:\n"
            "1. Open your file explorer and navigate to the following directory:\n"
            "   C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data\\Default\n"
            "   (Replace 'username' with your actual Windows username.\n"
            "   If you're logged into Chrome, use the logged-in user's name instead of 'Default' (e.g., \\User Data\\Logged in name)).\n"
            "   This is where the Chrome history database file is located.\n"
            "\n"
            "2. **Important**: Close Google Chrome before proceeding with any edits to the database.\n"
            "   If Chrome is open, your changes may not be applied correctly.\n"
            "\n"
            "3. Click 'Open Database' in the application to select and load the Chrome history database file.\n"
            "4. Once the database is loaded, you will see a success message.\n"
            "5. Click 'Backup Database' to create a backup of the current database in case of any issues.\n"
            "6. Click 'Modify Downloads' to open a window where you can view and edit the downloads table.\n"
            "7. Click 'Modify History' to open a window where you can view and edit the history table.\n"
            "8. Once edits are made, **close the application** and **reopen Google Chrome** to check if the changes have been applied.\n"
            "   - If you see the edits in Chrome, you’re done!\n"
            "   - If you want to make more edits, repeat the process by closing Chrome and reopening the program to make further modifications.\n"
            "9. **Important**: Always ensure Chrome is closed while making edits to the database. If Chrome is running, your changes will not be applied.\n"
            "10. If something goes wrong, click 'Restore Database' to restore the database from the backup you created.\n"
            "11. Use the log window to view logs and messages related to your actions.\n"
            "\n"
            "### Important Notes:\n"
            "- Chrome must be closed before making any edits to the database. If Chrome is open, your changes will not be applied.\n"
            "- Always reopen Chrome after editing to verify the changes were successful."
        )

        self.instructions_label = tk.Label(self.instructions_frame, text=instructions, justify=tk.LEFT)
        self.instructions_label.pack()

        # Create log window
        self.log_window = tk.Frame(self.root)
        self.log_window.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")
        self.log_window.columnconfigure(0, weight=1)
        self.log_window.rowconfigure(0, weight=1)

        self.log_text = tk.Text(self.log_window, wrap=tk.WORD, height=30, width=40)
        self.log_text.grid(row=0, column=0, sticky="nsew")

        log_scrollbar = tk.Scrollbar(self.log_window, orient="vertical", command=self.log_text.yview)
        log_scrollbar.grid(row=0, column=1, sticky="ns")
        self.log_text['yscrollcommand'] = log_scrollbar.set

        self.log_text.insert(tk.END, "Logs will appear here...\n")

    def log_message(self, message):
        """
        Log messages to the log window in the GUI.

        Args:
        message (str): The message to be logged.
        """
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.yview(tk.END)

    def datetime_to_chrome_epoch(self, dt):
        """
        Convert a standard datetime to Chrome's epoch format.

        Args:
        dt (datetime): The datetime to be converted.

        Returns:
        int: The Chrome epoch value.
        """
        delta = dt - CHROME_EPOCH_START
        return int(delta.total_seconds() * 1_000_000)

    def epoch_to_human_readable(self, epoch):
        """
        Convert Chrome's epoch format to a human-readable datetime.

        Args:
        epoch (int): The Chrome epoch value.

        Returns:
        str: The human-readable datetime.
        """
        try:
            epoch_in_seconds = epoch / 1_000_000
            visit_time = CHROME_EPOCH_START + timedelta(seconds=epoch_in_seconds)
            return visit_time.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            self.log_message(f"Error converting epoch: {e}")
            return "Invalid Epoch Time"

    def connect_to_db(self, db_path):
        """
        Establish a connection to the SQLite database.

        Args:
        db_path (str): The path to the database file.

        Returns:
        sqlite3.Connection: The database connection.
        """
        try:
            return sqlite3.connect(db_path)
        except sqlite3.Error as e:
            self.log_message(f"Database connection error: {e}")
            messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
            return None

    def open_database_file(self):
        """
        Open a file picker dialog to select a database file.
        """
        file_path = filedialog.askopenfilename(title="Select Chrome History Database", filetypes=[("All Files", "*.*")])
        if file_path:
            self.conn = self.connect_to_db(file_path)
            if self.conn:
                self.db_path = file_path
                self.log_message(f"Database loaded: {file_path}")
                messagebox.showinfo("Success", "Database loaded successfully.")

    def backup_database(self):
        """
        Create a backup of the current database.
        """
        if not self.db_path:
            self.log_message("No database loaded to backup.")
            messagebox.showwarning("No Database", "Please load a database first.")
            return

        self.backup_path = self.db_path + ".backup"
        try:
            shutil.copyfile(self.db_path, self.backup_path)
            self.log_message(f"Database backup created at: {self.backup_path}")
            messagebox.showinfo("Success", "Database backup created successfully.")
        except Exception as e:
            self.log_message(f"Error creating database backup: {e}")
            messagebox.showerror("Backup Error", f"Error creating database backup: {e}")

    def restore_database(self):
        """
        Restore the database from the backup.
        """
        if not self.backup_path or not os.path.exists(self.backup_path):
            self.log_message("No backup found to restore.")
            messagebox.showwarning("No Backup", "No backup found to restore.")
            return

        try:
            shutil.copyfile(self.backup_path, self.db_path)
            self.conn = self.connect_to_db(self.db_path)
            self.log_message(f"Database restored from backup: {self.backup_path}")
            messagebox.showinfo("Success", "Database restored successfully.")
        except Exception as e:
            self.log_message(f"Error restoring database: {e}")
            messagebox.showerror("Restore Error", f"Error restoring database: {e}")

    def modify_downloads(self):
        """
        Open a new window to modify the 'downloads' table.
        """
        if not self.conn:
            self.log_message("Database not loaded.")
            messagebox.showwarning("Database Not Loaded", "Please load the database file first.")
            return

        downloads_window = tk.Toplevel(self.root)
        downloads_window.title("Modify Downloads Table")
        downloads_window.geometry("800x400")

        # Create a treeview to display the downloads data
        downloads_tree = ttk.Treeview(downloads_window, columns=("Path", "Start Time", "End Time"), show="headings")
        downloads_tree.heading("Path", text="Path")
        downloads_tree.heading("Start Time", text="Start Time")
        downloads_tree.heading("End Time", text="End Time")
        downloads_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        def load_downloads_data():
            """
            Load data from the 'downloads' table.
            """
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT id, target_path, start_time, end_time FROM downloads")
                rows = cursor.fetchall()
                downloads_tree.delete(*downloads_tree.get_children())

                for row in rows:
                    start_time = self.epoch_to_human_readable(row[2])
                    end_time = self.epoch_to_human_readable(row[3])
                    downloads_tree.insert('', 'end', iid=row[0], values=(row[1], start_time, end_time))

                self.log_message(f"Downloads data loaded successfully. {len(rows)} rows fetched from database.")
            except sqlite3.Error as e:
                self.log_message(f"Error loading downloads data: {e}")
                messagebox.showerror("Database Error", f"Error loading downloads data: {e}")

        def edit_selected_row():
            """
            Edit the selected row in the downloads table.
            """
            selected_item = downloads_tree.selection()
            if not selected_item:
                messagebox.showwarning("No Row Selected", "Please select a row to edit.")
                return

            download_id = selected_item[0]
            values = downloads_tree.item(selected_item, 'values')
            current_path, current_start_time, current_end_time = values

            edit_window = tk.Toplevel(downloads_window)
            edit_window.title("Edit Download")
            edit_window.geometry("400x300")

            tk.Label(edit_window, text="Target Path:").pack(pady=5)
            path_entry = tk.Entry(edit_window, width=50)
            path_entry.insert(0, current_path)
            path_entry.pack(pady=5)

            tk.Label(edit_window, text="Start Time (YYYY-MM-DD HH:MM:SS):").pack(pady=5)
            start_time_entry = tk.Entry(edit_window, width=50)
            start_time_entry.insert(0, current_start_time)
            start_time_entry.pack(pady=5)

            tk.Label(edit_window, text="End Time (YYYY-MM-DD HH:MM:SS):").pack(pady=5)
            end_time_entry = tk.Entry(edit_window, width=50)
            end_time_entry.insert(0, current_end_time)
            end_time_entry.pack(pady=5)

            def save_changes():
                """
                Save changes to the database.
                """
                new_path = path_entry.get()
                new_start_time = start_time_entry.get()
                new_end_time = end_time_entry.get()

                try:
                    new_start_epoch = self.datetime_to_chrome_epoch(datetime.strptime(new_start_time, "%Y-%m-%d %H:%M:%S"))
                    new_end_epoch = self.datetime_to_chrome_epoch(datetime.strptime(new_end_time, "%Y-%m-%d %H:%M:%S"))

                    cursor = self.conn.cursor()
                    cursor.execute(
                        "UPDATE downloads SET target_path =?, start_time =?, end_time =? WHERE id =?",
                        (new_path, new_start_epoch, new_end_epoch, download_id)
                    )
                    self.conn.commit()

                    self.log_message(f"Row updated: ID={download_id}, Path={new_path}, Start={new_start_time}, End={new_end_time}")
                    load_downloads_data()
                    edit_window.destroy()
                except ValueError:
                    messagebox.showerror("Invalid Time Format", "Please enter valid date-time values in the format YYYY-MM-DD HH:MM:SS.")
                except sqlite3.Error as e:
                    self.log_message(f"Error updating downloads table: {e}")
                    messagebox.showerror("Database Error", f"Error saving changes: {e}")

            tk.Button(edit_window, text="Save Changes", command=save_changes).pack(pady=10)

        button_frame = tk.Frame(downloads_window)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit Selected Row", command=edit_selected_row)
        edit_button.pack(side=tk.LEFT, padx=10)

        load_downloads_data()

    def modify_history(self):
        """
        Open a new window to modify the 'history' table.
        """
        if not self.conn:
            self.log_message("Database not loaded.")
            messagebox.showwarning("Database Not Loaded", "Please load the database file first.")
            return

        history_window = tk.Toplevel(self.root)
        history_window.title("Modify History Table")
        history_window.geometry("800x400")

        history_tree = ttk.Treeview(history_window, columns=("URL", "Visit Time", "Title"), show="headings")
        history_tree.heading("URL", text="URL")
        history_tree.heading("Visit Time", text="Visit Time")
        history_tree.heading("Title", text="Title")
        history_tree.pack(fill=tk.BOTH, expand=True, pady=10)

        def load_history_data():
            """
            Load data from the 'urls' and 'visits' table.
            """
            try:
                cursor = self.conn.cursor()
                cursor.execute("""
                    SELECT urls.url, visits.visit_time, urls.title
                    FROM visits
                    JOIN urls ON visits.url = urls.id
                """)
                rows = cursor.fetchall()
                history_tree.delete(*history_tree.get_children())

                for row in rows:
                    visit_time = self.epoch_to_human_readable(row[1])
                    history_tree.insert('', 'end', values=(row[0], visit_time, row[2]))

                self.log_message(f"History data loaded successfully. {len(rows)} rows fetched from database.")
            except sqlite3.Error as e:
                self.log_message(f"Error loading history data: {e}")
                messagebox.showerror("Database Error", f"Error loading history data: {e}")

        def edit_selected_history_row():
            """
            Edit the selected row in the history table.
            """
            selected_item = history_tree.selection()
            if not selected_item:
                messagebox.showwarning("No Row Selected", "Please select a row to edit.")
                return

            visit_url = history_tree.item(selected_item, 'values')[0]
            current_visit_time = history_tree.item(selected_item, 'values')[1]

            edit_window = tk.Toplevel(history_window)
            edit_window.title("Edit History")
            edit_window.geometry("400x300")

            # Create a canvas and scrollbar for scrolling
            canvas = tk.Canvas(edit_window)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(edit_window, orient="vertical", command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill="y")

            canvas.configure(yscrollcommand=scrollbar.set)

            # Create a frame to hold the widgets and allow scrolling
            scrollable_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

            tk.Label(scrollable_frame, text="URL:").pack(pady=5)
            url_entry = tk.Entry(scrollable_frame, width=50)
            url_entry.insert(0, visit_url)
            url_entry.pack(pady=5)

            tk.Label(scrollable_frame, text="Visit Time (YYYY-MM-DD HH:MM:SS):").pack(pady=5)
            visit_time_entry = tk.Entry(scrollable_frame, width=50)
            visit_time_entry.insert(0, current_visit_time)
            visit_time_entry.pack(pady=5)

            def save_history_changes():
                """
                Save changes to the history table.
                """
                new_url = url_entry.get()
                new_visit_time = visit_time_entry.get()

                try:
                    new_visit_time_dt = datetime.strptime(new_visit_time, "%Y-%m-%d %H:%M:%S")
                    new_visit_epoch = self.datetime_to_chrome_epoch(new_visit_time_dt)

                    cursor = self.conn.cursor()
                    cursor.execute(
                        "UPDATE urls SET url =? WHERE url =?",
                        (new_url, visit_url)
                    )
                    cursor.execute(
                        "UPDATE visits SET visit_time =? WHERE url = (SELECT id FROM urls WHERE url =?)",
                        (new_visit_epoch, new_url)
                    )
                    self.conn.commit()

                    self.log_message(f"History updated: URL={new_url}, Visit Time={new_visit_time}")
                    load_history_data()
                    edit_window.destroy()
                except ValueError:
                    messagebox.showerror("Invalid Time Format", "Please enter a valid visit time in the format YYYY-MM-DD HH:MM:SS.")
                except sqlite3.Error as e:
                    self.log_message(f"Error updating history: {e}")
                    messagebox.showerror("Database Error", f"Error saving changes: {e}")

            tk.Button(scrollable_frame, text="Save Changes", command=save_history_changes).pack(pady=10)

            # Update the scrollable frame's scroll region
            scrollable_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        button_frame = tk.Frame(history_window)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit Selected Row", command=edit_selected_history_row)
        edit_button.pack(side=tk.LEFT, padx=10)

        load_history_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChromeDataModifier(root)
    root.mainloop()
