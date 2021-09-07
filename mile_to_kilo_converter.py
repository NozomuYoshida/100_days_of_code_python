# mile → kilo converter
import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
label_miles = tkinter.Label(text='Miles', font=('Arial', 24, 'bold'))
label_miles.grid(row=1, column=3)
window.config(padx=20, pady=20)

# Label
label_equal = tkinter.Label(text='=', font=('Arial', 24, 'bold'))
label_equal.grid(row=2, column=1)
window.config(padx=20, pady=20)

# Label
label_ans = tkinter.Label(text='xxx', font=('Arial', 24, 'bold'))
label_ans.grid(row=2, column=2)
window.config(padx=20, pady=20)

# Label
label_km = tkinter.Label(text='Km', font=('Arial', 24, 'bold'))
label_km.grid(row=2, column=3)
window.config(padx=20, pady=20)


def button_clicked():
    mile = int(input.get())
    km = mile * 1.6
    label_ans.config(text=str(km))


# Entry
input = tkinter.Entry(width=10)
input.grid(row=1, column=2)
window.config(padx=20, pady=20)

# Button
new_button = tkinter.Button(text='Calculate', command=button_clicked)
new_button.grid(row=3, column=2)
window.config(padx=20, pady=20)


window.mainloop()
