import tkinter as tk
from tkinter import ttk

# This basic program is a converter of seconds: you enter with integer number and receive its larger time magnitude
# of values as for example: decades, days, hours, etc...


def total_mgm(answer, start):  # -> Function that calculates the magnitudes and constructs the answer.
    # -> List of time magnitude and yours respective seconds.
    magnums = [[' millennium(s), ', 31557600000], [' century(s), ', 3155760000], [' decade(s), ', 315352800],
               [' year(s), ', 31536000], [' month(s), ', 2626560], [' week(s), ', 604800], [' day(s), ', 86400],
               [' hour(s), ', 3600], [' minute(s) and ', 60], [' second(s).']]
    num = int(start.get())
    response = start.get() + ' -> '  # -> Here's the answer that will be constructed as per the calculations.
    mgm = num // magnums[0][1]  # -> First calculation and your output, if there's.
    after = num % magnums[0][1]
    if mgm > 0:
        response += str(mgm) + magnums[0][0]
    for i in magnums[1:9]:  # -> Others calculations and yours outputs, except the last.
        mgm = after // i[1]
        after = after % i[1]
        if mgm > 0:
            response += str(mgm) + i[0]
    response += str(after) + magnums[9][0]  # -> Last output.
    answer.insert(tk.END, response)


def main():
    try:
        conv = tk.Tk()
        conv.geometry('300x180')
        conv.config(bg='#252424')
        conv.resizable(width=False, height=False)
        conv.title('Converter of Seconds')
        func = tk.Label(conv, text="Please, enter with integer number for conversion:", bg='#252424', fg='#FFF8E7')
        func.pack()
        e = tk.StringVar()
        e.set('0')
        start = tk.Entry(conv, width=17, textvariable=e, font='times 15 bold', justify='right',  bg='#252424',
                         fg='#FFF8E7', border=5)
        start.pack()
        converter = tk.Button(conv, text='Converter', width=24, command=lambda: total_mgm(answer, start))
        converter.pack()
        clean = tk.Button(conv, text='Clean', width=24, command=lambda: answer.delete(0, tk.END))
        clean.pack()
        answer = tk.Listbox(conv, width=45, height=3,  bg='#252424', fg='#FFF8E7')
        answer.pack()
        scroll = ttk.Scrollbar(conv, orient='horizontal')
        scroll.pack(side='bottom', fill='x')
        answer.config(xscrollcommand=scroll.set)
        scroll.config(command=answer.xview)
        conv.mainloop()
    except tk.EXCEPTION as tk_error:
        alert = tk.Tk()
        if ValueError:  # -> Common error from entry.
            ttk.Label(alert, text="Could not run the code correctly. Did you enter an integer?").pack()
        else:
            ttk.Label(alert, text="An unexpected error occurred, please contact the developer.").pack()
            ttk.Label(alert, text=str(tk_error)).pack()
        alert.mainloop()


if __name__ == "__main__":
    main()
