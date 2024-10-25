import PySimpleGUI as sg

# Penentuan tema dan warna teks
sg.theme("DarkPurple1")  # Tema
sg.theme_text_color("#00FFFF")  # Warna teks default

# Definisi window dan layout
window = sg.Window(title="Profile",
                   layout=[
                       [sg.Text("FTI UNISKA ", font=("Helvetica", 24), text_color="#FFFFFF")],
                       [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ", font=("Courier", 18, "italic bold underline"))],
                       [sg.Text("UNISKA MAB BANJARMASIN", text_color="#76EEC6")]
                   ],
                   size=(430, 200),
                   font=("Times", 18))

# Menampilkan window
window.read()

# Menutup window setelah ditutup
window.close()
