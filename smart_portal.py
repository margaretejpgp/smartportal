import os
import json
import ctypes
from tkinter import Tk, filedialog, colorchooser, messagebox

class SmartPortal:
    def __init__(self):
        self.theme = {
            "background_color": "#FFFFFF",
            "text_color": "#000000",
            "accent_color": "#FF5733"
        }
        self.config_file = "theme_config.json"

    def load_theme(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.theme = json.load(file)
            print(f"Loaded theme: {self.theme}")
        else:
            print("No theme configuration found. Using default theme.")

    def save_theme(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.theme, file, indent=4)
        print("Theme saved successfully.")

    def choose_color(self, color_type):
        color_code = colorchooser.askcolor(title=f"Choose {color_type} Color")[1]
        if color_code:
            self.theme[f"{color_type}_color"] = color_code
            print(f"Selected {color_type} color: {color_code}")

    def apply_theme(self):
        # Apply background color
        bg_color = self.theme["background_color"]
        ctypes.windll.user32.SystemParametersInfoW(20, 0, bg_color, 0)
        print(f"Applied background color: {bg_color}")

        # Note: Applying text and accent colors would require more complex handling
        # such as modifying registry values or using external tools. This is a placeholder.

    def start(self):
        self.load_theme()
        root = Tk()
        root.withdraw()
        while True:
            print("\nSmartPortal - Theme Customizer")
            print("1. Choose Background Color")
            print("2. Choose Text Color")
            print("3. Choose Accent Color")
            print("4. Apply Theme")
            print("5. Save Theme")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.choose_color("background")
            elif choice == '2':
                self.choose_color("text")
            elif choice == '3':
                self.choose_color("accent")
            elif choice == '4':
                self.apply_theme()
            elif choice == '5':
                self.save_theme()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    portal = SmartPortal()
    portal.start()