import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Lista de preguntas y respuestas con pistas
from Preguntas import questions

# Variables para la puntuación
global loop
loop = None
j1 = ""
j2 = ""
j1_score = 0
j2_score = 0
current_question_index = 0
current_player = 1

# Reiniciar juego
def reiniciar():
    global j1, j2, j1_score, j2_score, current_question_index, current_player, loop

    j1 = ""
    j2 = ""
    j1_score = 0
    j2_score = 0
    current_question_index = 0
    current_player = 1

    gif2_label.pack_forget()
    result_label.pack_forget()
    winner_label.pack_forget()
    reinicio_boton.pack_forget()

    if loop is not None:
        window.after_cancel(loop)
        loop = None

    gif1_label.pack(pady=10)
    jugador_1.pack(pady=10)
    nombre_1.pack(pady=10)
    jugador_2.pack(pady=10)
    nombre_2.pack(pady=10)
    start_button.pack(pady=20)
    
    nombre_1.delete(0, tk.END)
    nombre_2.delete(0, tk.END)
    
    animation1()

# Función para verificar la respuesta
def respuesta(selected_option):
    global current_question_index, current_player, j1_score, j2_score

    correct_answer = questions[current_question_index]["answer"]
    if selected_option == correct_answer:
        if current_player == 1:
            j1_score += 1
        else:
            j2_score += 1

    current_question_index += 1
    if current_question_index >= len(questions):
        ganador()
    else:
        current_player = 2 if current_player == 1 else 1
        pregunta()

# Función para cargar una pregunta
def pregunta():
    global current_question_index, j1, j2, current_player
    question_label.config(text=questions[current_question_index]["question"])
    for i, option in enumerate(questions[current_question_index]["options"]):
        option_buttons[i].config(text=option, state=tk.NORMAL)
    if current_player == 1:
        turn_label.config(text="Turno de " + j1)
    else:
        turn_label.config(text="Turno de " + j2)
    hint_texto.config(text="")

# Función para mostrar el ganador
def ganador():
    for button in option_buttons:
        button.pack_forget()
    question_label.pack_forget()
    turn_label.pack_forget()
    hint_texto.pack_forget()
    pista_boton.pack_forget()

    result_label.pack(pady=20)
    result_label.config(text=f"Puntuación de {j1}: {j1_score}\nPuntuación de {j2}: {j2_score}")

    if j1_score > j2_score:
        winner = f"¡{j1} tu ganas!"
    elif j2_score > j1_score:
        winner = f"¡{j2} tu ganas!"
    else:
        winner = "¡Es un empate!"
    
    winner_label.pack(pady=20)
    winner_label.config(text=winner)

    reinicio_boton.pack(pady=10)

# Función para mostrar la pista
def pista():
    hint_texto.config(text=questions[current_question_index]["hint"])

# Función para iniciar el juego
def inicio():
    global nombre_1, nombre_2, j1, j2

    j1 = nombre_1.get()
    j2 = nombre_2.get()

    nombre_1.pack_forget()
    nombre_2.pack_forget()
    jugador_1.pack_forget()
    jugador_2.pack_forget()
    
    start_button.pack_forget()
    gif1_label.pack_forget()

    gif2_label.pack(pady=5)
    turn_label.pack(pady=5)
    question_label.pack(pady=20)
    for button in option_buttons:
        button.pack(pady=5)
    pista_boton.pack(pady=10)
    hint_texto.pack(pady=10)
    pregunta()
    animation2()

# Configuración de la ventana principal
window = tk.Tk()
window.config(bg="#f7f7f7")
window.geometry("700x650")
window.resizable(False, False)
window.title("Quizazul")

# Crear etiqueta para la pregunta
question_label = tk.Label(window, text="", wraplength=700, bg="#f7f7f7", font=("Comic Sans MS", 18, "bold"))

# Cargar y procesar el GIF 1
gif1_path = "SBH4.gif"
gif1_open = Image.open(gif1_path)
frames1 = gif1_open.n_frames
imageObjects1 = []
for i in range(frames1):
    gif1_open.seek(i)
    frame1 = gif1_open.copy().resize((300, 300))
    foto_imagen1 = ImageTk.PhotoImage(frame1)
    imageObjects1.append(foto_imagen1)

# Cargar y procesar el GIF 2 
gif_path = "SBH8.gif"
gif_open = Image.open(gif_path)
frames = gif_open.n_frames
imageObjects = []
for j in range(frames):
    gif_open.seek(j)
    frame = gif_open.copy().resize((100, 100))
    foto_imagen = ImageTk.PhotoImage(frame)
    imageObjects.append(foto_imagen)


# Función para la animación de los GIFS
def animation1(current_frame=0):
    if current_frame < frames1:
        image1 = imageObjects1[current_frame]
        gif1_label.configure(image=image1)
        current_frame += 1
        window.after(100, lambda: animation1(current_frame))

def animation2(current_frame2=0):
    global loop
    image2 = imageObjects[current_frame2]
    gif2_label.configure(image=image2)
    current_frame2 += 1
    if current_frame2 == frames:
        current_frame2 = 0
    loop = window.after(100, lambda: animation2(current_frame2))


# Etiqueta para mostrar los GIFS
gif1_label = tk.Label(window, image="")
gif1_label.pack(pady=10)

gif2_label = tk.Label(window, image="")

# Espacio para los nombres de los jugadores
jugador_1 = tk.Label(window, text="Nombre del jugador 1", font=("Comic Sans MS", 12), bg="#f7f7f7")
jugador_1.pack(pady=10)
nombre_1 = tk.Entry(window, font=("Comic Sans Ms", 12))
nombre_1.pack(pady=10)

jugador_2 = tk.Label(window, text="Nombre del jugador 2", font=("Comic Sans MS", 12), bg="#f7f7f7")
jugador_2.pack(pady=10)
nombre_2 = tk.Entry(window, font=("Comic Sans Ms", 12))
nombre_2.pack(pady=10)

# Botón de inicio
start_button = tk.Button(window, text="¡Empezar!", font=("Comic Sans MS", 16, "bold"), bg="#ffdd57", fg="#333", command=inicio)
start_button.pack(pady=20)

# Botón de pista
pista_boton = tk.Button(window, text="¿Necesitas una pista?", font=("Comic Sans MS", 16, "bold"), bg="#ffdd57", fg="#333", command=pista)

# Estilo de los botones
button_style = {"font": ("Comic Sans MS", 14, "bold"), "bg": "#57ffdd", "fg": "#333", "width": 30, "border": 5, "relief": tk.RAISED}

# Botones de opciones
option_buttons = []
for i in range(4):
    button = tk.Button(window, text="", **button_style, command=lambda i=i: respuesta(questions[current_question_index]["options"][i][0]))
    option_buttons.append(button)

# Etiqueta de turno
turn_label = tk.Label(window, text="", font=("Comic Sans MS", 16, "bold"), bg="#f7f7f7")

# Etiqueta de pista
hint_texto = tk.Label(window, text="", wraplength=500, font=("Comic Sans MS", 16, "bold"), bg="#f7f7f7")

# Etiquetas de resultados
result_label = tk.Label(window, text="", font=("Comic Sans MS", 18, "bold"), bg="#f7f7f7")
winner_label = tk.Label(window, text="", font=("Comic Sans MS", 20, "bold"), bg="#f7f7f7", fg="#ff5733")

# Boton de reinicio
reinicio_boton = tk.Button(window, text="¡Jugar otra vez!", font=("Comic Sans MS", 16, "bold"), bg="#ffdd57", fg="#333", command=reiniciar)

# Iniciar animación
animation1()

# Iniciar ventana principal
window.mainloop()
