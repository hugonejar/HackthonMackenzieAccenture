import tkinter as tk
import analog_gauge_reader


def submit():
    # retrieve values from entry widgets
    val1 = min_angle.get()
    val2 = max_angle.get()
    val3 = min_value.get()
    val4 = max_value.get()
    val5 = units.get()
    
    # print values to console
    print(val1, val2, val3, val4, val5)

def clear():
    # clear values in entry widgets
    min_angle.delete(0, tk.END)
    max_angle.delete(0, tk.END)
    min_value.delete(0, tk.END)
    max_value.delete(0, tk.END)
    units.delete(0, tk.END)

# create a tkinter window with a larger size
window = tk.Tk()
window.geometry("400x400")

# create label widgets for each input field
label1 = tk.Label(window, text="Minimum Angle")
label2 = tk.Label(window, text="Maximum Angle")
label3 = tk.Label(window, text="Minimum Value")
label4 = tk.Label(window, text="Maximum Value")
label5 = tk.Label(window, text="Units")

# create five entry widgets
min_angle = tk.Entry(window)
max_angle = tk.Entry(window)
min_value = tk.Entry(window)
max_value = tk.Entry(window)
units = tk.Entry(window)

# create two buttons
send_button = tk.Button(window, text="Send", command=submit)
clean_button = tk.Button(window, text="Clean", command=clear)

# arrange widgets in the window using grid layout
label1.grid(row=0, column=0, padx=10, pady=10)
min_angle.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
max_angle.grid(row=1, column=1, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
min_value.grid(row=2, column=1, padx=10, pady=10)
label4.grid(row=3, column=0, padx=10, pady=10)
max_value.grid(row=3, column=1, padx=10, pady=10)
label5.grid(row=4, column=0, padx=10, pady=10)
units.grid(row=4, column=1, padx=10, pady=10)
send_button.grid(row=5, column=1, padx=10, pady=10, sticky="E")
clean_button.grid(row=5, column=0, padx=10, pady=10, sticky="W")

# start the event loop
window.mainloop()
