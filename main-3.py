from tkinter import *
import math

root = Tk()
root.title('brianalanreeves.com - Bore Calculator')
root.iconbitmap('./my_icon.ico')
root.geometry("500x400")


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def bore():
    if stroke_length_entry.get() and num_cylinders_entry.get() and cid_displacement_entry.get():
        # Get data entry and convert to numbers
        stroke_length = float(stroke_length_entry.get())
        numcyl = int(num_cylinders_entry.get())
        engine_disp = float(cid_displacement_entry.get())
        # Calculate Bore Diameter
        # Calculate Individual Cylinder Volume
        cyl_vol = engine_disp / numcyl
        # Calculate Circular Area from Volume and Stroke
        cir_area = cyl_vol / stroke_length
        # Calculate Cubic inch displacement for engine
        bore_diameter = (math.sqrt(cir_area / math.pi)) * 2
        # Format Bore Diameter
        bore_diameter = f"{bore_diameter:,.4f}"
        # Output CID to Display
        bore_diameter_label.config(text=f"Bore Diameter: {bore_diameter}")

    else:
        bore_diameter_label.config(text="You forgot to enter required info!!!")


label_frame = LabelFrame(root, text="Engine Bore Dia Calculator")
label_frame.pack(pady=30)

frame = Frame(label_frame)
frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
stroke_length_label = Label(frame, text="Stroke Length")
stroke_length_entry = Entry(frame, font=("Helvetica", 18))

num_cylinders_label = Label(frame, text="Number of Cylinders")
num_cylinders_entry = Entry(frame, font=("Helvetica", 18))

cid_displacement_label = Label(frame, text="Cubic Inch Displacement")
cid_displacement_entry = Entry(frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
stroke_length_label.grid(row=0, column=0)
stroke_length_entry.grid(row=0, column=1)

num_cylinders_label.grid(row=2, column=0)
num_cylinders_entry.grid(row=2, column=1, pady=20)

cid_displacement_label.grid(row=3, column=0)
cid_displacement_entry.grid(row=3, column=1)

# Button
button = Button(label_frame, text="Calculate Bore", command=bore)
button.pack(pady=20)

# Answer Label
bore_diameter_label = Label(root, text="", font=("Helvetica", 18))
bore_diameter_label.pack(pady=20)

root.mainloop()
