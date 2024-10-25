import PySimpleGUI as sg

# Mengatur tema dan warna teks
sg.theme("DarkPurple1")
sg.theme_text_color("#00FFFF")

# Mendefinisikan layout dan properti window
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                   size=(430, 200),
                   font=("Times", 18))

# Menampilkan window
window.read()
window.close()