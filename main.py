from tkinter import *
import math

root = Tk()
root.title('brianalanreeves.com - CID Calculator')
root.iconbitmap('./my_icon.ico')
root.geometry("500x400")


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def displacement():
    if bore_diameter_entry.get() and stroke_length_entry.get() and num_cylinders_entry.get():
        # Get data entry and convert to numbers
        bore = float(bore_diameter_entry.get())
        stroke = float(stroke_length_entry.get())
        numcyl = int(num_cylinders_entry.get())
        # Calculate CID
        # Calculate Circular Area from Diameter
        cir_area = ((bore / 2) ** 2) * math.pi
        # Calculate Cylinder Volume
        cyl_vol = cir_area * stroke
        # Calculate Cubic inch displacement for engine
        engine_disp = cyl_vol * numcyl
        # Format CID
        engine_disp = f"{engine_disp:,.2f}"
        # Output CID to Display
        displacement_label.config(text=f"CI Displacement: {engine_disp}")

    else:
        displacement_label.config(text="You forgot to enter required info!!!")


label_frame = LabelFrame(root, text="Engine Displacement Calculator")
label_frame.pack(pady=30)

frame = Frame(label_frame)
frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
bore_diameter_label = Label(frame, text="Bore Diameter")
bore_diameter_entry = Entry(frame, font=("Helvetica", 18))

stroke_length_label = Label(frame, text="Stroke Length")
stroke_length_entry = Entry(frame, font=("Helvetica", 18))

num_cylinders_label = Label(frame, text="Number of Cylinders")
num_cylinders_entry = Entry(frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
bore_diameter_label.grid(row=0, column=0)
bore_diameter_entry.grid(row=0, column=1)

stroke_length_label.grid(row=1, column=0)
stroke_length_entry.grid(row=1, column=1, pady=20)

num_cylinders_label.grid(row=2, column=0)
num_cylinders_entry.grid(row=2, column=1)

# Button
button = Button(label_frame, text="Calculate CID", command=displacement)
button.pack(pady=20)

# Label
displacement_label = Label(root, text="", font=("Helvetica", 18))
displacement_label.pack(pady=20)

root.mainloop()
