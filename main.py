import tkinter as tk

ablak = tk.Tk()
ablak.title("Autóverseny - SzL")
ablak.geometry("900x650")
ablak.resizable(False, False)

vaszon = tk.Canvas(
    ablak,
    width=900,
    height=650,
    bg="green"
)

vaszon.pack()

vaszon.create_rectangle(
    100, 80, 800, 570,
    fill="gray",
    outline="white",
    width=4
)

vaszon.create_rectangle(
    250, 200, 650, 450,
    fill="green",
    outline="white",
    width=4
)

vaszon.create_line(
    100, 325, 250, 325,
    fill="white",
    width=4,
    dash=(10, 5)
)

vaszon.create_text(
    450, 325,
    text="VERSENYPÁLYA",
    fill="white",
    font=("Arial", 20, "bold")
)

vaszon.create_rectangle(
    145, 310, 195, 340,
    fill="red",
    outline="black",
    width=2,
    tags="auto"
)

vaszon.create_rectangle(
    155, 315, 185, 335,
    fill="lightblue",
    outline="black",
    tags="auto"
)

def autoMozgatasa(irany):
    sebesseg = 10

    if irany == "bal":
        vaszon.move("auto", -sebesseg, 0)
    elif irany == "jobb":
        vaszon.move("auto", sebesseg, 0)
    elif irany == "fel":
        vaszon.move("auto", 0, -sebesseg)
    elif irany == "le":
        vaszon.move("auto", 0, sebesseg)


def billentyuKezeles(esemeny):
    if esemeny.keysym == "Left":
        autoMozgatasa("bal")
    elif esemeny.keysym == "Right":
        autoMozgatasa("jobb")
    elif esemeny.keysym == "Up":
        autoMozgatasa("fel")
    elif esemeny.keysym == "Down":
        autoMozgatasa("le")


ablak.bind("<KeyPress>", billentyuKezeles)

ablak.mainloop()

ablak.mainloop()