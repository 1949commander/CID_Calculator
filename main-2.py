from tkinter import *
import math

root = Tk()
root.title('brianalanreeves.com - Stroke Calculator')
root.iconbitmap('./my_icon.ico')
root.geometry("500x400")


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def stroke():
    if bore_diameter_entry.get() and num_cylinders_entry.get() and cid_displacement_entry.get():
        # Get data entry and convert to numbers
        bore = float(bore_diameter_entry.get())
        numcyl = int(num_cylinders_entry.get())
        engine_disp = float(cid_displacement_entry.get())
        # Calculate CID
        # Calculate Circular Area from Diameter
        cir_area = ((bore / 2) ** 2) * math.pi
        # Calculate Cubic inch displacement for engine
        cyl_vol = engine_disp / numcyl
        # Calculate Cylinder Volume
        stroke = cyl_vol / cir_area
        # Format Stroke
        stroke = f"{stroke:,.4f}"
        # Output CID to Display
        stroke_label.config(text=f"Stroke Length: {stroke}")

    else:
        stroke_label.config(text="You forgot to enter required info!!!")


label_frame = LabelFrame(root, text="Engine Stroke Length Calculator")
label_frame.pack(pady=30)

frame = Frame(label_frame)
frame.pack(pady=10, padx=20)

# Define Labels and Entry Boxes
bore_diameter_label = Label(frame, text="Bore Diameter")
bore_diameter_entry = Entry(frame, font=("Helvetica", 18))

num_cylinders_label = Label(frame, text="Number of Cylinders")
num_cylinders_entry = Entry(frame, font=("Helvetica", 18))

cid_displacement_label = Label(frame, text="Cubic Inch Displacement")
cid_displacement_entry = Entry(frame, font=("Helvetica", 18))

# Put Labels and Entry Boxes on the Screen
bore_diameter_label.grid(row=0, column=0)
bore_diameter_entry.grid(row=0, column=1)

num_cylinders_label.grid(row=2, column=0)
num_cylinders_entry.grid(row=2, column=1, pady=20)

cid_displacement_label.grid(row=3, column=0)
cid_displacement_entry.grid(row=3, column=1)

# Button
button = Button(label_frame, text="Calculate Stroke", command=stroke)
button.pack(pady=20)

# Answer Label
stroke_label = Label(root, text="", font=("Helvetica", 18))
stroke_label.pack(pady=20)

root.mainloop()
