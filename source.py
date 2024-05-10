# script for changing wallpaper
# 5.24
# A Higgins
import os, os.path, time, random

def set_wallpaper():
    """sets the wallpaper via os.system"""
    file = 'spring.jpg'
    file2 = 'fall.jpg'
    file_path = '/home/aurelius/Pictures/Wallpapers/'

    theme = input("Please select either light or dark theme:")
    # if/else statement for light or dark theme
    if theme == "light":
        command = 'gsettings set org.gnome.desktop.background picture-uri-dark file:' + file_path + file
        os.system(command)

    elif theme == "dark":
        command = 'gsettings set org.gnome.desktop.background picture-uri-dark file:' + file_path + file2
        os.system(command)

set_wallpaper()
file_path = '/home/aurelius/Pictures/Wallpapers/'

print(len(file_path))