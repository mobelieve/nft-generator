import random
import os
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, messagebox

# Create output directory for NFTs
output_dir = 'nft_collection'
os.makedirs(output_dir, exist_ok=True)

class NFTGenerator:
    def __init__(self, master):
        self.master = master
        master.title("NFT Generator")

        # Layer directories
        self.background_dir = ""
        self.body_dir = ""
        self.clothes_dir = ""
        self.accessory_dir = ""

        # GUI Elements
        self.label = tk.Label(master, text="NFT Generator", font=("Arial", 16))
        self.label.pack(pady=10)

        self.select_background_button = tk.Button(master, text="Select Background Images Folder", command=self.select_background_folder)
        self.select_background_button.pack(pady=5)

        self.select_body_button = tk.Button(master, text="Select Body Images Folder", command=self.select_body_folder)
        self.select_body_button.pack(pady=5)

        self.select_clothes_button = tk.Button(master, text="Select Clothes Images Folder", command=self.select_clothes_folder)
        self.select_clothes_button.pack(pady=5)

        self.select_accessory_button = tk.Button(master, text="Select Accessories Images Folder", command=self.select_accessory_folder)
        self.select_accessory_button.pack(pady=5)

        self.num_nfts_label = tk.Label(master, text="Number of NFTs to generate:")
        self.num_nfts_label.pack(pady=5)

        self.num_nfts_entry = tk.Entry(master)
        self.num_nfts_entry.pack(pady=5)

        self.custom_text_label = tk.Label(master, text="Custom Text for NFTs:")
        self.custom_text_label.pack(pady=5)

        self.custom_text_entry = tk.Entry(master)
        self.custom_text_entry.pack(pady=5)

        self.generate_button = tk.Button(master, text="Generate NFTs", command=self.generate_nfts)
        self.generate_button.pack(pady=10)

    def select_background_folder(self):
        self.background_dir = filedialog.askdirectory()
        if self.background_dir:
            messagebox.showinfo("Selected Folder", f"Background images folder: {self.background_dir}")

    def select_body_folder(self):
        self.body_dir = filedialog.askdirectory()
        if self.body_dir:
            messagebox.showinfo("Selected Folder", f"Body images folder: {self.body_dir}")

    def select_clothes_folder(self):
        self.clothes_dir = filedialog.askdirectory()
        if self.clothes_dir:
            messagebox.showinfo("Selected Folder", f"Clothes images folder: {self.clothes_dir}")

    def select_accessory_folder(self):
        self.accessory_dir = filedialog.askdirectory()
        if self.accessory_dir:
            messagebox.showinfo("Selected Folder", f"Accessories images folder: {self.accessory_dir}")

    def generate_nfts(self):
        try:
            num_nfts = int(self.num_nfts_entry.get())
            custom_text = self.custom_text_entry.get()
            for i in range(1, num_nfts + 1):
                self.generate_nft(i, custom_text)
            messagebox.showinfo("Complete", f"Generated {num_nfts} unique NFTs!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def get_random_image_from_folder(self, folder_path):
        images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not images:
            messagebox.showerror("Error", f"No images found in {folder_path}!")
            return None
        return os.path.join(folder_path, random.choice(images))

    def generate_nft(self, nft_id, custom_text):
        # Select random images from each layer
        background_img_path = self.get_random_image_from_folder(self.background_dir)
        body_img_path = self.get_random_image_from_folder(self.body_dir)
        clothes_img_path = self.get_random_image_from_folder(self.clothes_dir)
        accessory_img_path = self.get_random_image_from_folder(self.accessory_dir)

        if not background_img_path:
            return
        
        # Load and combine images
        background_img = Image.open(background_img_path).convert("RGBA")

        # Load and overlay additional layers
        if body_img_path:
            body_img = Image.open(body_img_path).convert("RGBA")
            background_img = Image.alpha_composite(background_img, body_img)
        
        if clothes_img_path:
            clothes_img = Image.open(clothes_img_path).convert("RGBA")
            background_img = Image.alpha_composite(background_img, clothes_img)

        if accessory_img_path:
            accessory_img = Image.open(accessory_img_path).convert("RGBA")
            background_img = Image.alpha_composite(background_img, accessory_img)

        # Draw custom text on the NFT image
        draw = ImageDraw.Draw(background_img)
        font = ImageFont.load_default()
        text_position = (10, 10)  # Position for the text
        draw.text(text_position, custom_text, fill="white", font=font)

        # Save the final NFT image
        background_img.save(os.path.join(output_dir, f"nft_{nft_id}.png"))

# Main code to run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    nft_generator = NFTGenerator(root)
    root.mainloop()
