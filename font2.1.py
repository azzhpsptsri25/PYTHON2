import PySimpleGUI as sg

# Set the theme and text color
sg.theme("DarkPurple1")
sg.theme_text_color("#00FFFF")

# Define the window layout and properties
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA ")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                   size=(430, 200),
                   font=("Times", 18))

# Create and display the window
window()
window.close()