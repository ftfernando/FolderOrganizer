import os
import shutil
import logging
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import json


def load_config(config_file):
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as file:
        return json.load(file)


def setup_logging(log_folder):
    """Set up logging to capture detailed logs."""
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_filename = os.path.join(log_folder, f'file_organizer_{timestamp}.log')
    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging started.")


def backup_file(file_path, backup_folder):
    """Create a backup of the file before moving."""
    try:
        backup_path = os.path.join(backup_folder, os.path.basename(file_path))
        shutil.copy2(file_path, backup_path)
        logging.info(f"Backed up '{file_path}' to '{backup_path}'.")
        return backup_path
    except Exception as e:
        logging.error(f"Error backing up '{file_path}': {e}")
        return None


def process_directory(directory_path, extension_mapping, name_prefix_mapping, backup_folder, ignore_folders):
    """Process files in the directory based on extension and name prefix mappings."""
    if not os.path.exists(directory_path):
        logging.error(f"Directory '{directory_path}' does not exist.")
        return

    logging.info(f"Processing directory '{directory_path}'")

    for root, dirs, files in os.walk(directory_path):
        # Skip any root directory that is in the ignore_folders list
        if any(os.path.basename(root) in ignore_folders for ignore_folder in ignore_folders):
            continue

        for filename in files:
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1][1:].lower() if os.path.splitext(filename)[1] else ''
            file_name = os.path.splitext(filename)[0].lower()

            # Backup the file before moving
            backup_path = backup_file(file_path, backup_folder)
            if backup_path is None:
                continue

            moved = False
            # Check for name prefix matching
            for prefix, dest_folder in name_prefix_mapping.items():
                if file_name.startswith(prefix.lower()):
                    dest_folder_path = os.path.join(directory_path, dest_folder)
                    try:
                        if not os.path.exists(dest_folder_path):
                            os.makedirs(dest_folder_path)
                        dest_file_path = os.path.join(dest_folder_path, filename)
                        if os.path.exists(dest_file_path):
                            base, ext = os.path.splitext(filename)
                            counter = 1
                            while os.path.exists(dest_file_path):
                                dest_file_path = os.path.join(dest_folder_path, f"{base}_{counter}{ext}")
                                counter += 1
                        shutil.move(file_path, dest_file_path)
                        logging.info(f"Moved '{filename}' to '{dest_folder_path}' based on name prefix.")
                        moved = True
                        break
                    except Exception as e:
                        logging.error(f"Error moving '{filename}' to '{dest_folder_path}': {e}")
                        break

            # If not moved by name prefix, check for extension matching
            if not moved:
                for extensions, dest_folder in extension_mapping.items():
                    if file_extension in extensions:
                        dest_folder_path = os.path.join(directory_path, dest_folder)
                        try:
                            if not os.path.exists(dest_folder_path):
                                os.makedirs(dest_folder_path)
                            dest_file_path = os.path.join(dest_folder_path, filename)
                            if os.path.exists(dest_file_path):
                                base, ext = os.path.splitext(filename)
                                counter = 1
                                while os.path.exists(dest_file_path):
                                    dest_file_path = os.path.join(dest_folder_path, f"{base}_{counter}{ext}")
                                    counter += 1
                            shutil.move(file_path, dest_file_path)
                            logging.info(f"Moved '{filename}' to '{dest_folder_path}' based on extension.")
                            moved = True
                            break
                        except Exception as e:
                            logging.error(f"Error moving '{filename}' to '{dest_folder_path}': {e}")
                            break

    logging.info(f"Completed processing directory '{directory_path}'.")


def browse_folder():
    """Open a dialog to select the main folder."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        main_folder.set(folder_selected)
        logging.info(f"Selected folder: {folder_selected}")


def start_processing():
    """Start processing the selected folder."""
    folder = main_folder.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder.")
        return

    # Define the backup folder inside the main folder
    backup_folder = os.path.join(folder, 'backup_folder')
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Process files in the selected folder
    process_directory(folder, extension_mapping, name_prefix_mapping, backup_folder, ignore_folders)
    messagebox.showinfo("Info", "Processing completed.")


# Load the configuration file
config = load_config('controller.json')
extension_mapping = {tuple(ext.split(',')): folder for ext, folder in config['extension_mapping'].items()}
name_prefix_mapping = config['name_prefix_mapping']
ignore_folders = config['ignore_folders']
log_folder = config['log_folder']

# Set up logging
setup_logging(log_folder)

# Create the GUI
root = tk.Tk()
root.title("File Organizer | By: Fernando Thompson")

# Set the size of the window (width x height)
root.geometry("400x200")

# Create and pack widgets
tk.Label(root, text="Main Folder:").pack(padx=10, pady=5)
main_folder = tk.StringVar()
tk.Entry(root, textvariable=main_folder, width=50).pack(padx=10, pady=5)

tk.Label(root, text="Log Folder:").pack(padx=10, pady=5)
log_folder_var = tk.StringVar(value=log_folder)
tk.Entry(root, textvariable=log_folder_var, width=50).pack(padx=10, pady=5)

tk.Button(root, text="Browse Folder", command=browse_folder).pack(padx=10, pady=5)
tk.Button(root, text="Start Processing", command=start_processing).pack(padx=10, pady=10)

root.mainloop()
