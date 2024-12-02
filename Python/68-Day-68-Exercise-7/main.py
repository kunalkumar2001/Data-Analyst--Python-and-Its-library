# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.
import os

def clear_folder_clutter(folder_path):
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    for i, file_name in enumerate(png_files, start=1):
        new_file_name = str(i) + '.png'
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

# Provide the folder path where you want to clear the clutter
folder_path = 'path_to_your_folder'
# clear_folder_clutter(folder_path)png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats.