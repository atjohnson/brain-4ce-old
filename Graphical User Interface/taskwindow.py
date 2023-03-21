import tkinter as tk


def CreateShape(canvas, x1,x2,y1,y2):

    canvas.create_oval(x1,x2,y1,y2, outline='black', width=2)



def tWindow():

    window = tk.Tk()
    window.title("Brain4ce Menu")

    #Set window size and pos

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 600
    window_height = 400
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_height - window_height) // 2

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_pos, y_pos))




    canvas = tk.Canvas(window, width=450, height=450)
    canvas.pack()

    CreateShape(canvas, 25, 25, 75, 75)
    CreateShape(canvas, 100, 25, 150, 75)
    CreateShape(canvas, 175, 25, 225, 75)
    CreateShape(canvas, 25, 100, 75, 150)
    CreateShape(canvas, 100, 100, 150, 150)
    CreateShape(canvas, 175, 100, 225, 150)

    canvas.scale("all", 0, 0, 2, 2)
    canvas.place(relx=0.45, rely=0.05, anchor='n')
    canvas.create_text(100, 100, text="1", fill="black", font=('Helvetica 25 bold'))
    canvas.create_text(250, 100, text="2", fill="black", font=('Helvetica 25 bold'))   
    canvas.create_text(400, 100, text="3", fill="black", font=('Helvetica 25 bold'))
    canvas.create_text(100, 250, text="4", fill="black", font=('Helvetica 25 bold'))
    canvas.create_text(250, 250, text="5", fill="black", font=('Helvetica 25 bold'))
    canvas.create_text(400, 250, text="6", fill="black", font=('Helvetica 25 bold'))        