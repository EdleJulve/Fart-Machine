# IMPORTS

import tkinter as tk
import winsound
import os

os.chdir(os.path.dirname(__file__))

# FART COUNTER

fart_count = 0
def update_counter_label():
    counter_label.config(text=f"Pedos: {fart_count}")

# FUCTIONS

def play_fart(filename):
    

    if filename is None:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        return
    if os.path.exists(filename):
        winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        print("No encontré:", filename)
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

 # COUNTING FUNCTIONALITY
    global fart_count
    fart_count += 1
    print("💨 Pedo nro:", fart_count)
    update_counter_label()

def update_counter_label():
    counter_label.config(text=f"Pedos: {fart_count}")
	

# VENTANA ---> SETUP

root = tk.Tk()   #THIS CREATES THE WINDOW
root.title('Fart Machine 1.0') #THIS SETS THE TITLE OF THE WINDOW
root.geometry('300x250') #THIS SETS THE SIZE OF THE WINDOW
root.configure(bg='brown') #THIS SETS THE BACKGROUND COLOR OF THE WINDOW

#TITLE ---> SETUP
title_label = tk.Label(root, text='💩 Machine 1.0', font=('Segoe UI Emoji', 20, 'bold'), bg='brown')
title_label.pack(pady=10)



# BUTTONS --->FRAME
counter_label = tk.Label(root, text="Farts: 0",font=("Segoe UI", 14, "bold"), bg="#E6C9A8", fg="#553311")
counter_label.pack(pady=5)

buttons_frame = tk.Frame(root, bg='brown')
buttons_frame.pack(pady=20)

# BUTTONS - SOUND - SETUP

btn1 = tk.Button(buttons_frame, text='💩 1', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart1.wav'))
btn2 = tk.Button(buttons_frame, text='😆 2', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart2.wav'))
btn3 = tk.Button(buttons_frame, text='🤎 3', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart3.wav'))
btn4 = tk.Button(buttons_frame, text='🦨 4', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart4.wav'))
btn5 = tk.Button(buttons_frame, text='💨 5', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart5.wav'))
btn6 = tk.Button(buttons_frame, text='💥 6', font=("Segoe UI Emoji", 12), bg='#C19A6B', command=lambda: play_fart('fart6.wav'))

# pack/grid the buttons into the frame

btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3.grid(row=0, column=2, padx=5, pady=5)
btn4.grid(row=1, column=0, padx=5, pady=5)
btn5.grid(row=1, column=1, padx=5, pady=5)
btn6.grid(row=1, column=2, padx=5, pady=5)

#THIS KEEPS THE WINDOW OPEN

root.mainloop() 