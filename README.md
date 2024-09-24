NFT Generator With GUI






This is a simple Python-based NFT generator that allows users to create thousands of unique NFTs by layering images. The project uses a graphical user interface (GUI) built with Tkinter, allowing users to easily select different image folders for layers like background, body, clothes, and accessories. Custom text and other options are available to make each NFT unique.

Features
Layered Image Generation: Combine background, body, clothes, and accessory images.
Custom Text: Add custom text to each NFT image.
GUI Interface: Simple and user-friendly interface for easy use.
Randomized NFT Creation: Generate thousands of unique NFTs with random image combinations.
Table of Contents
Installation
Usage
Features
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/mobelieve/nft-generator.git
Navigate to the project directory:

bash
Copy code
cd nft-generator
Install dependencies: Ensure that you have Python installed (preferably Python 3.7 or later). Then, install the required dependencies:

bash
Copy code
pip install Pillow
Tkinter is part of the Python standard library, so no additional installation is required for it.

Run the program:

bash
Copy code
python nft_generator_gui.py
Usage
Open the Application:

After running the program, a GUI will appear.
Select Image Folders:

Use the buttons to select folders for Background, Body, Clothes, and Accessories.
Set the Number of NFTs:

Enter how many NFTs you want to generate in the provided field.
Add Custom Text (Optional):

If you want to add custom text to each NFT, type it in the text field.
Generate NFTs:

Click the Generate NFTs button to start creating your unique NFTs. The images will be saved in the nft_collection folder inside the project directory.
Features
Multiple Layers: The generator uses random images from different layers (background, body, clothes, accessories) to create unique NFTs.
Customizable Text: You can add custom text to each NFT, which will appear at the top-left of the image.
Randomization: Each NFT is created by randomly selecting images from the available image layers, ensuring uniqueness.
User-Friendly GUI: A simple graphical interface allows you to easily configure the NFT generation process.

This project is open-source and available under the MIT License.


Contributions are welcome! Please create a pull request or submit an issue if you have suggestions for improvements.

