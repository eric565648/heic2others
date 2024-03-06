import tkinter as tk
from tkinter import filedialog, messagebox
from pillow_heif import HeifImagePlugin
from PIL import Image

def convert_heic_to_jpg(input_path, output_path):
    # Open the HEIC file directly with Pillow thanks to heif-image-plugin
    image = Image.open(input_path)
    # image = pillow_heif.open_heif(input_path, convert_hdr_to_8bit=False, bgr_mode=True)
    image.show()
    
    # Save the image as JPG
    image.convert('RGB').save(output_path, "JPEG", subsampling=0, quality=95)

def open_file_dialog():
    # Allow user to select a HEIC file
    filepath = filedialog.askopenfilenames(title="Select HEIC File",
                                           filetypes=(("HEIC files", "*.heic"), ("All files", "*.*")))
    return filepath

def save_file_dialog(filename):
    # Allow user to select save location with predefined filename
    fpath = filedialog.asksaveasfilename(defaultextension=".jpg",
                                         initialfile=filename,
                                         filetypes=[("JPEG", "*.jpg"), ("All files", "*.*")])
    return fpath

def convert_files():
    files = open_file_dialog()
    for file_path in files:
        output_path = save_file_dialog(file_path.split('/')[-1].replace('.heic', '.jpg'))
        if output_path:
            convert_heic_to_jpg(file_path, output_path)
            messagebox.showinfo("Success", f"File saved: {output_path}")

# Create the GUI window
root = tk.Tk()
root.title("HEIC to JPG Converter")

# Create and pack the convert button
convert_button = tk.Button(root, text="Convert HEIC to JPG", command=convert_files)
convert_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
