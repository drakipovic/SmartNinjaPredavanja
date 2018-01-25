import Tkinter

def convert_km_to_mile():
    km = int(entry.get())

    miles = km * 1.6

    result.delete(0, len(result.get()))
    result.insert(0, miles)

def convert_feet_to_cm():
    feet = int(entry.get())

    cm = feet * 30.48

    result.delete(0, len(result.get()))
    result.insert(0, cm)


window = Tkinter.Tk()

window.geometry("500x500")
window.title("Unit Converter")


km_label = Tkinter.Label(window, text="Unesite broj")
km_label.pack(side="left")
entry = Tkinter.Entry(window)
entry.pack(side="left")

km_to_miles_btn = Tkinter.Button(window, text="Km to Mile", command=convert_km_to_mile)
km_to_miles_btn.pack()

feet_to_cm_btn = Tkinter.Button(window, text="Feet to cm", command=convert_feet_to_cm)
feet_to_cm_btn.pack()

result_label = Tkinter.Label(window, text="Rezultat")
result_label.pack(side="bottom")

result = Tkinter.Entry(window)
result.pack(side="bottom")

window.mainloop()