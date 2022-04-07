
from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SESSIONS = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN]
REPS = 0
MARKS = ""
timer = None
SESSIONPART = 0
# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_count():
    global REPS
    REPS += 1
    print(REPS)
    if REPS in (1, 3, 5, 7):
        timer_label.config(text = "Work", fg= GREEN)
        count_down(WORK_MIN * 60)

    elif REPS in (2 , 4 , 6 ):
        global SESSIONPART
        SESSIONPART += 1
        messagebox.showinfo(title=f"Important message", message=f"Work session {SESSIONPART} Done")
        take_break = messagebox.askyesno(title="A break is coming", message="Do you want to start the break now")

        if take_break == True:
            timer_label.config(text= "Break", fg= PINK)
            count_down(SHORT_BREAK_MIN * 60)

    elif REPS == 8:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count_number):
    """need a number of timer count"""
    count_min = math.floor(count_number / 60)
    count_sec = count_number % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count_number > 0:
        global timer
        timer = window.after(1000, count_down, count_number - 1)

    else:
        timer_count()
        global check_mark

        if REPS in (2, 4, 6, 8):
            global MARKS
            MARKS += "✓"
            check_mark.config(text= MARKS)

        else:
            check_mark.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

# construct a tk class
window = Tk()
window.title("Pomomdoro" )
window.config(padx=100, pady=50, bg=YELLOW)


# construct a canvas class to setup my image
canvas = Canvas(width=200, height=223)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)


# create labels

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "italic"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 18, "italic"), bg=YELLOW)
check_mark.grid(column=1, row=3)


# create button object

start_button = Button(text="Start", highlightthickness=0, command=timer_count)
start_button.grid(column=0, row=2)

reset = Button(text="Reset", command=time_reset)
reset.grid(column=2, row=2)



window.mainloop()
